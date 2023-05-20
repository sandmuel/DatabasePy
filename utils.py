import os
import pickle
from time import sleep

db = {}

# Save a dictionary into a pickle file.
def save_dict(dict, file_path):
    temp_file_path = file_path + ".tmp"
    with open(temp_file_path, 'wb') as file:
        pickle.dump(dict, file)
    os.replace(temp_file_path, file_path)

# Load a dictionary from a pickle file.
def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# Load the dictionary (or create a new one if it doesn't exist)
try:
    db = load_dict("db.sav")
except FileNotFoundError:
    pass

# Save the dictionary every minute
while True:
    sleep(60)
    save_dict(db, "db.sav")
