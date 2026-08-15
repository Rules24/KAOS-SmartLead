# KAOS SmartLead AI

KAOS SmartLead AI, KAOS Technology için geliştirilen yapay zekâ destekli müşteri iletişim ve lead yönetim sistemidir.

Sistem, kullanıcıların yapay zekâ asistanına soru sormasını, iletişim bilgilerini bırakmasını ve oluşturulan lead kayıtlarının yönetim panelinden görüntülenmesini sağlar.

## Projenin Amacı

SmartLead AI iki temel arayüzden oluşur:

- **B2C Karşılama Sayfası:** Kullanıcı yapay zekâ asistanına soru sorabilir ve isim/telefon bilgilerini bırakarak lead oluşturabilir.
- **B2B Yönetim Paneli:** Kaydedilen lead'ler isim, telefon, mesaj ve tarih bilgileriyle görüntülenebilir.

## Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- Groq API
- Wix Studio / Velo
- GitHub
- Render
- Gunicorn

## Proje Mimarisi

Proje Separation of Concerns (SoC) yaklaşımına göre katmanlara ayrılmıştır.

- `config.py` — uygulama yapılandırması
- `app/database.py` — veritabanı işlemleri
- `app/services/ai_service.py` — yapay zekâ servisi
- `app/routes.py` — API endpoint'leri
- `app/__init__.py` — Flask uygulama fabrikası
- `run.py` — uygulamanın giriş noktası

## API Endpoint'leri

- `GET /health` — backend sağlık kontrolü
- `POST /api/sohbet` — yapay zekâ sohbet servisi
- `POST /api/leads` — yeni lead kaydı
- `GET /api/leads` — kayıtlı lead'lerin listelenmesi

## Yerel Kurulum

Projeyi klonlayın:

```bash
git clone https://github.com/Rules24/KAOS-SmartLead.git
cd KAOS-SmartLead
```

Sanal ortam oluşturun:

```bash
python -m venv venv
```

Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

`.env` dosyası oluşturun ve gerekli ortam değişkenlerini tanımlayın:

```env
GROQ_API_KEY=your_api_key
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///smartlead.db
AI_PROVIDER=groq
CORS_ORIGINS=*
```

Uygulamayı çalıştırın:

```bash
python run.py
```

Yerel backend varsayılan olarak `http://127.0.0.1:5000` adresinde çalışır.

## Canlı Backend

Backend Render üzerinde yayınlanmıştır.

`https://kaos-smartlead.onrender.com`

Sağlık kontrolü:

`https://kaos-smartlead.onrender.com/health`

## Güvenlik

- API anahtarları `.env` dosyasında saklanır.
- `.env` dosyası GitHub deposuna dahil edilmez.
- Hassas bilgiler ortam değişkenleri üzerinden yönetilir.
- CORS yapılandırması uygulanmıştır.
- Veritabanı işlemlerinde parametreli sorgular kullanılmaktadır.

## Proje

**KAOS Technology — SmartLead AI**
