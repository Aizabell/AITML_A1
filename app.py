from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the pre-trained model and scaler
model = pickle.load(open('car_prediction.model', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Initialize an empty list to hold the prediction history
prediction_history = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        # Render the prediction page when accessed via GET
        return render_template("predict.html", prediction_history=prediction_history)

    # Handle POST requests (form submissions)
    action = request.form.get("action")  # Get the action from the form

    if action == "Clear":  # If the action is "Clear", reset the history
        prediction_history.clear()
        return render_template("predict.html", prediction_history=prediction_history)

    # If the action is "Predict", proceed with prediction
    year = request.form.get("year")
    max_power = request.form.get("max_power")
    engine = request.form.get("engine")
    owner = int(request.form.get("owner", 1))  # Default to "First"
    fuel = int(request.form.get("fuel", 0))  # Default to "Petrol"
    transmission = int(request.form.get("transmission", 0))  # Default to "Manual"

    # Handle missing numeric inputs by setting defaults
    year = int(year) if year else 2015  # Default to 2015
    max_power = float(max_power) if max_power else 80.0  # Default to 80 bhp
    engine = int(engine) if engine else 1500  # Default to 1500 CC

    # Prepare input for prediction
    input_data = np.array([[year, max_power, engine, owner, fuel, transmission]])

    # Scale input and predict
    scaled_input = scaler.transform(input_data)
    predicted_price_log = model.predict(scaled_input)
    predicted_price = np.exp(predicted_price_log[0])  # Reverse log transformation

    # Prepare parameters for display
    parameters = f"Year: {year}, Max Power: {max_power}, Engine: {engine}, Owner: {['First', 'Second', 'Third', 'Fourth & Above'][owner - 1]}, Fuel: {['Petrol', 'Diesel'][fuel]}, Transmission: {['Manual', 'Automatic'][transmission]}"

    # Append prediction and parameters to history
    prediction_history.append({"price": f"${predicted_price:,.2f}", "parameters": parameters})

    # Render the prediction page
    return render_template("predict.html", prediction_history=prediction_history)

