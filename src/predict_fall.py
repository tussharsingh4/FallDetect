# src/predict_fall.py
import time
from utils import load_model
from data_collection import read_mpu6050

def predict_fall(model):
    while True:
        sensor_data = read_mpu6050()
        prediction = model.predict([sensor_data])
        if prediction[0] == 1:
            print("Fall detected!")
        else:
            print("No fall.")
        time.sleep(0.1)

if __name__ == "__main__":
    model = load_model('../models/random_forest.pkl')
    predict_fall(model)
