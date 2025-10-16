from models.feedback_model import get_today_feedback

def calculate_chart_data():
    feedbacks = get_today_feedback()
    meals = ["Breakfast","Lunch","Snacks","Dinner"]
    ratings = ["Good","Average","Bad"]

    result = {meal:{r:0 for r in ratings} for meal in meals}

    for f in feedbacks:
        meal = f["meal"]
        rating = f["rating"]
        if meal in result and rating in result[meal]:
            result[meal][rating] += 1

    # Convert to percentages
    for meal in meals:
        total = sum(result[meal].values())
        if total > 0:
            for r in ratings:
                result[meal][r] = round(result[meal][r]/total*100,2)
    return result

