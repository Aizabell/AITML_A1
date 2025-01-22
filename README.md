# Car Price Prediction Simulator

## Author

**Student Name**: Oak Soe Kyaw
**Student ID**: ST125064

## Overview

The **Car Price Prediction Simulator** is a Flask-based web application designed to predict the selling price of a car based on user-provided parameters. It leverages a machine learning model trained on car price data, offering users an intuitive interface to interact with the model.

---

## Features

1. **User-Friendly Web Interface**:

   - Pages: Landing Page, Prediction Page
   - Input form for car parameters.
   - Displays predicted car prices dynamically.
   - Clear history functionality for easy management.

2. **Key Capabilities**:

   - Handles missing values by applying imputation techniques.
   - Allows users to make predictions based on essential car details such as year,max power, engine, owner, fuel, and transmission.

3. **Technology Stack**:

   - Backend: Python, Flask.
   - Frontend: HTML, CSS.
   - Machine Learning: Scikit-learn-based regression model.
   - Algorithms: Random Forest Regressor.

4. **Dockerized Deployment**:
   - Fully containerized using Docker for easy deployment.
   - Ready-to-use `docker-compose` for launching the application.

---

## How to Use

### Running Locally

1. **Clone the Repository**:

```bash
   git clone <https://github.com/Aizabell/AITML_A1.git>
```

2. **Set up a Virtual Environment**:

For Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run the Application**:

```bash
python app.py
```

The application will be accessible at http://127.0.0.1:5001.

## Using Docker

1. **Build the Docker Image**:

```bash
Copy
Edit
docker build -t <docker-username>/car-price-predictor .
```

2. **Run the Application**:

```bash
docker run -p 5001:5000 <docker-username>/car-price-predictor
```

3. **Using Docker Compose**: Ensure the docker-compose.yml file is correctly set up, then run:

```bash
docker-compose up -d
# or
docker-compose up
```

## Access the Application

- Open your browser and navigate to:

```bash
http://localhost:5001
```

## Input Parameters

| Parameter        | Description                                       | Example        |
| ---------------- | ------------------------------------------------- | -------------- |
| **Year**         | Year the car was manufactured (Optional)          | `2015`         |
| **Max Power**    | Maximum power output of the car in bhp (Optional) | `80`           |
| **Engine**       | Engine capacity in CC (Optional)                  | `1500`         |
| **Owner**        | Ownership history                                 | First, Second  |
| **Fuel Type**    | Type of fuel the car uses                         | Petrol, Diesel |
| **Transmission** | Transmission type                                 | Manual, Auto   |

### Example Predictions

**Input:**

- Year: `2015`
- Max Power: `80 bhp`
- Engine: `1500 CC`
- Owner: `First`
- Fuel: `Petrol`
- Transmission: `Manual`

**Prediction**: `$12,500.00`

---

**Input:**

- Year: _(not provided)_
- Max Power: `100 bhp`
- Engine: `2000 CC`
- Owner: `Second`
- Fuel: `Diesel`
- Transmission: `Automatic`

**Prediction**: `$18,700.00`
