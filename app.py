from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Dosyaları yükle
try:
    model = joblib.load('xgb_model.joblib')
    scaler = joblib.load('scaler.joblib')
    model_cols = joblib.load('model_columns.joblib')
except Exception as e:
    print(f"KRİTİK HATA: Model dosyaları yüklenemedi! {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Gelen veriyi terminale yazdır (Hata ayıklama için en önemli kısım)
    print("--- Gelen Form Verileri ---")
    print(request.form)
    
    try:
        f = request.form
        
        # Bu satırlardan hangisinde hata olduğunu terminalde göreceğiz
        income = float(f.get('income', 0))
        amount = float(f.get('amount', 0))
        rate = float(f.get('rate', 0))
        age = int(f.get('age', 0))
        emp_len = float(f.get('emp_length', 0))
        home_stat = f.get('home', 'RENT')
        
        # Feature Engineering
        data = {
            'person_age': [age],
            'person_income_log': [np.log1p(income)],
            'person_emp_length': [emp_len],
            'loan_amnt': [amount],
            'loan_int_rate': [rate],
            'loan_percent_income': [amount / income if income > 0 else 0],
            'cb_person_cred_hist_length': [5],
            'loan_grade_num': [1],
            'cb_person_default_on_file': [0],
            'interest_burden': [(amount * rate) / 100]
        }
        
        input_df = pd.DataFrame(0, index=[0], columns=model_cols)
        for k, v in data.items():
            if k in input_df.columns:
                input_df[k] = v
        
        h_col = f"person_home_ownership_{home_stat}"
        if h_col in input_df.columns:
            input_df[h_col] = 1

        scaled = scaler.transform(input_df)
        prob = model.predict_proba(scaled)[0][1]
        
        res = "Onaylandı" if prob < 0.35 else "Reddedildi"
        clr = "success" if prob < 0.35 else "danger"
        
        return render_template('index.html', result=res, probability=round(prob*100, 1), color=clr)
    
    except Exception as e:
        print(f"HATA DETAYI: {e}")
        return f"Sistem hatası: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)