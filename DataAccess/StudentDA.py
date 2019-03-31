import sqlite3
from sqlite3 import Error

class StudentDA():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, connection):
        cls.__db_connection = connection
        cls.__cursor = connection.cursor()

    @classmethod
    def setup_student_id_for_current_session(cls, student_id):
        cls.__student_id = student_id


    @classmethod
    def get_not_completed_exams_for_current_student(cls):
        current_student_school_class_id = cls.get_current_student_school_class_id()
        not_completed_exams_details = cls.get_not_completed_exams_details()

        not_completed_exams_ids_for_current_student = []
        for (exam_id, string_of_school_classes_ids) in not_completed_exams_details:
            list_of_school_classes_ids = str(string_of_school_classes_ids).split(" ")
            if ((list_of_school_classes_ids.count(str(current_student_school_class_id))) == 1):
                not_completed_exams_ids_for_current_student.append(exam_id)
        return not_completed_exams_ids_for_current_student



    @classmethod
    def get_current_student_school_class_id(cls):
        query = '''
            SELECT school_class_fk
            FROM student
            WHERE student_pk = ?

        '''
        cls.__cursor.execute(query, (cls.__student_id, ))
        school_class_id_tuple = cls.__cursor.fetchone()
        school_class_id = school_class_id_tuple[0]
        return school_class_id

    @classmethod
    def get_not_completed_exams_details(cls):
        query = '''
            SELECT exam_pk,
                school_classes_ids
            FROM exam
            WHERE exam_status = ?

        '''
        cls.__cursor.execute(query, ("Not Completed", ))
        not_completed_exams_details_tuple = cls.__cursor.fetchall()
        return not_completed_exams_details_tuple



    def __str__(self):
        return ("This is StudentDA Object")