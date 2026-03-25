from fastapi import FastAPI, Query
from app.services.currency import get_rate
from app.models.schemas import ConvertResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/convert", response_model=ConvertResponse)
def convert_currency(
    from_currency: str = Query(..., alias="from"),
    to_currency: str = Query(..., alias="to"),
    amount: float = Query(...)
):
    rate = get_rate(from_currency, to_currency)
    result = amount * rate

    return ConvertResponse(
        from_currency=from_currency,
        to_currency=to_currency,
        amount=amount,
        result=result
    )