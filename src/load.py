"""
load.py - Data loading from Kaggle CSVs and YouTube API
"""
import os
import requests
import pandas as pd
from config import DATA_DIR

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")

def load_local_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return None
    df = pd.read_csv(path)
    print(f"Loaded local CSV '{filename}': {len(df)} rows.")
    return df

def get_youtube_data(queries=None, max_results=50):
    """
    Fetches YouTube videos via YouTube Data API v3.
    Collects: title, view_count, like_count, comment_count,
              published_at, duration, tags
    """
    if not YOUTUBE_API_KEY:
        print("Error: YOUTUBE_API_KEY not set.")
        return None

    if queries is None:
        queries = ["social media marketing", "instagram tips", "tiktok viral", "content creator"]

    print("--- Fetching videos from YouTube API ---")
    all_rows = []

    for query in queries:
        print(f"  Searching: '{query}'")
        search_url = "https://www.googleapis.com/youtube/v3/search"
        search_params = {
            "part": "id",
            "q": query,
            "type": "video",
            "maxResults": max_results,
            "key": YOUTUBE_API_KEY,
        }
        r = requests.get(search_url, params=search_params)
        if r.status_code != 200:
            print(f"  Search error {r.status_code}: {r.text}")
            continue

        video_ids = [item["id"]["videoId"] for item in r.json().get("items", [])]
        if not video_ids:
            continue

        stats_url = "https://www.googleapis.com/youtube/v3/videos"
        stats_params = {
            "part": "snippet,statistics",
            "id": ",".join(video_ids),
            "key": YOUTUBE_API_KEY,
        }
        r2 = requests.get(stats_url, params=stats_params)
        if r2.status_code != 200:
            print(f"  Stats error {r2.status_code}: {r2.text}")
            continue

        for item in r2.json().get("items", []):
            snip = item.get("snippet", {})
            stats = item.get("statistics", {})
            all_rows.append({
                "video_id":      item.get("id"),
                "title":         snip.get("title"),
                "published_at":  snip.get("publishedAt"),
                "channel":       snip.get("channelTitle"),
                "tags_count":    len(snip.get("tags", [])),
                "title_length":  len(snip.get("title", "")),
                "view_count":    int(stats.get("viewCount", 0)),
                "like_count":    int(stats.get("likeCount", 0)),
                "comment_count": int(stats.get("commentCount", 0)),
                "query":         query,
            })

    if not all_rows:
        print("No videos collected.")
        return None

    df = pd.DataFrame(all_rows)
    df["engagement"] = df["like_count"] + df["comment_count"]
    df["engagement_rate"] = df["engagement"] / df["view_count"].replace(0, 1)

    df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce")
    df["post_hour"] = df["published_at"].dt.hour
    df["day_of_week"] = df["published_at"].dt.day_name()

    print(f"  Total videos collected: {len(df)}")
    return df

def save_data(df, filename):
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, filename)
    df.to_csv(path, index=False)
    print(f"Saved {len(df)} rows → {path}")
