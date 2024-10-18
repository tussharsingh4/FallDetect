# src/preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data():
    # Load the sensor data from the CSV file
    data_path = '../data/sensor_data.csv'
    data = pd.read_csv(data_path)

    # Separate features (sensor readings) and labels
    X = data.iloc[:, 1:-1].values  # sensor readings
    y = data.iloc[:, -1].values    # labels (fall or not)

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test, scaler
