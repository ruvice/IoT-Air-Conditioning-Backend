# CZ4171_BLE_Backend
Python + Flask backend for BLE indoor positioning


Files in test folder are used for debugging, you may ignore them.

The server is run from main.py. Classifier is implemented in knn_classifier.py. 2 databases are used. statusdatabase.db holds the current status of the aircon and rssidatabase.db holds the latest rssi values from training. rssivalues.csv is a temporary file that holds the values from rssidatabase.db during retraining of the knn_classifier.

Please note that RSSI values may vary from device to device. Using a different android device would most likely require you to retrain the classifier with RSSI values specific to the device that you are using.