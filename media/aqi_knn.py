import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset
dataset = pd.read_csv('AQI and Lat Long of Countries.csv')

# Step 2: Feature Selection/Engineering
selected_features = ['lat', 'lng', 'CO AQI Value', 'Ozone AQI Value', 'NO2 AQI Value', 'PM2.5 AQI Value']
X = dataset[selected_features]
y = dataset['AQI Value']



# Step 3: Splitting the Data and Feature Scaling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Model Training and Evaluation
model = KNeighborsRegressor(n_neighbors=10)  # You can adjust the number of neighbors as needed
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Calculate the accuracy of the model
accuracy = model.score(X_test, y_test)
print('Model Accuracy:', accuracy)

# Step 5: Predicting AQI Value for new data
# Get inputs from the user
lat =float(input('Enter latitude: '))
lng =float(input('Enter longitude: '))

#new data
new_data = pd.DataFrame({
    'lat': [lat],
    'lng': [lng],
    'CO AQI Value': [0],  # Placeholder value for CO AQI
    'Ozone AQI Value': [0],  # Placeholder value for Ozone AQI
    'NO2 AQI Value': [0],  # Placeholder value for NO2 AQI
    'PM2.5 AQI Value': [0]  # Placeholder value for PM2.5 AQI
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

