# src/train_model.py
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from preprocessing import load_and_preprocess_data
from utils import save_model

def train_random_forest():
    X_train, X_test, y_train, y_test, _ = load_and_preprocess_data()

    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions and evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy}")

    # Save the trained model
    save_model(model, '../models/random_forest.pkl')

if __name__ == "__main__":
    train_random_forest()
