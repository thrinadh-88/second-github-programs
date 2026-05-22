import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def create_sample_dataframe(rows: int = 20) -> pd.DataFrame:
    """Create a sample DataFrame with dates and numeric series."""
    dates = pd.date_range(start="2026-01-01", periods=rows, freq="D")
    values = np.cumsum(np.random.randn(rows) * 10 + 5)
    data = pd.DataFrame({
        "date": dates,
        "value": values,
        "value_squared": values ** 2,
    })
    data.set_index("date", inplace=True)
    return data


def analyze_data(df: pd.DataFrame) -> pd.DataFrame:
    """Add rolling mean and percent change to the DataFrame."""
    result = df.copy()
    result["rolling_mean"] = result["value"].rolling(window=5, min_periods=1).mean()
    result["pct_change"] = result["value"].pct_change().fillna(0) * 100
    return result


def plot_data(df: pd.DataFrame) -> None:
    """Plot the data using Matplotlib."""
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df["value"], marker="o", label="Value")
    plt.plot(df.index, df["rolling_mean"], linestyle="--", label="5-Day Rolling Mean")
    plt.title("Sample NumPy + pandas + Matplotlib Analysis")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("sample_plot.png")
    plt.show()


def main() -> None:
    df = create_sample_dataframe(rows=30)
    df = analyze_data(df)
    print("Sample DataFrame:\n", df.head(10))
    plot_data(df)


if __name__ == "__main__":
    main()

