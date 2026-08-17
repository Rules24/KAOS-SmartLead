from flask import Blueprint, render_template, request, jsonify

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError


sayfalar_bp = Blueprint("sayfalar", __name__)
api_bp = Blueprint("api", __name__)


@sayfalar_bp.route("/", methods=["GET"])
def ana_sayfa():
    return render_template("index.html")


@sayfalar_bp.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")


@api_bp.route("/sohbet", methods=["POST"])
def sohbet():
    veri = request.get_json(silent=True) or {}

    mesaj = veri.get("mesaj")
    gecmis = veri.get("gecmis", [])

    if not mesaj:
        return jsonify({
            "basari": False,
            "hata": "Mesaj alani zorunludur."
        }), 400

    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)

        return jsonify({
            "basari": True,
            "cevap": cevap
        })

    except AIServiceError:
        return jsonify({
            "basari": False,
            "hata": "Yapay zeka servisine su anda ulasilamiyor."
        }), 503


@api_bp.route("/leads", methods=["POST"])
def lead_kaydet():
    try:
        veri = request.get_json(silent=True) or {}

        isim = veri.get("isim")
        telefon = veri.get("telefon")
        mesaj = veri.get("mesaj")

        if not isim or not telefon:
            return jsonify({
                "basari": False,
                "hata": "Isim ve telefon alanlari zorunludur."
            }), 400

        lead_ekle(isim, telefon, mesaj)

        return jsonify({
            "basari": True,
            "mesaj": "Lead basariyla kaydedildi."
        }), 201

    except Exception as hata:
        print("Lead kaydetme hatasi:", hata)

        return jsonify({
            "basari": False,
            "hata": "Lead kaydedilirken bir hata olustu."
        }), 500


@api_bp.route("/leads", methods=["GET"])
def leadleri_getir():
    try:
        leadler = tum_leadler()

        sonuc = []

        for lead in leadler:
            sonuc.append({
                "id": lead["id"],
                "isim": lead["isim"],
                "telefon": lead["telefon"],
                "mesaj": lead["mesaj"],
                "tarih": lead["tarih"]
            })

        return jsonify({
            "basari": True,
            "leadler": sonuc
        })

    except Exception as hata:
        print("Lead listeleme hatasi:", hata)

        return jsonify({
            "basari": False,
            "hata": "Lead verileri alinirken bir hata olustu."
        }), 500
    })
