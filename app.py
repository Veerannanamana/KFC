from flask import Flask, Response, render_template, request, jsonify
import matplotlib.pyplot as plt
from io import BytesIO
from models.feedback_model import save_feedback
from utils.chart_data import calculate_chart_data
from utils.excel_handler import check_and_reset

app = Flask(__name__)

@app.route("/")
def index():
    check_and_reset()  # Daily reset check
    return render_template("index.html")

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json()
    save_feedback(data['roll_no'], data['meal'], data['rating'])
    return jsonify({"status": "success"})

@app.route("/get_chart_data")
def get_chart_data_json():
    check_and_reset()
    data = calculate_chart_data()
    return jsonify(data)

@app.route("/get_chart")
def get_chart_image():
    check_and_reset()
    data = calculate_chart_data()
    labels = list(data.keys())
    sizes = list(data.values())
    colors = ['green', 'yellow', 'red']

    # Moderate figure size and better resolution
    plt.figure(figsize=(3, 3), dpi=100)
    plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        textprops={'fontsize': 10, 'color': 'black'}
    )
    plt.title("Today's Meal Ratings", fontsize=12)
    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight', dpi=100)
    img.seek(0)
    plt.close()
    return Response(img.getvalue(), mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
