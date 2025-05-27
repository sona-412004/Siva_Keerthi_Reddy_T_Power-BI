university_data = {
"S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#1 Print all student names and their majors
for student in university_data.keys():
    print(university_data[student]["name"]+ " major is "+ university_data[student]["major"])
    
#2 Average score per course per student 
for student_id, student_info in university_data.items():
    print(f"{student_info['name']} average marks are as follows:")
    for course, scores in student_info["courses"].items():
        avg = round(sum(scores.values()) / len(scores), 2)
        print(f"       {course} average is {avg}")

#3  Find students who scored >90 in final of Python101 
for student_id,student_info in university_data.items():
    if "Python101" in student_info["courses"].keys():
        if student_info["courses"]["Python101"]["final"]>90:
            print(f"{student_info['name']} has scored more than 90 in python final")

#4 Add new course AI101 for student S101
university_data["S101"]["courses"]["AI101"] = {"midterm": 85, "final": 90, "project": 88}
print(university_data["S101"]["courses"]["AI101"])

#5 Print average for each course
course_scores = {}
for student in university_data.values():
    for course, scores in student["courses"].items():
        if course not in course_scores:
            course_scores[course] = []
        course_scores[course].extend(scores.values())

print("Average marks for each course:")
for course, scores in course_scores.items():
    avg = round(sum(scores) / len(scores), 2)
    print(f"{course}: {avg}")
