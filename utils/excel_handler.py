import pandas as pd
import os
from models.feedback_model import get_today_feedback
from datetime import datetime, timedelta
import json

BACKUP_DIR = "database/local_backup"
RESET_FILE = "database/reset_tracker.json"

os.makedirs(BACKUP_DIR, exist_ok=True)

def save_daily_excel(feedbacks, date_str):
    """Save given feedbacks to an Excel file for the specified date."""
    if feedbacks:
        df = pd.DataFrame(feedbacks)
        file_path = os.path.join(BACKUP_DIR, f"{date_str}.xlsx")
        df.to_excel(file_path, index=False)
        print(f"[INFO] Saved Excel for {date_str} at {file_path}")
    else:
        print(f"[INFO] No feedback to save for {date_str}")

def check_and_reset():
    """Check if the day has changed, save previous day Excel, and update tracker."""
    today = datetime.now().strftime("%Y-%m-%d")

    # Load last date safely
    last_date = None
    if os.path.exists(RESET_FILE):
        try:
            with open(RESET_FILE, "r") as f:
                data = f.read().strip()
                if data:
                    last_date = json.loads(data).get("last_date")
        except (json.JSONDecodeError, FileNotFoundError):
            last_date = None

    # If last_date is None, initialize it with today
    if not last_date:
        last_date = today
        with open(RESET_FILE, "w") as f:
            json.dump({"last_date": last_date}, f)
        return

    # If day changed, save previous day's Excel
    if last_date != today:
        print(f"[INFO] Day changed from {last_date} to {today}, saving Excel...")
        # Temporarily set system date to last_date for backup
        feedbacks = get_today_feedback(date_filter=last_date)
        save_daily_excel(feedbacks, last_date)

        # Update tracker
        with open(RESET_FILE, "w") as f:
            json.dump({"last_date": today}, f)
        print(f"[INFO] Reset tracker updated to {today}")
