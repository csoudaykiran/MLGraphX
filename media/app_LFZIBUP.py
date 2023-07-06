from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the saved model
model = joblib.load('aqi_model')

@app.route('/')
def home():
    return 'Hello, Flask!'


@app.route('/predict_aqi', methods=['POST'])
def predict_aqi():
    # Get the input data from the request
    data = request.get_json()

    # Extract the input features
    lat = data['latitude']
    lng = data['longitude']
    co_aqi = data['co_aqi']
    ozone_aqi = data['ozone_aqi']
    no2_aqi = data['no2_aqi']
    pm25_aqi = data['pm25_aqi']

    # Perform prediction using the loaded model
    prediction = model.predict([[lat, lng, co_aqi, ozone_aqi, no2_aqi, pm25_aqi]])

    # Prepare the response
    result = {
        'predicted_aqi': prediction[0]
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
