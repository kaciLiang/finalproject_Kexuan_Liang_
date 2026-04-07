# What Content and Timing Factors Drive Social Media Engagement?

**DSCI 510 – Spring 2026 | University of Southern California**  
**Author:** Kexuan Liang

---

## Project Description

This project investigates how content features and posting timing affect user engagement across social media platforms. Using data from the X (Twitter) API, an Instagram analytics dataset, and a multi-platform viral trends dataset, the analysis examines variables such as caption length, hashtag count, posting hour, and day of week to identify which factors are most strongly associated with engagement metrics (likes, comments, shares, engagement rate).

---

## Data Sources

| # | Name | Type | Fields |
|---|------|------|--------|
| 1 | Instagram Analytics (Kaggle) | CSV file | caption_length, hashtags_count, post_hour, likes, comments, engagement_rate |
| 2 | Viral Social Media Trends (Kaggle) | CSV file | platform, content_type, likes, shares, comments, engagement_level |
| 3 | X (Twitter) API | API | tweet.text, tweet.id, author_id, created_at, public_metrics |

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API keys
```bash
cp src/.env.example src/.env
# Edit src/.env and fill in your actual tokens
```

Your `src/.env` should look like:
```
X_BEARER_TOKEN=your_x_bearer_token_here
KAGGLE_API_TOKEN=your_kaggle_api_token_here
```

### 4. Add CSV data files
Place the following files in the `data/` directory (not committed to GitHub):
- `Instagram_Analytics.csv`
- `Cleaned_Viral_Social_Media_Trends.csv`

---

## Running the Project

```bash
# Run tests (verifies API connection)
cd src
python tests.py

# Run full pipeline
python main.py
```

---

## Project Structure

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── doc/
│   └── Kexuan_Liang_progress_report.pdf
├── src/
│   ├── .env.example       # Template – copy to .env
│   ├── config.py          # Paths and constants
│   ├── load.py            # Data loading (Kaggle + X API)
│   ├── process.py         # Cleaning & feature engineering
│   ├── analyze.py         # Correlation analysis & plots
│   ├── main.py            # Full pipeline runner
│   └── tests.py           # API and data tests
├── data/                  # ← gitignored, not committed
└── results/               # ← gitignored, not committed
```
