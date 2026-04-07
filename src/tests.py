"""
tests.py
--------
Run with: python tests.py
"""
import os, sys
import pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import DATA_DIR
from load import get_youtube_data, load_local_csv
from process import process_viral_trends

def _pass(msg): print(f"  PASS: {msg}")
def _fail(msg): print(f"  FAIL: {msg}")

def test_youtube_api():
    print("\n[TEST 1] YouTube Data API v3")
    df = get_youtube_data(queries=["social media engagement"], max_results=10)
    if df is None or len(df) == 0:
        _fail("YouTube API returned no data")
        return False
    expected = {"video_id", "title", "view_count", "like_count", "comment_count", "engagement_rate"}
    missing = expected - set(df.columns)
    if missing:
        _fail(f"Missing columns: {missing}")
        return False
    _pass(f"Retrieved {len(df)} videos with all required columns.")
    print(df[["title", "view_count", "like_count", "engagement_rate"]].head(3).to_string())
    return True

def test_instagram_data():
    print("\n[TEST 2] Instagram Analytics CSV")
    df = load_local_csv("Instagram_Analytics.csv")
    if df is None or len(df) == 0:
        _fail("Could not load Instagram_Analytics.csv")
        return False
    _pass(f"Loaded {len(df)} rows.")
    return True

def test_viral_trends_data():
    print("\n[TEST 3] Viral Social Media Trends CSV")
    df = load_local_csv("Cleaned_Viral_Social_Media_Trends.csv")
    if df is None or len(df) == 0:
        _fail("Could not load CSV")
        return False
    _pass(f"Loaded {len(df)} rows.")
    return True

def test_processing():
    print("\n[TEST 4] Data Processing")
    df = load_local_csv("Cleaned_Viral_Social_Media_Trends.csv")
    if df is None:
        _fail("No data to process")
        return False
    processed = process_viral_trends(df)
    if len(processed) == 0:
        _fail("Processing returned empty DataFrame")
        return False
    _pass(f"Processing works: {len(processed)} rows.")
    return True

if __name__ == "__main__":
    results = {
        "YouTube API":      test_youtube_api(),
        "Instagram CSV":    test_instagram_data(),
        "Viral Trends CSV": test_viral_trends_data(),
        "Data Processing":  test_processing(),
    }
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    for name, passed in results.items():
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    all_passed = all(results.values())
    print("\n" + ("All tests passed." if all_passed else "Some tests failed."))
    sys.exit(0 if all_passed else 1)
