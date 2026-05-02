import pandas as pd
import json
import logging
from pathlib import Path
from src.config import RATINGS_SCHEMA, DATA_PATHS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

<<<<<<< HEAD
=======

>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099
class RatingsValidator:

    def __init__(self, schema=RATINGS_SCHEMA):
        self.schema = schema
        self.report = {}

    def validate_columns(self, df):
<<<<<<< HEAD
        if set(df.columns) != set(self.schema.keys()):
=======
        required = set(self.schema.keys())
        if set(df.columns) != required:
>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099
            raise ValueError("Column mismatch")
        return True

    def validate_types(self, df):
        errors = 0
<<<<<<< HEAD
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            errors += df[col].isnull().sum()
=======
        for col, rules in self.schema.items():
            try:
                df[col] = pd.to_numeric(df[col], errors='coerce')
                errors += df[col].isnull().sum()
            except:
                pass
>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099
        return df, errors

    def validate_ranges(self, df):
        before = len(df)
        for col, rules in self.schema.items():
<<<<<<< HEAD
            df = df[(df[col] >= rules['min']) & (df[col] <= rules['max'])]
        return df, before - len(df)
=======
            if 'min' in rules and 'max' in rules:
                df = df[(df[col] >= rules['min']) & (df[col] <= rules['max'])]
        removed = before - len(df)
        return df, removed
>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099

    def validate_nulls(self, df):
        before = len(df)
        df = df.dropna()
<<<<<<< HEAD
        return df, before - len(df)

    def run_all(self, df):
        self.validate_columns(df)
=======
        removed = before - len(df)
        return df, removed

    def run_all(self, df):
        self.validate_columns(df)

>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099
        df, dtype_errors = self.validate_types(df)
        df, range_removed = self.validate_ranges(df)
        df, null_removed = self.validate_nulls(df)

        self.report = {
            "total_rows_after_cleaning": len(df),
            "dtype_errors": int(dtype_errors),
            "range_violations": int(range_removed),
            "null_violations": int(null_removed)
        }

        return df, self.report


class RatingsLoader:

    def __init__(self, filepath=DATA_PATHS['raw']):
        self.filepath = filepath
        self.validator = RatingsValidator()

    def load(self):
<<<<<<< HEAD
        df = pd.read_csv(self.filepath, sep='\t')
=======
        if not Path(self.filepath).exists():
            raise FileNotFoundError("File not found")
        df = pd.read_csv(self.filepath, sep=' ')
>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099
        logger.info(f"Loaded {len(df)} rows")
        return df

    def deduplicate(self, df):
        before = len(df)
        df = df.drop_duplicates(['user_id', 'movie_id'], keep='last')
        logger.info(f"Removed {before - len(df)} duplicates")
        return df

    def process(self):
        df = self.load()
<<<<<<< HEAD
=======

>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099
        df = self.deduplicate(df)

        clean_df, report = self.validator.run_all(df)

        Path(DATA_PATHS['processed']).parent.mkdir(parents=True, exist_ok=True)
        clean_df.to_csv(DATA_PATHS['processed'], index=False)

        Path(DATA_PATHS['validation_report']).parent.mkdir(parents=True, exist_ok=True)
        with open(DATA_PATHS['validation_report'], 'w') as f:
            json.dump(report, f, indent=2)

        logger.info("Pipeline completed successfully")


def main():
<<<<<<< HEAD
    RatingsLoader().process()
=======
    loader = RatingsLoader()
    loader.process()

>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099

if __name__ == "__main__":
    main()