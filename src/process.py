import pandas as pd
import numpy as np


def process_instagram(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the Instagram Analytics dataset.
    """
    print("--- Processing Instagram dataset ---")
    df = df.copy()

    required = ["likes", "comments", "engagement_rate"]
    df = df.dropna(subset=required)

    numeric_cols = [
        "likes", "comments", "shares", "saves",
        "engagement_rate", "caption_length",
        "hashtags_count", "post_hour", "follower_count",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "day_of_week" in df.columns:
        df["day_of_week"] = df["day_of_week"].astype(str)

    print(f"  Instagram: {len(df)} rows after cleaning.")
    return df


def process_viral_trends(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the Viral Social Media Trends dataset.
    """
    print("--- Processing Viral Trends dataset ---")
    df = df.copy()

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    required = ["likes", "comments"]
    df = df.dropna(subset=required)

    numeric_cols = ["views", "likes", "shares", "comments"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "engagement_rate" not in df.columns and "views" in df.columns:
        df["engagement_rate"] = (
            (df["likes"] + df["comments"] + (df["shares"] if "shares" in df.columns else 0))
            / df["views"].replace(0, np.nan)
        )

    if "post_date" in df.columns:
        df["post_date"] = pd.to_datetime(df["post_date"], errors="coerce")
        df["post_hour"] = df["post_date"].dt.hour
        df["day_of_week"] = df["post_date"].dt.day_name()

    print(f"  Viral Trends: {len(df)} rows after cleaning.")
    return df
