import geopy.distance

def detect_location_anomaly(transaction_location, user_habitual_location, threshold=50):
    
    distance = geopy.distance.geodesic(transaction_location, user_habitual_location).km
    return distance > threshold

transaction_location = (28.6139, 77.2090)  # Example: New Delhi
user_habitual_location = (19.0760, 72.8777)  # Example: Mumbai
is_anomalous = detect_location_anomaly(transaction_location, user_habitual_location)

if is_anomalous:
    print("Alert: Suspicious transaction detected based on location anomaly!")
else:
    print("Transaction location is within normal range.")
