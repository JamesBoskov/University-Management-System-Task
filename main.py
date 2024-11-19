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
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_average_grade(self):
        return (sum[self.grades] / len(self.grades))
    
    def get_student_summary(self):
        return [self.name, self.calculate_average_grade()]

    