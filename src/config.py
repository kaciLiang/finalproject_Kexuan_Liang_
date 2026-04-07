import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
DATA_DIR    = os.path.join(BASE_DIR, '..', 'data')
RESULTS_DIR = os.path.join(BASE_DIR, '..', 'results')

INSTAGRAM_DATASET_SLUG    = "kundanbedmutha/instagram-analytics-dataset"
VIRAL_TRENDS_DATASET_SLUG = "atharvasoundankar/viral-social-media-trends-and-engagement-analysis"

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")
YOUTUBE_QUERIES = ["social media marketing", "instagram tips", "tiktok viral", "content creator"]
