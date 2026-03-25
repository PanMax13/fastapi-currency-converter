from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_convert_currency(monkeypatch):
        def _get_rate(from_currency, to_currency):
            return 0.9

        monkeypatch.setattr("app.main.get_rate", _get_rate)

        response = client.get("/convert?amount=100&from=USD&to=EUR")

        assert response.status_code == 200

        data = response.json()

        # Original case: USD to EUR
        assert data["from_currency"] == "USD"
        assert data["to_currency"] == "EUR"
        assert data["amount"] == 100
        assert data["result"] == 90

        # Additional case: EUR to USD
        response2 = client.get("/convert?amount=200&from=EUR&to=USD")
        data2 = response2.json()
        assert response2.status_code == 200
        assert data2["from_currency"] == "EUR"
        assert data2["to_currency"] == "USD"
        assert data2["amount"] == 200
        assert data2["result"] == 180  # 200 * 0.9

        # Additional case: JPY to GBP
        response3 = client.get("/convert?amount=50&from=JPY&to=GBP")
        data3 = response3.json()
        assert response3.status_code == 200
        assert data3["from_currency"] == "JPY"
        assert data3["to_currency"] == "GBP"
        assert data3["amount"] == 50
        assert data3["result"] == 45  # 50 * 0.9

        # Additional case: lowercased currency codes
        response4 = client.get("/convert?amount=10&from=usd&to=eur")
        data4 = response4.json()
        assert response4.status_code == 200
        assert data4["from_currency"].upper() == "USD"
        assert data4["to_currency"].upper() == "EUR"
        assert data4["amount"] == 10
        assert data4["result"] == 9  # 10 * 0.9

        