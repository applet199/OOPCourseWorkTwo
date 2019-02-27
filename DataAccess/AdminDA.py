


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
                       student_full_name
                FROM student
                '''
        cls.__cursor.execute(query)
        students = cls.__cursor.fetchall()
        return students

    @classmethod
    def get_all_teachers_from_db(cls):
        query = '''
                SELECT teacher_pk,
                       teacher_full_name
                FROM teacher
                '''
        cls.__cursor.execute(query)
        teachers = cls.__cursor.fetchall()
        return teachers

    @classmethod
    def get_all_admins_from_db(cls):
        query = '''
                SELECT admin_pk,
                       admin_full_name
                FROM admin
                '''
        cls.__cursor.execute(query)
        admins = cls.__cursor.fetchall()
        return admins

    @classmethod
    def get_all_school_classes_from_db(cls):
        query = '''
                SELECT school_class_pk
                FROM school_class
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
    def get_total_number_of_teachers_from_db(cls):
        total_number_of_teachers_query = '''
                                         SELECT count(*)
                                         FROM teacher
                                         '''
        cls.__cursor.execute(total_number_of_teachers_query)
        teachers_count_tuple = cls.__cursor.fetchone()
        teachers_count = 0
        if (teachers_count_tuple != None):
            teachers_count = teachers_count_tuple[0]
        return teachers_count

    @classmethod
    def insert_new_user_to_db(cls, user_pk, login_name, password, user_type, user_full_name):
        insert_new_user_query = '''
                                INSERT INTO user (
                                    user_pk,
                                    login_name,
                                    password,
                                    user_type,
                                    user_full_name)
                                VALUES
                                    (?, ?, ?, ?, ?)
                                '''
        cls.__cursor.execute(insert_new_user_query, (user_pk, login_name, password, user_type, user_full_name))
        cls.__db_connection.commit()

    @classmethod
    def insert_new_student_to_db(cls, student_pk, student_full_name, date_of_birth, school_class_id):
        insert_new_student_query = '''
                                   INSERT INTO student (
                                        student_pk,
                                        student_full_name,
                                        date_of_birth,
                                        class_fk)
                                   VALUES
                                        (?, ?, ?, ?)
                                   '''
        cls.__cursor.execute(insert_new_student_query, (student_pk, student_full_name, date_of_birth, school_class_id))
        cls.__db_connection.commit()

    @classmethod
    def insert_new_teacher_to_db(cls, teacher_pk, teacher_full_name, date_of_birth):
        insert_new_teacher_query = '''
                                   INSERT INTO teacher (
                                        teacher_pk,
                                        teacher_full_name,
                                        date_of_birth)
                                   VALUES
                                        (?, ?, ?)
                                   '''
        cls.__cursor.execute(insert_new_teacher_query, (teacher_pk, teacher_full_name, date_of_birth))
        cls.__db_connection.commit()


    @classmethod
    def get_student_details_tuple_by_id(cls, student_pk):
        select_student_details_query = '''
                                        SELECT student_full_name,
                                               login_name,
                                               password,
                                               date_of_birth,
                                               school_class_fk
                                        FROM user
                                        INNER JOIN student
                                        WHERE user.user_full_name = student.student_full_name
                                        AND student_pk = ?
                                        '''
        cls.__cursor.execute(select_student_details_query, (student_pk, ))
        student_details_tuple = cls.__cursor.fetchone()
        return student_details_tuple

    @classmethod
    def get_teacher_details_tuple_by_id(cls, teacher_pk):
        select_teacher_details_query = '''
                                        SELECT teacher_full_name,
                                               login_name,
                                               password,
                                               date_of_birth
                                        FROM user
                                        INNER JOIN teacher
                                        WHERE user.user_full_name = teacher.teacher_full_name
                                        AND teacher_pk = ?
                                        '''
        cls.__cursor.execute(select_teacher_details_query, (teacher_pk, ))
        teacher_details_tuple = cls.__cursor.fetchone()
        return teacher_details_tuple

    @classmethod
    def get_admin_details_tuple_by_id(cls, admin_pk):
        select_admin_details_query = '''
                                        SELECT admin_full_name,
                                               login_name,
                                               password,
                                               date_of_birth
                                        FROM user
                                        INNER JOIN admin
                                        WHERE user.user_full_name = admin.admin_full_name
                                        AND admin_pk = ?
                                        '''
        cls.__cursor.execute(select_admin_details_query, (admin_pk, ))
        admin_details_tuple = cls.__cursor.fetchone()
        return admin_details_tuple

    @classmethod
    def get_school_class_details_tuples_list_by_id(cls, school_class_pk):
        select_school_class_details_query = '''
                                        SELECT school_class_pk,
                                               year_level,
                                               student_pk,
                                               student_full_name
                                        FROM student
                                        INNER JOIN school_class
                                        WHERE student.school_class_fk = school_class.school_class_pk
                                        AND school_class_pk = ?
                                        '''
        cls.__cursor.execute(select_school_class_details_query, (school_class_pk, ))
        school_class_details_tuples_list = cls.__cursor.fetchall()
        return school_class_details_tuples_list


    def __str__(self):
        return ("This is AdminDA Object")