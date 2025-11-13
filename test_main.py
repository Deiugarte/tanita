import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_user():
    """Test the user endpoint returns a valid response"""
    response = client.get("/user/1")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "age" in data
    assert "gender" in data
    assert "height" in data
    assert "weight" in data


def test_read_body_composition():
    """Test the body composition endpoint returns a valid response"""
    response = client.get("/user/1/body-composition")
    assert response.status_code == 200
    data = response.json()
    # Check that the response has the expected structure
    assert isinstance(data, dict)


def test_read_segment_analysis():
    """Test the segment analysis endpoint returns a list"""
    response = client.get("/user/1/segment-analysis")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_historical_weight_data():
    """Test the historical weight data endpoint"""
    response = client.get("/user/1/historical-data/weight")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_historical_fat_data():
    """Test the historical fat data endpoint"""
    response = client.get("/user/1/historical-data/fat")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_historical_muscle_data():
    """Test the historical muscle data endpoint"""
    response = client.get("/user/1/historical-data/muscle")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_app_health():
    """Test that the app can start and respond to requests"""
    response = client.get("/docs")
    assert response.status_code == 200
