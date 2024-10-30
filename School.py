class School:
    def __init__(self, name):
        # Public attribute
        self.name = name

        # Private attributes (encapsulated)
        self.__students = []
        self.__total_funds = 0.0

    # Method to add a student
    def add_student(self, student_name):
        self.__students.append(student_name)
        print(f"Student {student_name} added to the school.")

    # Method to remove a student
    def remove_student(self, student_name):
        if student_name in self.__students:
            self.__students.remove(student_name)
            print(f"Student {student_name} removed from the school.")
        else:
            print(f"Student {student_name} not found.")

    # Method to add funds (private access)
    def __add_funds(self, amount):
        if amount > 0:
            self.__total_funds += amount
            print(f"Funds added: ${amount}. Total funds: ${self.__total_funds}")
        else:
            print("Amount must be positive.")

    # Public method to accept donations
    def accept_donation(self, amount):
        print("Accepting donation...")
        self.__add_funds(amount)

    # Public method to check total funds (read-only access)
    def get_total_funds(self):
        print(f"Total funds: ${self.__total_funds}")
        return self.__total_funds

    # Method to get all students (read-only access)
    def get_students(self):
        print("Listing all students:")
        for student in self.__students:
            print(student)
        return self.__students

# Example usage
school = School("Koiarbil High School")

# Public method to add students
school.add_student("Alice")
school.add_student("Bob")
school.remove_student("Alice")

# Listing students (read-only access)
school.get_students()

# Accept donations (controls fund addition)
school.accept_donation(1000.0)

# Check total funds (read-only access)
school.get_total_funds()

# Direct access to private attributes (raises AttributeError)
# print(school.__students)  # Not accessible directly
# print(school.__total_funds)  # Not accessible directly