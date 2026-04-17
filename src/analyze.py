
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")          # headless (no display needed)
import matplotlib.pyplot as plt

from config import RESULTS_DIR


def ensure_results_dir():
    os.makedirs(RESULTS_DIR, exist_ok=True)


# Correlation

def compute_correlations(df: pd.DataFrame, target: str = "engagement_rate") -> pd.Series:
    numeric_df = df.select_dtypes(include="number")
    if target not in numeric_df.columns:
        print(f"  Warning: '{target}' not found for correlation.")
        return pd.Series(dtype=float)
    correlations = numeric_df.corr()[target].drop(target).sort_values(ascending=False)
    print(f"\nCorrelations with '{target}':\n{correlations}\n")
    return correlations


# Plots

def plot_correlation_bar(correlations: pd.Series, dataset_name: str) -> None:
    # Bar chart
    ensure_results_dir()
    if correlations.empty:
        return

    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ["steelblue" if v >= 0 else "tomato" for v in correlations.values]
    correlations.plot(kind="bar", color=colors, ax=ax)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title(f"{dataset_name} – Correlation with Engagement Rate")
    ax.set_ylabel("Pearson r")
    ax.set_xlabel("Feature")
    plt.tight_layout()

    path = os.path.join(RESULTS_DIR, f"{dataset_name}_correlation.png")
    fig.savefig(path, dpi=120)
    plt.close(fig)
    print(f"Saved → {path}")


def plot_engagement_by_hour(df: pd.DataFrame, dataset_name: str,
                            engagement_col: str = "engagement_rate") -> None:
     # plot by hour
    ensure_results_dir()
    if "post_hour" not in df.columns or engagement_col not in df.columns:
        print(f"  Skipping hour plot for {dataset_name} (missing columns).")
        return

    hourly = df.groupby("post_hour")[engagement_col].mean()

    fig, ax = plt.subplots(figsize=(8, 4))
    hourly.plot(ax=ax, marker="o", color="steelblue")
    ax.set_title(f"{dataset_name} – Avg Engagement by Posting Hour")
    ax.set_xlabel("Hour of Day (0–23)")
    ax.set_ylabel(f"Mean {engagement_col}")
    ax.set_xticks(range(0, 24))
    plt.tight_layout()

    path = os.path.join(RESULTS_DIR, f"{dataset_name}_by_hour.png")
    fig.savefig(path, dpi=120)
    plt.close(fig)
    print(f"Saved → {path}")


def plot_engagement_by_platform(df: pd.DataFrame, dataset_name: str,
                                platform_col: str = "platform",
                                engagement_col: str = "engagement_rate") -> None:
    #Box plot of engagement
    ensure_results_dir()
    if platform_col not in df.columns or engagement_col not in df.columns:
        print(f"  Skipping platform plot for {dataset_name} (missing columns).")
        return

    fig, ax = plt.subplots(figsize=(8, 5))
    df.boxplot(column=engagement_col, by=platform_col, ax=ax)
    ax.set_title(f"{dataset_name} – Engagement by Platform")
    plt.suptitle("")
    ax.set_xlabel("Platform")
    ax.set_ylabel(engagement_col)
    plt.tight_layout()

    path = os.path.join(RESULTS_DIR, f"{dataset_name}_by_platform.png")
    fig.savefig(path, dpi=120)
    plt.close(fig)
    print(f"Saved → {path}")


def run_full_analysis(df: pd.DataFrame, dataset_name: str,
                      engagement_col: str = "engagement_rate") -> None:
    print(f"Analysing: {dataset_name}")
    correlations = compute_correlations(df, target=engagement_col)
    plot_correlation_bar(correlations, dataset_name)
    plot_engagement_by_hour(df, dataset_name, engagement_col)
    plot_engagement_by_platform(df, dataset_name, engagement_col)
