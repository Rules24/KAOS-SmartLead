import os
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri yükle
load_dotenv()


class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "kaos-smartlead-development-key"
    )

    DATABASE_URL = os.environ.get(
        "DATABASE_URL",
        "sqlite:///smartlead.db"
    )

    GROQ_API_KEY = os.environ.get(
        "GROQ_API_KEY",
        ""
    )

    AI_PROVIDER = os.environ.get(
        "AI_PROVIDER",
        "groq"
    )

    BUSINESS_CONTEXT = os.environ.get(
        "BUSINESS_CONTEXT",
        """
        Sen KAOS Technology'nin yapay zekâ destekli asistanısın.
        KAOS Technology; teknoloji, dijital çözümler ve yenilikçi
        iş süreçleri alanında hizmet veren bir markadır.
        Kullanıcılara profesyonel, anlaşılır, çözüm odaklı ve
        yenilikçi bir iletişim diliyle yardımcı ol.
        """
    )

    CORS_ORIGINS = os.environ.get(
        "CORS_ORIGINS",
        "http://localhost:5000"
    )

    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}