# What Content and Timing Factors Drive Social Media Engagement?

**DSCI 510 - Spring 2026 | University of Southern California**
**Author:** Kexuan Liang

## Project Description

This project investigates how content features and posting timing affect user engagement across social media platforms. Using data from the YouTube Data API v3, an Instagram analytics dataset, and a multi-platform viral trends dataset, the analysis examines variables such as caption length, hashtag count, posting hour, and day of week to identify which factors are most strongly associated with engagement metrics.

## Data Sources

| # | Name | Type | Fields |
|---|------|------|--------|
| 1 | Instagram Analytics (Kaggle) | CSV file | caption_length, hashtags_count, post_hour, likes, comments, engagement_rate |
| 2 | Viral Social Media Trends (Kaggle) | CSV file | platform, content_type, likes, shares, comments, engagement_level |
| 3 | YouTube Data API v3 | API | video_id, title, published_at, view_count, like_count, comment_count |

## Setup

Install dependencies: pip install -r requirements.txt
Configure API keys: cp src/.env.example src/.env

Your src/.env should look like:
YOUTUBE_API_KEY=your_youtube_api_key_here
KAGGLE_API_TOKEN=your_kaggle_api_token_here

## Running the Project

cd src
python tests.py
python main.py
