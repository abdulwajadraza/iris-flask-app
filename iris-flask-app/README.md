🌸 Iris Flower Prediction App (Flask + KNN Model)

This repository contains a simple Flask web application that predicts the species of an Iris flower based on four input features:

Sepal Length

Sepal Width

Petal Length

Petal Width

The prediction is powered by a K-Nearest Neighbors (KNN) model trained on the famous Iris dataset.

📌 Features

A clean and simple web interface built with Flask and HTML.

Users can input flower measurements and get predictions in real-time.

Uses a KNN model trained and saved with joblib.

Runs locally on your machine (http://127.0.0.1:5000/).

📂 Project Structure
iris-flask-app/
│
├── app.py                # Flask application
├── knn_model.pkl         # Saved trained KNN model
├── templates/
│   └── index.html        # Homepage (form for user input)
├── static/               # (Optional) CSS/JS/images for styling
├── requirements.txt      # Dependencies for the project
└── README.md             # Project documentation

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/iris-flask-app.git
cd iris-flask-app

2. Create and activate virtual environment (recommended)
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the Flask app
python app.py

5. Open in browser

Go to:
👉 http://127.0.0.1:5000

🧪 Example Input & Output

Input (from homepage):

Sepal Length: 5.1

Sepal Width: 3.5

Petal Length: 1.4

Petal Width: 0.2

Output (prediction):
👉 Predicted Species: Iris-setosa

📊 Model Information

Algorithm: K-Nearest Neighbors (KNN)

Dataset: Iris dataset (150 samples, 3 classes)

Training & Model Saving:

import joblib
joblib.dump(model, 'knn_model.pkl')

📦 Dependencies

Main libraries used:

Flask – Web framework

scikit-learn – For KNN model

joblib – Saving and loading the trained model

(See requirements.txt for full list)

🚀 Future Improvements

Deploy on Heroku / Render / AWS / Azure for public access

Add Bootstrap / Tailwind for better styling

Add option for multiple models (RandomForest, Logistic Regression, etc.)

📝 License

This project is open-source and available under the MIT License.

🙌 Acknowledgements

Iris Dataset – UCI Machine Learning Repository

scikit-learn & Flask community