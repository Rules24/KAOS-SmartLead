from flask import Flask, jsonify
from flask_cors import CORS

from config import config
from app.database import init_db
from app.routes import sayfalar_bp, api_bp


def create_app(config_name="development"):
    app = Flask(__name__)

    # 1. Ayarları yükle
    app.config.from_object(config[config_name])

    # 2. CORS'u aç
    CORS(
        app,
        origins=app.config.get("CORS_ORIGINS", "*")
    )

    # 3. Veritabanını başlat
    with app.app_context():
        init_db(app)

    # 4. Blueprint'leri kaydet
    app.register_blueprint(sayfalar_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    # 5. Sunucu canlılık kontrolü
    @app.route("/health")
    def health():
        return jsonify({
            "basari": True,
            "durum": "aktif"
        })

    # 6. Uygulamayı döndür
    return app