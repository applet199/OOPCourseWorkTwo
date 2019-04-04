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

    @classmethod
    def get_exam_details_by_id(cls, exam_id):
        query = '''
            SELECT exam_pk,
                questions_ids
            FROM exam
            WHERE exam_pk = ?
        '''
        cls.__cursor.execute(query, (exam_id, ))
        exams_details_tuple = cls.__cursor.fetchone()
        return exams_details_tuple

    @classmethod
    def get_question_type_by_id(cls, question_id):
        query = '''
            SELECT question_type
            FROM question
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(query, (question_id, ))
        question_type_tuple = cls.__cursor.fetchone()
        return question_type_tuple[0]

    @classmethod
    def get_single_answer_question_details_by_id(cls, question_pk):
        select_single_answer_question_details_query = '''
            SELECT question_pk,
                points,
                question_body,
                option_A_text,
                option_B_text,
                option_C_text,
                option_D_text,
                option_E_text,
                correct_answer
            FROM question
            INNER JOIN single_answer_question on question_pk = question_fk
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(select_single_answer_question_details_query, (question_pk, ))
        question_details_list = cls.__cursor.fetchall()
        question_details = question_details_list[0]
        return question_details

    @classmethod
    def insert_exam_result_by_id_to_db(cls, exam_pk):
        students_ids_string = cls.get_all_students_of_exam_by_id(exam_pk)
        aggregate_points_by_students_ids = ""
        for student_id in students_ids_string.split(" "):
            if (student_id != ""):
                aggregate_points_by_students_ids = aggregate_points_by_students_ids + "(" + str(student_id) + ",0) "
        query = '''
            INSERT INTO exam_result (
                exam_result_pk,
                aggregate_points_by_students_ids
                )
            VALUES (?, ?)
        '''
        cls.__cursor.execute(query, (exam_pk, aggregate_points_by_students_ids))
        cls.__db_connection.commit()



    @classmethod
    def get_all_students_of_exam_by_id(cls, exam_pk):
        query = '''
            SELECT students_ids
            FROM exam
            WHERE exam_pk = ?
        '''
        cls.__cursor.execute(query, (exam_pk, ))
        students_ids_tuple = cls.__cursor.fetchone()
        students_ids = students_ids_tuple[0]
        return students_ids


    @classmethod
    def is_single_answer_correct_by_question_id(cls, question_pk, student_answer):
        query = '''
            SELECT correct_answer
            FROM single_answer_question
            WHERE question_fk = ?
        '''
        cls.__cursor.execute(query, (question_pk, ))
        correct_answer_tuple = cls.__cursor.fetchone()
        correct_answer = correct_answer_tuple[0]
        student_answer = student_answer.rstrip()
        is_correct = student_answer is correct_answer
        return is_correct

    @classmethod
    def is_exam_result_id_already_in_db(cls, exam_result_pk):
        query = '''
            SELECT exam_result_pk
            FROM exam_result
            WHERE exam_result_pk = ?
        '''
        cls.__cursor.execute(query, (exam_result_pk, ))
        exam_result_pk_tuple = cls.__cursor.fetchone()
        return exam_result_pk_tuple != None

    @classmethod
    def get_question_points_by_id(cls, question_id):
        query = '''
            SELECT points
            FROM question
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(query, (question_id,))
        points_tuple = cls.__cursor.fetchone()
        points= points_tuple[0]
        return points

    @classmethod
    def add_question_points_to_exam_result_by_student_id_in_DB(cls, exam_result_pk, student_pk, points):
        aggregate_points_by_students_ids_string = cls.get_aggregate_points_by_students_ids_string_by_exam_result_id(exam_result_pk)
        aggregate_points_by_students_ids_list = aggregate_points_by_students_ids_string.split(" ")
        for aggregate_points_by_student_id in aggregate_points_by_students_ids_list:
            student_id_and_old_points = aggregate_points_by_student_id.split(",")
            student_id_string = student_id_and_old_points[0]
            old_points_string = student_id_and_old_points[1]
            student_id = int(student_id_string.strip("("))
            if (student_id == student_pk):
                old_points = int(old_points_string.strip(")"))
                new_points = old_points + points
                student_id_and_new_points = "(" + str(student_id) + "," + str(new_points) + ")"
                aggregate_points_by_students_ids_string = aggregate_points_by_students_ids_string.replace(student_id_and_old_points, student_id_and_new_points)
        cls.update_aggregate_points_by_students_ids_by_exam_id(exam_result_pk)

    @classmethod
    def get_aggregate_points_by_students_ids_string_by_exam_result_id(cls, exam_result_pk):
        query = '''
            SELECT aggregate_points_by_students_ids
            FROM exam_result
            WHERE exam_result_pk = ?
        '''
        cls.__cursor.execute(query, (exam_result_pk,))
        aggregate_points_by_students_ids_tuple = cls.__cursor.fetchone()
        aggregate_points_by_students_ids = aggregate_points_by_students_ids_tuple[0]
        return aggregate_points_by_students_ids.rstrip()


    def __str__(self):
        return ("This is StudentDA Object")