# 💻 LaptiQ – Laptop Price Prediction System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-green.svg)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()

**LaptiQ** is a futuristic, responsive web application that predicts the price of laptops based on user-provided specifications. Built with a glowing neon-themed UI, it combines a trained ML model with a fully modular Flask backend.

---

## ✨ Features

- 🧠 Predicts laptop prices using features like:
  - Brand
  - Processor type
  - RAM and Storage
  - GPU
  - Operating System
  - Display size & resolution
- 🖥️ Futuristic neon-glassmorphism UI
- 📊 Real-time prediction output on-screen
- 📁 Fully modular frontend with HTML, CSS, JavaScript
- 💡 Includes model training Jupyter notebook and CSV dataset

---

## 📁 Project Structure

```bash
laptop/
│
├── app.py                    # Flask application script
├── model.pkl                 # Trained ML model
├── Laptop_data.csv           # Main dataset used for training
├── model_train.ipynb         # Jupyter notebook for training
│
├── requirements.txt          # All Python dependencies
├── README.md                 # This file
│
├── static/
│   ├── style.css             # Main CSS styling
│   └── images/               # All laptop or theme-related images
│
└── templates/
    ├── index.html            # Home page
    ├── contact.html          # Contact form
    ├── about.html            # About project
    └── project.html          # Prediction form page
```

---

## 🚀 Getting Started

1. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask application**
   ```bash
   python app.py
   ```

3. **Open in browser**
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the app.

---

## 📌 Notes

- All UI templates reside inside the `templates/` folder.
- Static resources (CSS, JS, images) go in the `static/` directory.
- Use this for adding images in HTML:
  ```html
  <img src="{{ url_for('static', filename='images/yourimage.png') }}" alt="Laptop Image">
  ```

---

## 📷 Demo (Optional)

<img width="1920" height="3523" alt="image" src="https://github.com/user-attachments/assets/09c65551-e7d9-4127-bcea-16800e385709" />

---

## 👨‍💻 Developed By

**Ishant Bansal**  
🎓 BCA Student, Lords University, Alwar  
🔗 [GitHub](https://github.com/Ishant-Bansal) | [LinkedIn](https://www.linkedin.com/in/ishant-bansal)

---

## 📄 License

Licensed under the [MIT License](LICENSE). Feel free to use, modify, and share with attribution.
