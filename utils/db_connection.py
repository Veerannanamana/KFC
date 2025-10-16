from pymongo import MongoClient

# Replace with your MongoDB Atlas credentials
MONGO_URI = "mongodb+srv://lakshmannamana:lakshmannamana@box1.tbri4rm.mongodb.net/?retryWrites=true&w=majority&appName=BOX1"

client = MongoClient(MONGO_URI)
db = client["kiet_food_feedback"]
feedback_collection = db["feedbacks"]

def get_feedback_collection():
    return feedback_collection
