import pandas as pd


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    날짜 기반 파생 변수 생성
    """
    df = df.copy()

    if "date" in df.columns:
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month
        df["year_month"] = df["date"].dt.to_period("M")

    return df


def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    월별 총 지출 집계
    """
    if "year_month" not in df.columns:
        raise ValueError("year_month column not found. Run add_time_features first.")

    summary = (
        df.groupby("year_month")["amount"]
        .sum()
        .reset_index()
        .sort_values("year_month")
    )

    summary.rename(columns={"amount": "monthly_total"}, inplace=True)

    return summary
