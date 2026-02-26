from src.loader import load_all_csv
from src.preprocess import preprocess_transactions
from src.feature_engineering import add_time_features, monthly_summary
from src.analytics import expense_vs_income
from src.model import predict_next_month


def run_pipeline():
    # 1. Load
    df = load_all_csv("data/raw")

    # 2. Preprocess
    df = preprocess_transactions(df)

    # 3. Feature Engineering
    df = add_time_features(df)

    # 4. Monthly Summary
    monthly_df = monthly_summary(df)

    # 5. Basic Analytics
    income_expense = expense_vs_income(df)

    # 6. Prediction
    next_month_pred = predict_next_month(monthly_df)

    print("Monthly Summary:")
    print(monthly_df)

    print("\nIncome vs Expense:")
    print(income_expense)

    print("\nNext Month Prediction:")
    print(next_month_pred)


if __name__ == "__main__":
    run_pipeline()
