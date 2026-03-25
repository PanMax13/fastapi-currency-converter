# Currency Converter API

A simple FastAPI-based currency converter microservice that retrieves real-time exchange rates from the [ExchangeRate-API](https://www.exchangerate-api.com/).

## Features

- Convert currencies using up-to-date exchange rates
- RESTful API endpoints
- Dockerized for easy deployment
- Automated testing and CI with GitHub Actions

## Requirements

- Python 3.10 or higher (recommended 3.13 for development)
- Docker & Docker Compose (for containerization)
- ExchangeRate-API key ([Free API key here](https://www.exchangerate-api.com/))

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/currency-converter-api.git
cd currency-converter-api
```

### 2. Set up Environment Variables

Create a `.env` file in the root of your project and add your API key:

```env
API=your_exchange_rate_api_key
```

### 3. Running Locally

#### With Docker Compose

```sh
docker-compose up --build
```

Visit the API at [http://localhost:8000](http://localhost:8000)

#### Without Docker

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
2. Start the FastAPI server:
    ```sh
    uvicorn app.main:app --reload
    ```

### 4. API Usage

#### Endpoint: `/convert`

**Example request:**

```
GET /convert?from=USD&to=EUR
```

**Parameters:**
- `from` (str): The source currency code (e.g., `USD`)
- `to` (str): The target currency code (e.g., `EUR`)

**Example response:**
```json
{
  "from": "USD",
  "to": "EUR",
  "rate": 0.91
}
```

### 5. Running Tests

```sh
PYTHONPATH=. pytest -v
```

Or, tests will run automatically via GitHub Actions on each push to the `test` branch.

### 6. Project Structure

```
.
├── app/
│   ├── main.py
│   └── services/
│       └── currency.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── .gitignore
```

### 7. Continuous Integration

- CI config: [`.github/workflows/test.yml`](.github/workflows/test.yml)
- Upon push to `test` branch:
    - Runs all tests
    - If tests pass, merges and pushes changes to `main` branch automatically

---

## License

MIT License

## Maintainer

- [PanMax13](mailto:panezhamax@gmail.com)

