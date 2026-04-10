from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # App
    app_name: str = "Purchase Transaction API"
    debug: bool = True

    # Database
    database_url: str = Field(
        default="sqlite:///./test.db",
        description="Database connection string"
    )

    # External API
    treasury_api_url: str = Field(
        default="https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/rates_of_exchange",
        description="US Treasury Rates of Exchange API"
    )

    # Business rules
    max_description_length: int = 50
    exchange_rate_lookback_days: int = 180  # 6 months

    # HTTP client
    http_timeout_seconds: int = 10

    class Config:
        env_file = ".env"
        case_sensitive = False


# Singleton instance
settings = Settings()