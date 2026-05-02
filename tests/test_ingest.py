import pytest
import pandas as pd
from src.ingest import RatingsLoader, RatingsValidator

def test_load():
    loader = RatingsLoader()
<<<<<<< HEAD
    assert len(loader.load()) > 0
=======
    df = loader.load()
    assert len(df) > 0
>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099

def test_deduplication():
    loader = RatingsLoader()
    df = loader.load()
<<<<<<< HEAD
    assert len(loader.deduplicate(df)) <= len(df)
=======
    df2 = loader.deduplicate(df)
    assert len(df2) <= len(df)
>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099

def test_validate_columns():
    validator = RatingsValidator()
    df = pd.DataFrame({
        'user_id': [1],
        'movie_id': [1],
        'rating': [4],
        'timestamp': [1234567890]
    })
<<<<<<< HEAD
    assert validator.validate_columns(df)
=======
    assert validator.validate_columns(df) == True
>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099

def test_validate_types():
    validator = RatingsValidator()
    df = pd.DataFrame({
        'user_id': ['a'],
        'movie_id': [1],
        'rating': [4],
        'timestamp': [123]
    })
<<<<<<< HEAD
    _, errors = validator.validate_types(df)
=======
    df, errors = validator.validate_types(df)
>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099
    assert errors >= 1

def test_validate_ranges():
    validator = RatingsValidator()
    df = pd.DataFrame({
        'user_id': [1],
        'movie_id': [1],
<<<<<<< HEAD
        'rating': [10],
        'timestamp': [1234567890]
    })
    _, removed = validator.validate_ranges(df)
=======
        'rating': [10],  # invalid
        'timestamp': [1234567890]
    })
    df, removed = validator.validate_ranges(df)
>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099
    assert removed >= 1

def test_validate_nulls():
    validator = RatingsValidator()
    df = pd.DataFrame({
        'user_id': [1],
        'movie_id': [None],
        'rating': [4],
        'timestamp': [1234567890]
    })
<<<<<<< HEAD
    _, removed = validator.validate_nulls(df)
    assert removed >= 1
=======
    df, removed = validator.validate_nulls(df)
    assert removed >= 1
>>>>>>> c6682f99dc999e3fc7b7f2a8b9a0bcf04fe51099
