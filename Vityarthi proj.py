employees=[]


# add employee
def add():
    
    
   

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")

    try:
        salary = float(input("Enter Basic Salary: "))
    except ValueError:
        print("Invalid salary!")
        return

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "designation": designation,
        "salary": salary,
        "attendance": 0,
        "leave": 0
    }

    employees.append(employee)
    

    print("Employee added successfully!")
    




#employee details
def display():
    

    print(" EMPLOYEE DETAILS")
    
    

    if len(employees) == 0:
        print("No employees found.")
        return

    for emp in employees:
        print("Employee ID   :", emp["id"])
        print("Name          :", emp["name"])
        print("Department    :", emp["department"])
        print("Designation   :", emp["designation"])
        print("Basic Salary  :", emp["salary"])
        print("Attendance    :", emp["attendance"])
        print("Leave Taken   :", emp["leave"])


# search employee
def search():
    print("employee search")

    emp_id = input("Enter Employee ID: ")

    found = False

    for emp in employees:
        if emp["id"] == emp_id:
            print("\nEmployee Found")
            print("Name        :", emp["name"])
            print("Department  :", emp["department"])
            print("Designation :", emp["designation"])
            print("Salary      :", emp["salary"])
            found = True
            break

    if found == False:
        print("Employee not found.")


# updated employee details
def update():
    print(" UPDATE EMPLOYEE")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:

            print("\n1. Update Name")
            print("2. Update Department")
            print("3. Update Designation")
            print("4. Update Salary")

            choice = input("Enter your choice: ")

            if choice == "1":
                emp["name"] = input("Enter new name: ")

            elif choice == "2":
                emp["department"] = input("Enter new department: ")

            elif choice == "3":
                emp["designation"] = input("Enter new designation: ")

            elif choice == "4":
                try:
                    emp["salary"] = float(input("Enter new salary: "))
                except ValueError:
                    print("Invalid salary.")
                    return

            else:
                print("Invalid choice.")
                return

            print("Employee updated successfully!")
            return

    print("Employee not found.")


# remove employee
def delete():
    print("DELETE EMPLOYEE")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee deleted successfully!")
            return

    print("Employee not found.")

# attendence
def attendance():
    print("ATTENDANCE")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            emp["attendance"] = emp["attendance"] + 1
            print("Attendance marked successfully!")
            return

    print("Employee not found.")


# apply for leave
def apply_leave():
    print("APPLY LEAVE")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:

            try:
                days = int(input("Enter number of leave days: "))
            except ValueError:
                print("Please enter a valid number.")
                return

            if days > 0:
                emp["leave"] = emp["leave"] + days
                print("Leave applied successfully!")
            else:
                print("Invalid number of days.")

            return

    print("Employee not found.")

# salary
def salary():
    print("SALARY CALCULATION ")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:

            basic = emp["salary"]

            # Allowance
            hra = basic * 0.20
            da = basic * 0.10

            # Total salary
            gross_salary = basic + hra + da

            # Tax
            tax = gross_salary * 0.10

            # Net salary
            net_salary = gross_salary - tax

            print("\nBasic Salary :", basic)
            print("HRA          :", hra)
            print("DA           :", da)
            print("Gross Salary :", gross_salary)
            print("Tax          :", tax)
            print("Net Salary   :", net_salary)

            return

    print("Employee not found.")


# Main method
while True:

    
    print("       OFFICE MANAGEMENT SYSTEM")
    print(())

    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Mark Attendance")
    print("7. Apply Leave")
    print("8. Calculate Salary")
    print("9. Exit")

    choice = input("\nEnter your choice: ")



    if choice == "1":
        print(" add employee")
        add()
        
        print("CHECK AFTER ADD:",employees)

    elif choice == "2":
        display()

       
        

       

    elif choice == "3":
        print("employee search")
        search()

    elif choice == "4":
        print(" UPDATE EMPLOYEE")
        update()

    elif choice == "5":
        print("DELETE EMPLOYEE")
        delete()

    elif choice == "6":
        print("ATTENDANCE")
        attendance()

    elif choice == "7":
        print("APPLY LEAVE")
        apply_leave()

    elif choice == "8":
        print("SALARY CALCULATION ")
        salary()

    elif choice == "9":
        print("Exit!")
        break

    else:
        print("Invalid choice.")

