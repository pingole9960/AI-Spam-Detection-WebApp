# AI Spam Detection Web App

An **AI-powered Spam Detection Web Application** that classifies messages as **Spam 🚨 or Not Spam ✅** using Machine Learning and Natural Language Processing (NLP).

The application is built using **Python, Scikit-learn, and Streamlit**, and uses a trained ML model to analyze text messages in real time.

---

## 🚀 Live Demo

Deployed Web App
[(Add your deployment link here)
](https://ai-spam-detection-webapp-pwxtuqllpuy5bqyfmbsywq.streamlit.app/)
---

## 📌 Project Highlights

* AI-powered spam message classification
* Natural Language Processing (NLP) based text analysis
* Real-world SMS spam dataset
* Interactive web interface
* Real-time prediction
* Lightweight ML model for fast inference
* Deployment-ready AI application

---

## 🧠 Machine Learning Pipeline

1. **Data Collection**
   SMS Spam Collection dataset containing labeled messages.

2. **Data Preprocessing**

   * Removing unnecessary columns
   * Label encoding (Spam / Ham)
   * Text cleaning

3. **Feature Engineering**

   * Text converted into numerical features using **TF-IDF Vectorization**

4. **Model Training**

   * Algorithm used: **Multinomial Naive Bayes**
   * Train/Test split for evaluation

5. **Model Evaluation**

   * Accuracy Score used for performance evaluation

6. **Model Deployment**

   * Model saved using **Joblib**
   * Web interface built with Streamlit

---

## 📊 Model Performance

| Metric   | Score |
| -------- | ----- |
| Accuracy | ~96%  |

The model performs efficiently on unseen messages and provides instant predictions.

---

## 🛠️ Tech Stack

**Programming Language**

* Python

**Libraries**

* pandas
* numpy
* scikit-learn
* joblib

**Framework**

* Streamlit

**Machine Learning**

* TF-IDF Vectorizer
* Multinomial Naive Bayes

---

## 📂 Project Structure

```id="81u27m"
AI-Spam-Detection-WebApp
│
├── app.py                # Streamlit Web Application
├── train_model.py        # Model training script
├── spam_classifier.py    # Console-based prediction
├── spam.csv              # Dataset
├── spam_model.pkl        # Trained ML model
├── vectorizer.pkl        # TF-IDF vectorizer
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## ▶️ Run Locally

Install dependencies

```id="pt6re4"
pip install -r requirements.txt
```

Run the Streamlit app

```id="6uqawp"
streamlit run app.py
```

Open browser

```id="d6m4pt"
http://localhost:8501
```

---

## 💡 Example Prediction

Input Message:

```id="64gqq9"
Congratulations! You have won a free prize.
```

Prediction:

```id="z7k4ju"
Spam 🚨
```

Input Message:

```id="tfrhpu"
Hello, are we meeting tomorrow?
```

Prediction:

```id="k9n3z7"
Not Spam ✅
```

---

## 🎯 Use Cases

* Email spam filtering
* SMS spam detection
* Cybersecurity applications
* NLP text classification systems

---

## 📈 Future Improvements

* Deep Learning based model
* Probability score for predictions
* Upload multiple messages (CSV input)
* Dashboard analytics
* API integration

---

## 👩‍💻 Author

Dipali Ingole

Aspiring **AI Engineer | Machine Learning Enthusiast**

---

## ⭐ Support

If you like this project, consider **starring the repository**.
