# Iris Species Prediction Project 🌸

This project is a full-stack application designed to predict Iris species based on flower measurements. It uses a trained RandomForest model to provide real-time predictions through a FastAPI backend and a Streamlit front-end dashboard, where users can interact with the model and visualize predictions and analytics.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files and Directories](#files-and-directories)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Project Structure

- **Backend**: FastAPI server for handling prediction API requests, utilizing a trained RandomForest model.
- **Frontend**: Streamlit dashboard with interactive sliders for setting flower measurements and displaying real-time predictions and analytics.
- **Model**: `RandomForestClassifier` trained on the Iris dataset using Scikit-learn, saved as `irisTest.joblib`.

## Features

- **Predict Iris Species**: Enter measurements for sepal length, sepal width, petal length, and petal width to receive a prediction of the Iris species.
- **Visualization**: Interactive charts comparing user inputs to average values for each Iris species.
- **Custom Background and Styling**: Includes background and custom styling for a user-friendly experience.
- **Real-time Analytics**: Bar and line charts display input trends vs. species dimensions, providing instant feedback on how measurements compare.

---

## Installation

### Prerequisites

- **Python 3.8+**

### Install Dependencies

Install required packages with:
```bash
pip install -r requirements.txt
```

### Clone the Repository
```bash
git clone <repository-url>
cd iris-species-prediction
```
### Model Training and Saving
To train and save the RandomForest model:

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import joblib

data = load_iris()
X, y = data.data, data.target

model = RandomForestClassifier()
model.fit(X, y)
joblib.dump(model, 'irisTest.joblib')
This saves the model as irisTest.joblib in the project root.
```

### Running the Application
1. Start the Backend (FastAPI)
Start the FastAPI server to handle prediction requests:
```python
uvicorn backend:app --reload
```
The API will be available at http://localhost:8000.

2. Start the Frontend (Streamlit)
Run the Streamlit application to launch the prediction dashboard:

```puyhon
streamlit run frontend.py
```
The Streamlit dashboard will be available at http://localhost:8501.

### API Testing
Visit http://localhost:8000/docs to test the API endpoints using Swagger UI.

Example request payload for /predict/ endpoint:

```json
{"features": [5.1, 3.5, 1.4, 0.2]}
```
### Usage
Enter Flower Measurements: Adjust the sidebar sliders to set values for sepal length, sepal width, petal length, and petal width.
Get Prediction: Click "Predict Species" to see the Iris species prediction.
View Analytics: Explore charts comparing input measurements with average values for each Iris species.
Files and Directories
model_train.py: Script to train and save the RandomForest model.
backend.py: FastAPI server code for handling prediction requests.
frontend.py: Streamlit dashboard for user interactions and visualizations.
requirements.txt: List of dependencies.
irisTest.joblib: Saved model file.

---

## Screenshots

### Dashboard Home:

![Home Page](https://github.com/user-attachments/assets/3f0a8dd6-2a0a-450a-8e29-069a23647cc4)

### Prediction Result:

![Profile Page](https://github.com/user-attachments/assets/6b187543-ef1e-4d29-9d0f-3833a2e3e536)


### Analytics Comparison:

![Create Post](https://github.com/user-attachments/assets/68fda79c-d46a-4b85-9217-38715348b9d4)


---

### Contributing
Contributions are welcome! Please submit issues or pull requests for any enhancements or fixes.

---

