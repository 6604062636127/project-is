import pandas as pd
from xgboost import XGBRegressor
import pickle

# ฟังก์ชันสำหรับโหลดโมเดล
def load_model(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# ฟังก์ชันสำหรับทำนายราคา
def predict_price(area, bedrooms, bathrooms, parking):
    model = load_model('model.pkl')
    input_data = pd.DataFrame([[area, bedrooms, bathrooms, parking]], columns=['Area', 'Bedrooms', 'Bathrooms', 'Parking'])
    prediction = model.predict(input_data)
    return prediction[0]

# ตัวอย่างการใช้งาน
predicted_price = predict_price(2000, 3, 2, 1)
print(f'The estimated price of the house is: ${predicted_price:,.2f}')
