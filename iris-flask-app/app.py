from flask import Flask, request, render_template
import joblib
import numpy as np

# Load the saved model
model = joblib.load('knn_model.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        
        # Prepare input for model
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        
        # Prediction
        prediction = model.predict(features)[0]  # already returns "Iris-setosa" etc.
        
        # If you want to clean the name (remove 'Iris-')
        result = prediction.replace("Iris-", "")
        
        return render_template('index.html', prediction_text=f"The predicted species is: {result}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
