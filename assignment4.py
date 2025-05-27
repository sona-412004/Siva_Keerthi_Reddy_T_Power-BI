class Department:
    total_departments = 0

    def __init__(self, dept_id, name, location, dept_head):
        self.dept_id = dept_id
        self.name = name
        self.location = location
        self.dept_head = dept_head
        Department.total_departments += 1

    def display_dept(self):
        print("\nDepartment Information")
        print("----------------------")
        print(f"ID        : {self.dept_id}")
        print(f"Name      : {self.name}")
        print(f"Location  : {self.location}")
        print(f"Head      : {self.dept_head}")

# List to store department objects
departments = []

# 1. Take user input
num_departments = int(input("Enter the number of departments: "))
for i in range(num_departments):
    print(f"\nEnter details for department {i+1}:")
    dept_id = int(input("ID: "))
    name = input("Name: ")
    location = input("Location: ")
    dept_head = input("Department Head: ")
    dept = Department(dept_id, name, location, dept_head)
    departments.append(dept)

# 2. Display all departments
print("\nAll Departments:")
for dept in departments:
    dept.display_dept()

# 3. Display total departments
print(f"\nTotal departments: {Department.total_departments}")

# 4. Search by dept ID
search_id = int(input("\nEnter dept ID to search: "))
found = False
for dept in departments:
    if dept.dept_id == search_id:
        print("\nDepartment Found:")
        dept.display_dept()
        found = True
        break
if not found:
    print("Department with that ID not found.")

# 5. Search by dept name
search_name = input("\nEnter dept name to search: ").lower()
found = False
for dept in departments:
    if (dept.name.lower().startswith(search_name) or
    dept.name.lower().endswith(search_name) or
    search_name in dept.name.lower()):
        print("\nDepartment Found:")
        dept.display_dept()
        found = True
        break
if not found:
    print("Department with that name not found.")