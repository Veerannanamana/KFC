from utils.db_connection import get_feedback_collection
from datetime import datetime

collection = get_feedback_collection()

def save_feedback(roll_no, meal, rating):
    today = datetime.now().strftime("%Y-%m-%d")
    doc = {
        "roll_no": roll_no,
        "meal": meal,
        "rating": rating,
        "date": today
    }
    collection.insert_one(doc)
    return True

def get_today_feedback():
    today = datetime.now().strftime("%Y-%m-%d")
    docs = list(collection.find({"date": today}, {"_id":0}))
    return docs
