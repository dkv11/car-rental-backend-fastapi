import os 

class Settings:
    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "Car Rental Backend")
        self.environment = os.getenv("ENV", "development")

        self.database_url = os.getenv("DATABASE_URL")

        self.jwt_secret_key = os.getenv("JWT_SECRET_KEY")
        self.jwt_algorithm = os.getenv("JWT_ALGORITHM", "HS256")
        self.jwt_expire_minutes = int(os.getenv("JWT_EXPIRE_MINUTES", "60"))

        self._validate_required_settings()

    def _validate_required_settings(self):

        if not self.database_url:
            raise ValueError("DATABASE_URL is required")
        if not self.jwt_secret_key:
            raise ValueError("JWT_SECRET_KEY is required")

settings = Settings()
