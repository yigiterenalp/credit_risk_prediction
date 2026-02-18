# 🏦 Kredi Risk Analizi ve Tahmin Sistemi (XGBoost)

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Machine Learning](https://img.shields.io/badge/ML-XGBoost-orange.svg)](https://xgboost.readthedocs.io/)

Bu proje, bankacılık sektöründe kredi başvurularının risk durumunu (default risk) tahmin etmek amacıyla geliştirilmiş uçtan uca bir makine öğrenmesi uygulamasıdır. Mezuniyet projem kapsamında, özellikle finans dünyası için kritik olan **Recall (Batığı Yakalama)** oranına odaklanılarak inşa edilmiştir.

---

## 📌 Proje Özeti ve İş Problemi

Bankalar için en büyük risk, geri ödenmeyen kredilerdir. Bu proje:
- Müşteri verilerini analiz ederek potansiyel riskleri önceden tespit eder.
- Veriye dayalı karar destek mekanizması ile kredi onay sürecini optimize eder.
- **XGBoost** algoritması ile yüksek doğruluklu sonuçlar sunar.

## 🛠️ Teknik Mimari ve Süreç

1. **Veri Ön İşleme:** Aykırı değerlerin temizlenmesi (Yaş, Gelir vb.) ve eksik verilerin median/mean ile doldurulması.
2. **Özellik Mühendisliği:** Gelir verisinin normal dağılımı için Log dönüşümü ve `Interest Burden` (Faiz Yükü) gibi yeni değişkenlerin üretilmesi.
3. **Model:** Sınıf dengesizliği (imbalance) dikkate alınarak optimize edilmiş **XGBoost Classifier**.
4. **Dağıtım:** Kullanıcı dostu ve modern bir **Flask** web arayüzü.

## 📊 Model Performansı

Modelin test verisi üzerindeki güncel başarı metrikleri:

| Metrik | Skor |
| :--- | :--- |
| **Accuracy (Doğruluk)** | **%91.9** |
| **Recall (Batığı Yakalama - Sınıf 1)** | **%78.0** |
| **Precision (Keskinlik - Sınıf 1)** | **%84.0** |
| **F1-Score** | **%81.0** |

> **Analiz:** Modelimiz, borcunu ödemeyecek 1361 riskli müşterinin **1061** tanesini başarıyla yakalamayı başarmıştır.

## 💻 Kurulum ve Çalıştırma

Proje **Conda** ortamı üzerinde stabil çalışmaktadır.

1. **Depoyu klonlayın:**
   ```bash
   git clone [https://github.com/yigiterenalp/credit_risk_prediction.git](https://github.com/yigiterenalp/credit_risk_prediction.git)
   cd credit_risk_prediction

   Conda ortamını hazırlayın:

Bash

conda create -n credit_risk_env python=3.10
conda activate credit_risk_env
Gerekli kütüphaneleri kurun:

Bash

pip install -r requirements.txt
Uygulamayı başlatın:

Bash

python app.py
Tarayıcıdan http://127.0.0.1:5000 adresine giderek sistemi test edebilirsiniz.
