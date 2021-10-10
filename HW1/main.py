from application.salary import calculate_salary
from application.db import people

if __name__ == '__main__':
    people.get_employees('John')
    calculate_salary('John')
