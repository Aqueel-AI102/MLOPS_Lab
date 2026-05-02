import pytest
import pandas as pd
from src.ingest import RatingsLoader, RatingsValidator

def test_load():
    loader = RatingsLoader()
    assert len(loader.load()) > 0

def test_deduplication():
    loader = RatingsLoader()
    df = loader.load()
    assert len(loader.deduplicate(df)) <= len(df)

def test_validate_columns():
    validator = RatingsValidator()
    df = pd.DataFrame({
        'user_id': [1],
        'movie_id': [1],
        'rating': [4],
        'timestamp': [1234567890]
    })
    assert validator.validate_columns(df)

def test_validate_types():
    validator = RatingsValidator()
    df = pd.DataFrame({
        'user_id': ['a'],
        'movie_id': [1],
        'rating': [4],
        'timestamp': [123]
    })
    _, errors = validator.validate_types(df)
    assert errors >= 1

def test_validate_ranges():
    validator = RatingsValidator()
    df = pd.DataFrame({
        'user_id': [1],
        'movie_id': [1],
        'rating': [10],
        'timestamp': [1234567890]
    })
    _, removed = validator.validate_ranges(df)
    assert removed >= 1

def test_validate_nulls():
    validator = RatingsValidator()
    df = pd.DataFrame({
        'user_id': [1],
        'movie_id': [None],
        'rating': [4],
        'timestamp': [1234567890]
    })
    _, removed = validator.validate_nulls(df)
    assert removed >= 1
