import pandas as pd


def load_dataset(file_path):
    """Load network traffic data from a CSV file."""
    return pd.read_csv(file_path)


def clean_dataset(data):
    """Remove duplicate and missing records."""
    data = data.drop_duplicates()
    data = data.dropna()

    return data


def show_dataset_info(data):
    """Display basic information about the dataset."""
    print("Dataset shape:", data.shape)
    print("\nColumns:")
    print(data.columns.tolist())
    print("\nTraffic classes:")
    if "Label" in data.columns:
        print(data["Label"].value_counts())


if __name__ == "__main__":
    print("AI-Powered Network Traffic Classification")
    print("Preprocessing module ready.")
