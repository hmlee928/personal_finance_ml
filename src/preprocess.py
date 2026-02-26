import pandas as pd


def preprocess_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    기본 전처리:
    - 날짜 컬럼 datetime 변환
    - 금액 컬럼 숫자형 변환
    - 결측값 제거
    """

    df = df.copy()

    # 날짜 처리 (컬럼 이름은 나중에 맞춰 조정 가능)
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # 금액 처리
    if "amount" in df.columns:
        df["amount"] = (
            df["amount"]
            .astype(str)
            .str.replace(",", "")
            .astype(float)
        )

    # 결측값 제거
    df = df.dropna()

    return df
