from flask import Flask, request,render_template
import joblib
import pandas as pd

app=Flask(__name__)
model=joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method=='POST':
        data={
            "City": request.form.get("City"),
            "Room Type": request.form.get("Room Type"),
            "Bedrooms": float(request.form.get("Bedrooms")),
            "Bathrooms": float(request.form.get("Bathrooms")),
            "GuestsCapacity": int(request.form.get("GuestsCapacity")),
            "HasWifi": int(request.form.get("HasWifi")),
            "HasAC": int(request.form.get("HasAC")),
            "DistanceFromCityCenter": float(request.form.get("DistanceFromCityCenter")),
            "PricePerNight": float(request.form.get("PricePerNight"))
        }
        df=pd.DataFrame([data])
        prediction=model.predict(df)[0]
        return render_template('index.html', prediction_text=f'Predicted Price Per Night: ${round(prediction, 2)}')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
