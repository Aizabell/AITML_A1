# AITML_A1

# Car Price Prediction Simulator

## Overview

The **Car Price Prediction Simulator** is a Flask-based web application designed to predict the selling price of a car based on user-provided parameters. It leverages a machine learning model trained on car price data, offering users an intuitive interface to interact with the model.

---

## Features

1. **User-Friendly Web Interface**:

   - Input form for car parameters.
   - Displays predicted car prices dynamically.
   - Clear history functionality for easy management.

2. **Key Capabilities**:

   - Handles missing values by applying imputation techniques.
   - Allows users to make predictions based on essential car details.

3. **Technology Stack**:

   - Backend: Python, Flask.
   - Frontend: HTML, CSS.
   - Machine Learning: Scikit-learn-based regression model.

4. **Dockerized Deployment**:
   - Fully containerized using Docker for easy deployment.
   - Ready-to-use `docker-compose` for launching the application.

---

## How to Use

### Running Locally

1. **Clone the Repository**:

```bash
   git clone <repository-url>
   cd <repository-directory>
```

2. **Set up a Virtual Environment**:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run the Application**:

```bash
Copy
Edit
python app.py
```

The application will be accessible at http://127.0.0.1:5001.
