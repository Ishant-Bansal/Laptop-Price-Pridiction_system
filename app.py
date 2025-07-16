
from flask import Flask, render_template, request
import joblib
import os
from datetime import datetime

app = Flask(__name__)

# --- Load the trained model ---
model = None
try:
    model_path = 'model.joblib'
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        print(f"Model loaded successfully from {model_path}!")
    else:
        print(f"Error: Model file '{model_path}' not found. Please ensure it's in the same directory as app.py.")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")
    model = None

# --- Data Mappings ---
brand_dict = {'ASUS': 1, 'Lenovo': 2, 'acer': 3, 'Avita': 4, 'HP': 5, 'DELL': 6, 'MSI': 7, 'APPLE': 8}
processor_brand_dict = {'Intel' : 1, 'AMD':2, 'M1': 3}
processor_name_dict = {'Core i3' : 1, 'Core i5':2, 'Celeron Dual':3, 'Ryzen 5':4, 'Core i7':5,'Core i9':6, 'M1':7, 'Pentium Quad':8, 'Ryzen 3':9, 'Ryzen 7':10, 'Ryzen 9':11}
processor_gnrtn_dict = {'10th':5, 'Not Available':0, '11th':6, '7th':2, '8th':3, '9th':4, '4th':1,'12th':7}
ram_type_dict = {'DDR4':3, 'LPDDR4':4, 'LPDDR4X':5, 'DDR5':6, 'DDR3':1, 'LPDDR3':2}
os_dict = {'Windows':1, 'DOS':2, 'Mac':3}
os_bit_dict = {'64': 1, '32': 2}
touchscreen_dict = {'Yes': 1, 'No': 0}
msoffice_dict = {'Yes': 1, 'No': 0}
warranty_dict = {'1 Year': 1, '2 Year': 2, '3 Year': 3, 'No Warranty': 0}

search_history = []

def extract_number(val):
    if isinstance(val, str):
        val = val.strip().upper()
        if 'TB' in val:
            return float(val.replace('TB', '').replace(' ', '')) * 1024
        elif 'MB' in val:
            return float(val.replace('MB', '').replace(' ', '')) / 1024
        elif 'GB' in val:
            return float(val.replace('GB', '').replace(' ', ''))
        else:
            return float(val)
    return float(val)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/history')
def history():
    return render_template('history.html', history_entries=search_history)

@app.route('/project', methods=['GET', 'POST'])
def project():
    prediction_result = None
    form_values = {}
    if request.method == 'POST':
        if model is None:
            prediction_result = "Error: Machine learning model is not loaded. Cannot predict."
            return render_template('project.html', prediction=prediction_result, form_data=form_values, request=request)
        # Retrieve form data from the POST request
        brand = request.form['brand']
        processor_brand = request.form['processor_brand']
        processor_name = request.form['processor_name']
        processor_gnrtn = request.form['processor_gnrtn']
        ram_gb = request.form['ram_gb']
        ram_type = request.form['ram_type']
        ssd = request.form['ssd']
        hdd = request.form['hdd']
        os_ = request.form['os']
        os_bit = request.form['os_bit']
        graphic_card_gb = request.form['graphic_card_gb']
        Touchscreen = request.form['Touchscreen']
        msoffice = request.form['msoffice']
        warranty = request.form['warranty']
        form_values = {
            'brand': brand,
            'processor_brand': processor_brand,
            'processor_name': processor_name,
            'processor_gnrtn': processor_gnrtn,
            'ram_gb': ram_gb,
            'ram_type': ram_type,
            'ssd': ssd,
            'hdd': hdd,
            'os': os_,
            'os_bit': os_bit,
            'graphic_card_gb': graphic_card_gb,
            'Touchscreen': Touchscreen,
            'msoffice': msoffice,
            'warranty': warranty
        }
        brand_code = brand_dict.get(brand, 0)
        processor_brand_code = processor_brand_dict.get(processor_brand, 0)
        processor_name_code = processor_name_dict.get(processor_name, 0)
        processor_gnrtn_code = processor_gnrtn_dict.get(processor_gnrtn, 0)
        ram_type_code = ram_type_dict.get(ram_type, 0)
        os_code = os_dict.get(os_, 0)
        os_bit_code = os_bit_dict.get(os_bit.replace('-bit',''), 0) if os_bit else 0
        touchscreen_code = touchscreen_dict.get(Touchscreen, 0)
        msoffice_code = msoffice_dict.get(msoffice, 0)
        warranty_code = warranty_dict.get(warranty.title(), 0)
        try:
            ram_gb_num = extract_number(ram_gb)
            ssd_num = extract_number(ssd)
            hdd_num = extract_number(hdd)
            graphic_card_gb_num = extract_number(graphic_card_gb)
        except ValueError as e:
            prediction_result = f"Error in numerical input: {e}. Please ensure RAM, SSD, HDD, Graphics are valid numbers."
            return render_template('project.html', prediction=prediction_result, form_data=form_values, request=request)
        missing_feature = 0
        features_for_prediction = [
            brand_code, processor_brand_code, processor_name_code, processor_gnrtn_code,
            ram_gb_num, ram_type_code, ssd_num, hdd_num, os_code, os_bit_code,
            graphic_card_gb_num, touchscreen_code, msoffice_code, warranty_code,
            missing_feature
        ]
        try:
            prediction = model.predict([features_for_prediction])
            rounded_prediction = round(prediction[0], 2)
            prediction_result = f"Predicted Price: ₹{rounded_prediction:,.2f}"
        except Exception as e:
            prediction_result = f"Error during prediction: {e}. Please check model input."
        # Save to history
        search_history.append({
            'Brand': brand,
            'Processor Brand': processor_brand,
            'Processor Name': processor_name,
            'Processor Gen.': processor_gnrtn,
            'RAM (GB)': ram_gb,
            'RAM Type': ram_type,
            'SSD (GB)': ssd,
            'HDD (GB)': hdd,
            'OS': os_,
            'OS Bit': os_bit,
            'Graphics (GB)': graphic_card_gb,
            'Warranty': warranty,
            'Touchscreen': Touchscreen,
            'MS Office': msoffice,
            'Predicted Price (₹)': f"{rounded_prediction:,.2f}" if prediction_result and 'Predicted Price' in prediction_result else "N/A",
            'Search Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return render_template('project.html', prediction=prediction_result, form_data=form_values, request=request)

if __name__ == '__main__':
    app.run(debug=True)
