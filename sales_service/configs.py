from prettyconf import config


class Settings:
    DATABASE_URL = config("DATABASE_URL")
    EXTERNAL_API_TOKEN = config("EXTERNAL_API_TOKEN")


settings = Settings()
