# What Content and Timing Factors Drive Social Media Engagement?
**DSCI 510 - Spring 2026 | University of Southern California**
**Author:** Kexuan Liang

## Project Description
This project investigates how content features and posting timing affect user engagement across social media platforms. Using data from the YouTube Data API v3, an Instagram analytics dataset, and a multi-platform viral trends dataset, the analysis examines variables such as caption length, hashtag count, posting hour, and day of week to identify which factors are most strongly associated with engagement metrics.

## Data Sources

| # | Name | Type | Fields | Format | Link |
|---|------|------|--------|--------|------|
| 1 | Instagram Engagement Analytics | File (Kaggle) | caption_length, hashtags_count, post_hour, likes, comments, engagement_rate | CSV | https://www.kaggle.com/datasets/kundanbedmutha/instagram-analytics-dataset |
| 2 | Viral Social Media Trends | File (Kaggle) | caption_length, hashtags_count, likes, comments, shares, engagement_rate | CSV | https://www.kaggle.com/datasets/atharvasoundankar/viral-social-media-trends-and-engagement-analysis |
| 3 | YouTube Data API v3 | API | video_id, title, published_at, view_count, like_count, comment_count | JSON | https://developers.google.com/youtube/v3 |

## Results
_To be updated in final submission._

## Installation

1. Install dependencies:
pip install -r requirements.txt
2. Configure API keys:
cp src/.env.example src/.env
Your `src/.env` should look like:
YOUTUBE_API_KEY=your_youtube_api_key_here
KAGGLE_API_TOKEN=your_kaggle_api_token_here
## Running the Project

From the `src/` directory run:
python tests.py
python main.py
Results will appear in the `results/` folder. All obtained data will be stored in `data/`.
