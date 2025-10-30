class Student:
    def __init__(self,name,korean,math,english,science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())
    
students = [
    Student("김길동",87,97,88,95),
    Student("이길동",83,98,82,97),
    Student("박길동",82,91,85,94),
    Student("장길동",81,20,86,95),
    Student("최길동",85,91,88,92),
    Student("김길동",86,91,81,90),
]

print("이름","총점","평균", sep="\t")
for student in students:
    print(student.to_string())