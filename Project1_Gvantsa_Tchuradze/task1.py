# ----------- PART A: DATA DEFINITION -----------

# students dictionary with student ID as key and details as value
students = {
    "S001": {"name":"nino nebieridze","scores":[94, 96, 92, 95],"attendance":21},
    "S002": {"name":"anano aneli","scores":[78, 82, 80, 79],"attendance":26},
    "S003": {"name":"gela gelashvili","scores":[88, 90, 86, 92],"attendance":30},
    "S004": {"name":"niko nikoladze","scores":[59, 62, 58, 60],"attendance":22},
    "S005": {"name":"saba saralidze","scores":[70, 72, 68, 75],"attendance":24},
    "S006": {"name":"aleko abashidze","scores":[83, 85, 80, 81],"attendance":27},
    "S007": {"name":"john snow","scores":[91, 89, 87, 92],"attendance":29},
    "S008": {"name":"lasha leshkasheli","scores":[45, 50, 48, 52],"attendance":20},
    "S009": {"name":"peter steel","scores":[65, 60, 62, 58],"attendance":25},
    "S010": {"name":"emanuel makroni","scores":[55, 58, 54, 60],"attendance":18},
}

# ----------- PART B: FUNCTIONALITY -----------

# Returns the average of a list of scores, rounded to 2 decimals
def calculate_average(scores: list) -> float:
    return round(sum(scores) / len(scores), 2)

# Returns letter grade based on average:
def assign_grade(average: float) -> str:
    if average >= 90: return "A"
    if average >= 80: return "B"
    if average >= 70: return "C"
    if average >= 60: return "D"
    return "F"


# pass/fail status based on average score and attendance
def check_eligibility(student_dict: dict, total_classes: int) -> tuple:
    average = calculate_average(student_dict["scores"])
    attendance_percentage = (student_dict["attendance"] / total_classes) * 100

    if average >= 60 and attendance_percentage >= 75:
        return (True, "Passed")
    elif average < 60 and attendance_percentage < 75:
        return (False, "Failed due to low average and attendance")
    elif average < 60:
        return (False, "Failed due to low average")
    else:
        return (False, "Failed due to low attendance")


# Returns list of top n student IDs by average score]
def find_top_performers(students: dict, n: int) -> list:
    averages = []
    for student_id, details in students.items():
        avg_score = calculate_average(details["scores"])
        averages.append((student_id, avg_score))
    averages.sort(key=lambda x: x[1], reverse=True)
    return averages[:n]


# Returns dictionary with course statistics
def generate_report(students: dict) -> dict:
    total_students = len(students)
    passed_count = 0
    failed_count = 0
    avg_scores = []
    total_attendance = 0

    for details in students.values():
        avg_score = calculate_average(details["scores"])
        avg_scores.append(avg_score)
        total_attendance += details["attendance"]

        eligibility, _ = check_eligibility(details, 30)
        if eligibility:
            passed_count += 1
        else:
            failed_count += 1

    highest_score = max(avg_scores)
    lowest_score = min(avg_scores)
    class_average = round(sum(avg_scores) / total_students, 2)
    average_attendance_rate = round((total_attendance / (total_students * 30)) * 100, 2)

    return {
        "total_students": total_students,
        "passed_count": passed_count,
        "failed_count": failed_count,
        "class_average": class_average,
        "highest_score": highest_score,
        "lowest_score": lowest_score,
        "average_attendance_rate": average_attendance_rate
    }


# ----------- PART C: ANALYSIS & OUTPUT -----------

print("\n=== COURSE STATISTICS ===")
generated_report = generate_report(students)
for key, value in generated_report.items():
    print(f"{key}: {value}")


print("\n=== TOP 5 PERFORMERS ===")
for student in find_top_performers(students, 5):
    print(student[0] + " - " + students[student[0]]["name"] + ": "
          + str(student[1]) + " (" + assign_grade(student[1]) + ")")


print("=== STUDENTS WHO FAILED ===")
for id, student in students.items():
    value = check_eligibility(student, 30)
    if not value[0]:
        print(f"{id} - {value[1]} " + " (" + str(calculate_average(student["scores"])) + ")")

print("\n=== GRADE DISTRIBUTION ===")
dictionary = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
for student in students.values():
    dictionary[assign_grade(calculate_average(student["scores"]))] += 1

for key, value in dictionary.items():
    print(f"{key}: " + str(value) + " students")