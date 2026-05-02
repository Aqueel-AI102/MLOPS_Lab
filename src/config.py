RATINGS_SCHEMA = {
    'user_id': {'dtype': 'int64', 'min': 1, 'max': 1000},
    'movie_id': {'dtype': 'int64', 'min': 1, 'max': 1700},
    'rating': {'dtype': 'float64', 'min': 0.5, 'max': 5.0},
    'timestamp': {'dtype': 'int64', 'min': 1000000000, 'max': 2000000000}
}

DATA_PATHS = {
    'raw': 'data/raw/ratings.csv',
    'processed': 'data/processed/ratings_clean.csv',
    'validation_report': 'evaluations/validation_report.json'
}