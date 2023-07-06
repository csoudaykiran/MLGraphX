import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Step 1: Data Preprocessing
# Assuming you have already loaded and cleaned the dataset
dataset = pd.read_csv('AQI and Lat Long of Countries.csv')

# Step 2: Feature Selection/Engineering
# Selecting relevant features
selected_features = ['lat', 'lng', 'PM2.5 AQI Value', 'Ozone AQI Value', 'CO AQI Value']
X = dataset[selected_features]
y = dataset['AQI Value']

# Step 3: Splitting the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Model Training and Evaluation
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)


# Predicting AQI Value for new data
new_data = pd.DataFrame({
    'lat': [44.7444],
    'lng': [44.2031],
    'PM2.5 AQI Value': [51],
    'Ozone AQI Value': [36],
    'CO AQI Value': [1]
})

predicted_aqi_value = model.predict(new_data)
predicted_category = ""

# Define AQI category thresholds
good_threshold = 50
moderate_threshold = 100

# Categorize the predicted AQI value
if predicted_aqi_value <= good_threshold:
    predicted_category = "Good"
elif predicted_aqi_value <= moderate_threshold:
    predicted_category = "Moderate"
else:
    predicted_category = "Bad"

print('Predicted AQI Value:', predicted_aqi_value)
print('Predicted AQI Category:', predicted_category)


