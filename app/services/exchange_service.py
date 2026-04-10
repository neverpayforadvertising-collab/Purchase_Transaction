import httpx
from datetime import datetime, timedelta
from app.cache.memory_cache import MemoryCache
from app.domain.exceptions import ConversionError, ExternalAPIError

cache = MemoryCache()

class ExchangeService:
    def __init__(self, api_url: str):
        self.api_url = api_url

    async def fetch_rates(self, currency: str):
        cached = cache.get(currency)
        if cached:
            return cached

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    self.api_url,
                    params={"filter": f"country_currency_desc:{currency}"}
                )
                response.raise_for_status()
            except Exception:
                raise ExternalAPIError("Failed to fetch exchange rates")

        data = response.json()["data"]
        cache.set(currency, data, ttl=3600)
        return data

    async def convert(self, transaction, currency: str):
        rates = await self.fetch_rates(currency)

        valid = []
        for r in rates:
            d = datetime.strptime(r["record_date"], "%Y-%m-%d").date()
            if d <= transaction.transaction_date and d >= transaction.transaction_date - timedelta(days=180):
                valid.append((d, float(r["exchange_rate"])))

        if not valid:
            raise ConversionError("No valid exchange rate found")

        best = max(valid, key=lambda x: x[0])

        return {
            "id": transaction.id,
            "description": transaction.description,
            "transaction_date": transaction.transaction_date,
            "original_amount_usd": float(transaction.amount_usd),
            "exchange_rate": best[1],
            "converted_amount": round(float(transaction.amount_usd) * best[1], 2),
            "currency": currency
        }