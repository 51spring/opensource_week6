# 성적관리프로그램 (객체지향 프로그램으로 수정하기)

#  조건: 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 

#          키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를  계산하는 프로그램 작성

#        - 입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수 

#        - 삽입 함수, 삭제 함수, 탐색함수(학번, 이름), 정렬(총점)함수, 80점이상 학생 수 카운트 함수 


class Student:
    def __init__(self, student_id, name, english, c_language, python): # 학생의 정보를 저장하는 클래스
        self.student_id = student_id
        self.name = name
        self.english = english
        self.c_language = c_language
        self.python = python
        self.total = self.calculate_total()
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()
        self.rank = None

    def calculate_total(self): # 총점을 계산하는 메소드 
        return self.english + self.c_language + self.python

    def calculate_average(self): # 평균을 계산하는 메소드
        return round(self.total / 3, 2)

    def calculate_grade(self): # 학점을 계산하는 메소드
        if self.average >= 95:
            return 'A+'
        elif self.average >= 90:
            return 'A'
        elif self.average >= 85:
            return 'B+'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 75:
            return 'C+'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 65:
            return 'D+'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'

    def __str__(self): # 학생의 정보를 출력하는 메소드
        return "\t".join(str(x) for x in [self.student_id, self.name, self.english, self.c_language, self.python, self.total, self.average, self.grade, self.rank])


def get_input(): # 학생들의 정보를 입력받는 함수
    students = []
    for _ in range(5):
        student_id = input("학번: ")
        name = input("이름: ")
        english = int(input("영어: "))
        c_language = int(input("C-언어: "))
        python = int(input("파이썬: "))
        students.append(Student(student_id, name, english, c_language, python))
    return students


def calculate_rank(students): # 학생들의 등수를 계산하는 함수
    students.sort(key=lambda x: x.average, reverse=True)
    for i, student in enumerate(students, start=1):
        student.rank = i
    return students


def print_results(students): # 학생들의 정보를 출력하는 함수
    print("성적관리 프로그램")
    print("=============================================================================")
    print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("=============================================================================")
    for student in students:
        print(student)


def count_students(students): # 평균이 80점 이상인 학생 수를 계산하는 함수
    count = sum(1 for student in students if student.average >= 80)
    print(f"평균이 80점 이상인 학생수: {count}")


students = get_input() # 학생들의 정보를 입력
students = calculate_rank(students) # 학생들의 등수를 계산
print_results(students) # 학생들의 정보를 출력
count_students(students) # 평균이 80점 이상인 학생 수를 출력