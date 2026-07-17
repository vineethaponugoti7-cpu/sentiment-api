from fastapi.testclient import TestClient
from main import app

# TestClient lets us send requests to our API inside the test,
# without needing to start the server manually.
client = TestClient(app)


def test_home():
    """The home endpoint should return a 200 status and a message."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_predict_negative():
    """A clearly negative sentence should be classified as negative."""
    response = client.post("/predict", json={"text": "This was terrible and I am very angry"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "negative"


def test_predict_returns_sentiment():
    """Any valid request should return a sentiment field."""
    response = client.post("/predict", json={"text": "The flight was on time"})
    assert response.status_code == 200
    assert "sentiment" in response.json()


def test_predict_rejects_bad_input():
    """Sending the wrong format should be rejected with a 422 error."""
    response = client.post("/predict", json={"wrong_field": "hello"})
    assert response.status_code == 422