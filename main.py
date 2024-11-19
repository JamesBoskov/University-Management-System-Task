class person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_details(self):
        return {"Name" : self.name, 
        "Age" : self.age, 
        "Gender" : self.gender}

class student(person):
    def __init__(self, name, age, gender, student_id, course, grades):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course
        self.grades = grades
    def set_student_details(self, student_id, course):
        self.student_id = student_id
        self.course = course
    
    def add_grade(self, grades):
        for grade in grades:
            self.grades.append(grade)
    
    def calculate_average_grade(self):
        return (sum(self.grades) / len(self.grades))
    
    def get_student_summary(self):
        return self.name, self.calculate_average_grade()

class proffesor(person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
    
    def set_professor_details(self, staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
    
    def give_feedback(self, student, feedback):
        print(f"Feedback for {student.name}: {feedback}")
    
    def increase_salary(self, percentage):
        self.salary *= (1 + percentage/100)
    
    def get_professor_summary(self):
        return self.name, self.salary
    
class administatrator(person):
    def __init__(self, name, age, gender, admin_id, office, years_of_service):
        super().__init__(name, age, gender)
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
    
    def set_admin_details(self, admin_id, office, years_of_service):
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service

    def increment_service_years(self):
        self.years_of_service += 1
    
    def get_admin_summary(self):
        return self.name, self.years_of_service

doug = student("Doug", 17, "Male", 12345, "English", [1])
dog = student("Dog", 19, "Dog", 12346, "When asked he replied woof woof", [0]) # years as in dog years

douglas = proffesor("Douglas", 24, "Male", 12345, "English", 12345)
douglette = proffesor("Douglette", 28, "Female", 12346, "Spanish (those who know)", 10000)

dougie = administatrator("Dougie", "unknown", "unknown", "refused", "No", 7)

doug.add_grade([1, 2, 3, 4, 5])
doug.calculate_average_grade

douglas.give_feedback(dog, "You are genuinely a dog, get out of my classroom")
douglas.increase_salary(10)

dougie.increment_service_years()

print(doug.get_student_summary(), douglas.get_professor_summary(), dougie.get_admin_summary())