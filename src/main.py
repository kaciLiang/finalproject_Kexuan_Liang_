
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import DATA_DIR, RESULTS_DIR
from load import get_youtube_data, load_local_csv, save_data
from process import process_instagram, process_viral_trends
from analyze import run_full_analysis

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

def main():
    print("Running social media analysis")

    print("Instagram Analytics")
    ig_raw = load_local_csv("Instagram_Analytics.csv")
    if ig_raw is not None:
        ig = process_instagram(ig_raw)
        run_full_analysis(ig, "Instagram", engagement_col="engagement_rate")

    print("Viral Social Media Trends")
    vt_raw = load_local_csv("Cleaned_Viral_Social_Media_Trends.csv")
    if vt_raw is not None:
        vt = process_viral_trends(vt_raw)
        run_full_analysis(vt, "ViralTrends", engagement_col="engagement_rate")

    print("YouTube API")
    yt_raw = get_youtube_data()
    if yt_raw is not None:
        save_data(yt_raw, "youtube_collected.csv")
        run_full_analysis(yt_raw, "YouTube", engagement_col="engagement_rate")

    print(" Check results")

if __name__ == "__main__":
    main()
