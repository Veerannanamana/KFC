from utils.db_connection import feedback_collection
from datetime import date

def save_feedback(roll_no, meal, rating):
    """Save a feedback document to MongoDB with today's date."""
    feedback_collection.insert_one({
        "roll_no": roll_no,
        "meal": meal,
        "rating": rating,
        "date": str(date.today())
    })
    return True

def get_today_feedback(date_filter=None):
    """Fetch all feedback documents for a given date (default: today)."""
    today = date_filter if date_filter else str(date.today())
    feedbacks = list(feedback_collection.find({"date": today}))
    return feedbacks
