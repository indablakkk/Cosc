from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Custom filter for formatting datetime in Jinja2
@app.template_filter('strftime')
def datetime_format(value, format='%H:%M'):
    if isinstance(value, datetime):
        return value.strftime(format)
    return value

# Function to get schedule (with added professor and student info)
def get_schedule():
    # Only one student's schedule is returned
    schedule = [
        [1, 'ANSO 2060', 'Room 101', 'Mon', '09:00', '11:20', datetime(2024, 12, 12, 9, 0), datetime(2024, 12, 12, 10, 0), 'Dr. Smith'],
        [2, 'COSC 2610', 'Room 102', 'Tue', '11:30', '13:50', datetime(2024, 12, 12, 10, 0), datetime(2024, 12, 12, 11, 0), 'Dr. Johnson'],
        [3, 'COSC 2810', 'Room 103', 'Wed', '14:00', '16:20', datetime(2024, 12, 12, 11, 0), datetime(2024, 12, 12, 12, 0), 'Dr. Taylor'],
        [4, 'HLSC 1690', 'Room 104', 'Thu', '16:30', '19:20', datetime(2024, 12, 12, 12, 0), datetime(2024, 12, 12, 13, 0), 'Dr. Davis'],
        [5, 'PHIL 2110', 'Room 105', 'Fri', '19:00', '21:20', datetime(2024, 12, 12, 13, 0), datetime(2024, 12, 12, 14, 0), 'Dr. Miller'],
    ]
    return schedule

@app.route("/", methods=["GET", "POST"])
def timetable():
    # Get the schedule for the student
    schedule = get_schedule()

    # Get current time
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Student info
    student_name = "Alisher Karimov"
    student_id = "4224640"

    return render_template("timetable.html", schedule=schedule, current_time=date_time, student_name=student_name, student_id=student_id)

if __name__ == '__main__':
    app.run(debug=True)
