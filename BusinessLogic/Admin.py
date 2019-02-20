
from OOPCourseWorkTwo.BusinessLogic.User import User

class Administrator(User):

    def __init__(self, user_id=None, full_name=None, username=None, password=None, admin_id=None):
        super.__init__(user_id, full_name, username, password)
        self.__admin_id = admin_id









    def __str__(self):
        return ("This is Administartor Object")