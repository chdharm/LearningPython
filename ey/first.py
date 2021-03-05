import copy

def decor(func):
    def inner(students):
        new_students = deepcopy(students)
        for val in new_students.keys():
            if new_students[val].age > 20:
                new_students[val]["address"] = 'central'
        return func(new_students)
    return inner


class Student:
    def __init__(self):
        self.students = {
            "Peter": {"age": 10, "address": "Lisbon"},
            "Isabel": {"age": 11, "address": "Sesimbra"},
            "Anna": {"age": 9, "address": "Lisbon"},
            "Rust": {"age": 24, "address": "Lousiana"},
            "marty": {"age": 9, "address": "Texas"},
            "Kendrick": {"age": 43, "address": "LA"},
            "Lamar": {"age": 34, "address": "London"}
        }

    def get_number_of_students(self):
        return len(self.students.keys())

    def get_students_averge_age(self, students):
        total_students = self.get_number_of_students()
        total_age = 0
        for key in self.students.keys():
            total_age += students[key]["age"]
        print("total_students:", total_students)
        print("total_age:", total_age)
        return total_age / total_students

    def get_students_with_address(self, students, address):
        return [x for x in students.keys() if students[x]["address"] == address]

    @staticmethod
    def test_decor(self, students):
        print(students)

if __name__ == '__main__':
    st = Student()
    print(st.get_number_of_students())
    print(st.get_students_averge_age(st.students))
    print(st.get_students_with_address(st.students, "Lisbon"))
    print(st.test_decor(st.students))
#
# Design Class Student with following information :
#
# students = {
# "Peter": {"age": 10, "address": "Lisbon"},
# "Isabel": {"age": 11, "address": "Sesimbra"},
# "Anna": {"age": 9, "address": "Lisbon"},
# "Rust": {"age": 24, "address": "Lousiana"},
# "marty": {"age": 9, "address": "Texas"},
# "Kendrick": {"age": 43, "address": "LA"},
# "Lamar": {"age": 34, "address": "London"}
# }
#
# 1. Implement a method to return number of students are in the "students" dict
# 2. Implement a method that receives the students dict and returns the average age
# 3. Implement a method that receives the students dict and an address, and returns
# a list with the name of all students which address matches the address in the
# argument. For instance, invoking "find_students(students, ’Lisbon’)" should return
# Peter and Anna.
# 4. Implement a decorator to override the address of students with age above 20 as 'central' and return updated dictionary as O/P
