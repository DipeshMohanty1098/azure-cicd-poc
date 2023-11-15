from flask import Flask, jsonify
from pymongo import MongoClient
import os
import sys
 
app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))
 
# MongoDB connection string
# Replace the connection string with your actual MongoDB URI
mongo_uri = "mongodb+srv://ramvilla997:Qwerty123@cluster0.b8wxule.mongodb.net/shoebot_db?retryWrites=true&w=majority"
 
# Create a MongoDB client
client = MongoClient(mongo_uri)
 
# Connect to the MongoDB database
def connect_to_db():
    try:
        client.server_info()  # Check if the client is connected
        print('Connected to MongoDB')
    except Exception as e:
        print('Error connecting to MongoDB:', str(e))
        sys.exit(1)  # Exit the application in case of an error
 
connect_to_db()
 
@app.route('/api/records', methods=['GET'])
def get_records():
    try:
        db = client.get_database('shoebot_db')  # Replace with your actual database name
        collection = db.get_collection('products')  # Replace with your actual collection name
 
        # Fetch records from the collection
        records = list(collection.find({}))
 
        # Convert ObjectId to string in each document
        for record in records:
            record['_id'] = str(record['_id'])
 
        return jsonify(records), 200
    except Exception as e:
        print('Error fetching records:', str(e))
        return jsonify({'error': 'An error occurred while fetching records', 'details': str(e)}), 500
   
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)