class InvalidAgeException(Exception):
    pass

class InvalidDesignationException(Exception):
    pass

def get_employee():
    name = input("Enter your name: ")
    
    while True:
        try:
            age = int(input("Enter your age (18-60): "))
            if not (18 <= age <= 60):
                raise InvalidAgeException("Age must be between 18 and 60.")
            break
        except ValueError:
            print("Please enter a valid integer for age.")
        except InvalidAgeException as e:
            print(e)

    while True:
        try:
            designation = input("Enter your designation (Programmer/Manager/Tester): ").strip().lower()
            if designation == "programmer":
                salary = 25000
            elif designation == "manager":
                salary = 30000
            elif designation == "tester":
                salary = 20000
            else:
                raise InvalidDesignationException("Invalid designation entered.")
            break
        except InvalidDesignationException as e:
            print(e)

    confirm = input("Confirm details? (y/n): ").strip().lower()
    if confirm == 'y' or confirm == '':
        print("\nEmployee Details:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Designation: {designation.capitalize()}")
        print(f"Salary: {salary}")
        with open("employees.txt", "a") as f:
            f.write(f"{name},{age},{designation},{salary}\n")
        return {"name": name, "age": age, "designation": designation, "salary": salary}
    else:
        print("Entry cancelled.")
        return None

def display_employees():
    try:
        with open("employees.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No employee records found.")
                return
            print("\nAll Employees:")
            for line in lines:
                name, age, designation, salary = line.strip().split(",")
                print(f"Name: {name}, Age: {age}, Designation: {designation.capitalize()}, Salary: {salary}")
    except FileNotFoundError:
        print("No employee records found.")

def raise_salary():
    name_to_raise = input("Enter the name of the person to give a hike: ")
    try:
        with open("employees.txt", "r") as f:
            employees = [line.strip().split(",") for line in f.readlines()]
    except FileNotFoundError:
        print("No employee records found.")
        return

    found = False
    for emp in employees:
        if emp[0].lower() == name_to_raise.lower():
            found = True
            while True:
                try:
                    percent = float(input("Enter hike percent (1-30): "))
                    if not (1 <= percent <= 30):
                        print("Percent must be between 1 and 30.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            old_salary = float(emp[3])
            new_salary = old_salary + (old_salary * percent / 100)
            emp[3] = f"{new_salary:.2f}"
            print(f"{emp[0]}'s new salary is {emp[3]}")
            break
    if not found:
        print("Employee not found.")
        return

    with open("employees.txt", "w") as f:
        for emp in employees:
            f.write(",".join(emp) + "\n")

def main():
    print("Welcome to Employee Management Application")
    while True:
        print("\nMenu:")
        print("1. Create Employee")
        print("2. Display Employees")
        print("3. Raise Salary")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            get_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            raise_salary()
        elif choice == '4':
            print("Thank you for using the application.")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
