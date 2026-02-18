\# 🏦 Credit Risk Analysis \& Prediction System (XGBoost)



\[!\[Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)

\[!\[Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)

\[!\[Machine Learning](https://img.shields.io/badge/ML-XGBoost-orange.svg)](https://xgboost.readthedocs.io/)



Bu proje, bankacılık sektöründe kredi başvurularının risk durumunu (default risk) tahmin etmek amacıyla geliştirilmiş uçtan uca bir makine öğrenmesi uygulamasıdır. Mezuniyet projesi kapsamında, yüksek doğruluk ve özellikle finans dünyası için kritik olan \*\*Recall (duyarlılık)\*\* oranına odaklanılarak inşa edilmiştir.



---



\## 📌 Proje Özeti ve İş Problemi



Bankalar için en büyük maliyet kalemi, geri ödenmeyen kredilerdir (Bad Loans). Bu projenin amacı:

\- Mevcut müşteri verilerini analiz ederek potansiyel riskleri önceden tespit etmek.

\- Manuel değerlendirme sürecini hızlandırmak.

\- Veriye dayalı karar destek mekanizması oluşturmak.







\## 🛠️ Teknik Mimari ve Süreç



Proje, veri temizliğinden dağıtıma kadar şu aşamalardan oluşmaktadır:



1\. \*\*Veri Ön İşleme (Data Preprocessing):\*\* - Aykırı değerlerin (Outliers) temizlenmesi (Yaş > 100, Gelir > 300k vb.).

&nbsp;  - Eksik verilerin (NaN) istatistiksel yöntemlerle (median/mean) doldurulması.

&nbsp;  - Mantıksal hataların ayıklanması.

2\. \*\*Özellik Mühendisliği (Feature Engineering):\*\*

&nbsp;  - Gelir verisine Logaritmik dönüşüm uygulanarak normal dağılıma yaklaştırılması.

&nbsp;  - `Interest Burden` (Faiz Yükü) gibi yeni finansal metriklerin üretilmesi.

&nbsp;  - One-Hot Encoding ile kategorik verilerin sayısal formata çevrilmesi.

3\. \*\*Model Eğitimi:\*\* - Sektör standardı olan \*\*XGBoost Classifier\*\* kullanılmıştır.

&nbsp;  - Veri setindeki sınıf dengesizliği (imbalance) `scale\_pos\_weight` parametresi ile optimize edilmiştir.

4\. \*\*Dağıtım (Deployment):\*\* - Model, kullanıcı dostu bir \*\*Flask\*\* web arayüzü ile sunulmaktadır.







\## 📊 Model Performansı



Modelin test verisi üzerindeki başarı metrikleri şöyledir:



| Metrik | Skor |

| :--- | :--- |

| \*\*Accuracy (Doğruluk)\*\* | %92 |

| \*\*Recall (Batığı Yakalama)\*\* | \*\*%78\*\* |

| \*\*Precision (Keskinlik)\*\* | %84 |

| \*\*F1-Score\*\* | %81 |



> \*\*Not:\*\* Finansal risk yönetiminde, borcunu ödemeyecek müşteriyi kaçırmamak (Recall) kritik öneme sahiptir. Modelimiz riskli müşterilerin büyük bir çoğunluğunu başarıyla tespit etmektedir.







\## 💻 Kurulum ve Çalıştırma



Proje \*\*Conda\*\* ortamı üzerinde stabil çalışmaktadır.



1\. \*\*Depoyu klonlayın:\*\*

&nbsp;  ```bash

&nbsp;  git clone \[https://github.com/kullanici\_adin/credit\_risk\_prediction.git](https://github.com/kullanici\_adin/credit\_risk\_prediction.git)

&nbsp;  cd credit\_risk\_prediction



Conda ortamını hazırlayın:



Bash



conda create -n credit\_risk\_final python=3.10

conda activate credit\_risk\_final

Gerekli kütüphaneleri kurun:



Bash



pip install -r requirements.txt

Uygulamayı başlatın:



Bash



python app.py

Tarayıcınızdan http://127.0.0.1:5000 adresine giderek uygulamayı kullanmaya başlayabilirsiniz.



📁 Dosya Yapısı

app.py: Flask sunucusu ve tahmin motoru.



xgb\_model.joblib: Eğitilmiş XGBoost model dosyası.



scaler.joblib: Veri ölçeklendirme için kullanılan scaler.



templates/: Web arayüzü (HTML) dosyaları.



requirements.txt: Kütüphane bağımlılıkları.

