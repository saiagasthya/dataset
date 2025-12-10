from pathlib import Path
import pandas as pd
import os

# Resolve project root (two levels up from this script) so paths work on Windows without backslash escapes
PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "Amazon_Unlocked_Mobile.csv"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_GOOD = OUTPUT_DIR / "good_records.csv"
OUTPUT_BAD = OUTPUT_DIR / "bad_records.csv"

def load_data(path):
    print("📥 Loading dataset...")
    return pd.read_csv(path)

# --------------------------
# 2. Clean & Segregate Data
# --------------------------
def segregate_records(df):
    print("🧹 Cleaning & splitting data...")

    # Mark duplicates
    df["is_duplicate"] = df.duplicated()

    # Define conditions for GOOD data
    good_condition = (
        df["Rating"].between(1, 5) &       # rating 1–5
        df["Reviews"].notna() &            # no missing reviews
        df["Reviews"].str.len() > 5 &      # review length > 5
        (df["is_duplicate"] == False)      # not duplicate
    )

    good_records = df[good_condition]
    bad_records = df[~good_condition]

    return good_records, bad_records

# --------------------------
# 3. Save data to output folder
# --------------------------
def save_output(good, bad):
    print("💾 Saving segregated files...")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    good.to_csv(OUTPUT_GOOD, index=False)
    bad.to_csv(OUTPUT_BAD, index=False)

    print(f"✔ Good records saved to: {OUTPUT_GOOD}")
    print(f"✔ Bad records saved to: {OUTPUT_BAD}")

# --------------------------
# 4. Main Flow
# --------------------------
if __name__ == "__main__":
    df = load_data(INPUT_FILE)
    good, bad = segregate_records(df)
    save_output(good, bad)
    print("✅ Segregation complete!")