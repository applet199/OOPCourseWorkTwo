

from OOPCourseWorkTwo.BusinessLogic.User import User


class Student(User):

    def __init__(self, user_id=None, full_name=None, username=None, password=None, student_id=None):
        super.__init__(user_id, full_name, username, password)
        self.__student_id = student_id










    def __str__(self):
        return ("This is Student Object")