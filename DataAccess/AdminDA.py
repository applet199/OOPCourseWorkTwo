


import sqlite3
from sqlite3 import Error

class AdminDA():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, connection):
        cls.__db_connection = connection
        cls.__cursor = connection.cursor()

    @classmethod
    def get_all_students_from_db(cls):
        query = '''
                SELECT student_pk,
                       student_name
                FROM student
                '''
        cls.__cursor.execute(query)
        students = cls.__cursor.fetchall()
        return students

    @classmethod
    def get_all_teachers_from_db(cls):
        query = '''
                SELECT teacher_pk,
                       teacher_name
                FROM teacher
                '''
        cls.__cursor.execute(query)
        teachers = cls.__cursor.fetchall()
        return teachers

    @classmethod
    def get_all_admins_from_db(cls):
        query = '''
                SELECT admin_pk,
                       admin_name
                FROM admin
                '''
        cls.__cursor.execute(query)
        admins = cls.__cursor.fetchall()
        return admins

    @classmethod
    def get_all_school_classes_from_db(cls):
        query = '''
                SELECT class_pk
                FROM class
                '''
        cls.__cursor.execute(query)
        school_classes = cls.__cursor.fetchall()
        return school_classes

    @classmethod
    def get_total_number_of_users_from_db(cls):
        total_number_of_users_query = '''
                                      SELECT count(*)
                                      FROM user
                                      '''
        cls.__cursor.execute(total_number_of_users_query)
        users_count_tuple = cls.__cursor.fetchone()
        users_count = 0
        if (users_count_tuple != None):
            users_count = users_count_tuple[0]
        return users_count

    @classmethod
    def get_total_number_of_students_from_db(cls):
        total_number_of_students_query = '''
                                         SELECT count(*)
                                         FROM student
                                         '''
        cls.__cursor.execute(total_number_of_students_query)
        students_count_tuple = cls.__cursor.fetchone()
        students_count = 0
        if (students_count_tuple != None):
            students_count = students_count_tuple[0]
        return students_count

    @classmethod
    def insert_new_user_to_db(cls, user_pk, user_name, password, user_type):
        insert_new_user_query = '''
                                INSERT INTO user (
                                    user_pk,
                                    user_name,
                                    password,
                                    user_type)
                                VALUES
                                    (?, ?, ?, ?)
                                '''
        cls.__cursor.execute(insert_new_user_query, (user_pk, user_name, password, user_type))
        cls.__db_connection.commit()

    @classmethod
    def insert_new_student_to_db(cls, student_pk, student_name, date_of_birth, school_class_id):
        insert_new_student_query = '''
                                   INSERT INTO student (
                                        student_pk,
                                        student_name,
                                        date_of_birth,
                                        class_fk)
                                   VALUES
                                        (?, ?, ?, ?)
                                   '''
        cls.__cursor.execute(insert_new_student_query, (student_pk, student_name, date_of_birth, school_class_id))
        cls.__db_connection.commit()

    def __str__(self):
        return ("This is AdminDA Object")