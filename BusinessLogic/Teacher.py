

from OOPCourseWorkTwo.BusinessLogic.User import User


class Teacher(User):

    def __init__(self, user_id=None, full_name=None, username=None, password=None, teacher_id=None):
        super.__init__(user_id, full_name, username, password)
        self.__teacher_id = teacher_id









    def __str__(self):
        return ("This is Teacher Object")