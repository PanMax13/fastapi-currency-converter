from app.services.currency import get_rate

def test_get_rate_for_success(monkeypatch):
    class Response:
        def json(self):
            return {
                "result": "success",
                "conversion_rates": {
                    "EUR": 0.9,
                    "USD": 1.0,
                    "JPY": 156.15,
                    "GBP": 0.81
                }
            }

    def get(*args, **kwargs):
        return Response()

    monkeypatch.setattr("requests.get", get)

    rate = get_rate("USD", "EUR")
    assert rate == 0.9

    rate = get_rate("EUR", "USD")
    assert rate == 1.0