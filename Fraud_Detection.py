import geopy.distance

def detect_location_anomaly(transaction_location, user_habitual_location, threshold=50):
    """
    Detects anomalies in transaction location based on user habitual location.

    Parameters:
    - transaction_location: Tuple (latitude, longitude) of the current transaction.
    - user_habitual_location: Tuple (latitude, longitude) of the user's usual location.
    - threshold: Distance threshold in kilometers to flag anomalies.

    Returns:
    - Boolean: True if the transaction is anomalous, False otherwise.
    """
    distance = geopy.distance.geodesic(transaction_location, user_habitual_location).km
    return distance > threshold

# Example Usage
transaction_location = (28.6139, 77.2090)  # Example: New Delhi
user_habitual_location = (19.0760, 72.8777)  # Example: Mumbai
is_anomalous = detect_location_anomaly(transaction_location, user_habitual_location)

if is_anomalous:
    print("Alert: Suspicious transaction detected based on location anomaly!")
else:
    print("Transaction location is within normal range.")
