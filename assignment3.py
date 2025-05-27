'''Build a student grade management system using the following Python concepts:
- List of dictionaries
- Function with required arguments, *args, **kwargs
- Function decorator
- Loops and control statements

Requirements
1. Use a **decorator** to log function activity.
2. Use a function to **add student data** using *args and **kwargs.
3. Store student records in a **list of dictionaries**.
4. Use **loops and conditionals** to calculate and display results.'''





# 1. Decorator to log activity
def log_activity(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is running...")
        return func(*args, **kwargs)
    return wrapper

# 2. List to store all students
students = []

# 3. Function to add student data
@log_activity
def add_student(name, *args, **kwargs):
    student = {"name": name}
    subjects = list(kwargs.keys())
    for subject in subjects:
        student[subject] = kwargs[subject]
    students.append(student)

# 4. Function to show all student data with average
@log_activity
def show_students():
    for student in students:
        print(f"\nStudent: {student['name']}")
        total = 0
        count = 0
        for key in student:
            if key != "name":
                print(f"{key}: {student[key]}")
                total += student[key]
                count += 1
        if count > 0:
            average = total / count
            print(f"Average Marks: {round(average, 2)}")
            if average >= 50:
                print("Result: Passed")
            else:
                print("Result: Failed")
        else:
            print("No subjects added.")

# 5. Adding student data
add_student("Alice", Math=85, English=78, Science=92)
add_student("Bob", Math=45, English=50, Science=40)
add_student("Clara", Math=95, English=88, Science=91)

# 6. Showing results
show_students()
