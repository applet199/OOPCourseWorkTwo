import sqlite3
from sqlite3 import Error

class TeacherDA():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, connection):
        cls.__db_connection = connection
        cls.__cursor = connection.cursor()

    @classmethod
    def get_all_active_school_classes_from_db(cls):
        query = '''
                SELECT school_class_pk
                FROM school_class
                WHERE active = 1
                '''
        cls.__cursor.execute(query)
        active_school_classes = cls.__cursor.fetchall()
        return active_school_classes


    @classmethod
    def insert_single_answer_question_into_db(cls, single_answer_question_details):
        total_number_of_questions = cls.get_total_number_of_questions_in_db()
        question_pk = total_number_of_questions + 1

        total_number_of_single_answer_questions = cls.get_total_number_of_single_answer_questions_in_db()
        single_answer_question_pk = total_number_of_single_answer_questions + 1

        question_body = single_answer_question_details[0]
        option_A_text = single_answer_question_details[1]
        option_B_text = single_answer_question_details[2]
        option_C_text = single_answer_question_details[3]
        option_D_text = single_answer_question_details[4]
        option_E_text = single_answer_question_details[5]
        year_level = single_answer_question_details[6]
        question_tag = single_answer_question_details[7]
        correct_ansewr = cls.get_correct_answer_string_for_single_answer_question(single_answer_question_details[8])
        insert_into_question_table_query = '''
           INSERT INTO question (
             question_pk,
             question_type,
             points,
             year_level,
             question_tag
             )
           VALUES (?, ?, ?, ?, ?)
        '''
        cls.__cursor.execute(insert_into_question_table_query, (question_pk, "Single Answer", 10, year_level, question_tag))
        cls.__db_connection.commit()
        insert_into_single_answer_question_table_query = '''
            INSERT INTO single_answer_question (
              single_answer_question_pk,
              question_body,
              option_A_text,
              option_B_text,
              option_C_text,
              option_D_text,
              option_E_text,
              correct_answer,
              question_fk
              )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cls.__cursor.execute(insert_into_single_answer_question_table_query, (single_answer_question_pk, question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, correct_ansewr, question_pk))
        cls.__db_connection.commit()


    @classmethod
    def insert_multiple_answers_question_into_db(cls, multiple_answers_question_details):
        total_number_of_questions = cls.get_total_number_of_questions_in_db()
        question_pk = total_number_of_questions + 1

        total_number_of_multiple_answers_questions = cls.get_total_number_of_multiple_answers_questions_in_db()
        multiple_answers_question_pk = total_number_of_multiple_answers_questions + 1

        question_body = multiple_answers_question_details[0]
        option_A_text = multiple_answers_question_details[1]
        option_B_text = multiple_answers_question_details[2]
        option_C_text = multiple_answers_question_details[3]
        option_D_text = multiple_answers_question_details[4]
        option_E_text = multiple_answers_question_details[5]
        year_level = multiple_answers_question_details[6]
        question_tag = multiple_answers_question_details[7]
        correct_answers = cls.get_correct_answers_string_for_multiple_answers_question(multiple_answers_question_details[8])
        insert_into_question_table_query = '''
           INSERT INTO question (
             question_pk,
             question_type,
             points,
             year_level,
             question_tag
             )
           VALUES (?, ?, ?, ?, ?)
        '''
        cls.__cursor.execute(insert_into_question_table_query, (question_pk, "Multiple Answers", 10, year_level, question_tag))
        cls.__db_connection.commit()
        insert_into_multiple_answers_question_table_query = '''
            INSERT INTO multiple_answers_question (
              multiple_answers_question_pk,
              question_body,
              option_A_text,
              option_B_text,
              option_C_text,
              option_D_text,
              option_E_text,
              correct_answers,
              question_fk
              )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cls.__cursor.execute(insert_into_multiple_answers_question_table_query, (multiple_answers_question_pk, question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, correct_answers, question_pk))
        cls.__db_connection.commit()

    @classmethod
    def insert_essay_question_into_db(cls, essay_question_details):
        total_number_of_questions = cls.get_total_number_of_questions_in_db()
        question_pk = total_number_of_questions + 1

        total_number_of_essay_questions = cls.get_total_number_of_essay_questions_in_db()
        essay_question_pk = total_number_of_essay_questions + 1

        question_body = essay_question_details[0]
        year_level = essay_question_details[1]
        question_tag = essay_question_details[2]

        insert_into_question_table_query = '''
           INSERT INTO question (
             question_pk,
             question_type,
             points,
             year_level,
             question_tag
             )
           VALUES (?, ?, ?, ?, ?)
        '''
        cls.__cursor.execute(insert_into_question_table_query, (question_pk, "Essay", 10, year_level, question_tag))
        cls.__db_connection.commit()
        insert_into_essay_question_table_query = '''
            INSERT INTO essay_question (
              essay_question_pk,
              question_body,
              question_fk
              )
            VALUES (?, ?, ?)
        '''
        cls.__cursor.execute(insert_into_essay_question_table_query, (essay_question_pk, question_body, question_pk))
        cls.__db_connection.commit()


    @classmethod
    def insert_exam_into_db(cls, exam_pk, questions_ids, school_classes_ids, exam_status):
        total_available_points = cls.get_total_available_points_by_questions_ids(questions_ids)
        number_of_questions = len(questions_ids.split(" ")) - 1
        students_ids = cls.get_students_ids_in_exam_by_school_classes_ids(school_classes_ids)
        query = '''
            INSERT INTO exam (
              exam_pk,
              questions_ids,
              school_classes_ids,
              exam_status,
              total_available_points,
              number_of_questions,
              students_ids
              )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        cls.__cursor.execute(query, (exam_pk, questions_ids, school_classes_ids, exam_status, total_available_points, number_of_questions, students_ids))
        cls.__db_connection.commit()

    @classmethod
    def get_total_available_points_by_questions_ids(cls, question_ids):
        total_available_points = 0
        questions_ids_list = question_ids.split(" ")
        for question_id in questions_ids_list:
            question_points = cls.get_question_available_points_by_id(question_id)
            total_available_points = total_available_points + question_points
        return total_available_points

    @classmethod
    def get_question_available_points_by_id(cls, question_pk):
        query = '''
            SELECT points
            FROM question
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(query, (question_pk,))
        available_points_tuple = cls.__cursor.fetchone()
        if (available_points_tuple == None):
            return 0
        available_points = available_points_tuple[0]
        return available_points

    @classmethod
    def get_students_ids_in_exam_by_school_classes_ids(cls, school_classes_ids_string):
        school_classes_ids = school_classes_ids_string.split(" ")
        students_ids_in_exam = ""
        for school_class_id in school_classes_ids:
            students_ids_in_school_class = cls.get_all_students_ids_in_school_class_by_id(school_class_id)
            students_ids_in_exam = students_ids_in_exam + students_ids_in_school_class
        return students_ids_in_exam

    @classmethod
    def get_school_classes_ids_in_exam_by_exam_id(cls, exam_pk):
        query = '''
            SELECT school_classes_ids
            FROM exam
            WHERE exam_pk = ?
        '''
        cls.__cursor.execute(query, (exam_pk,))
        school_classes_ids_tuple = cls.__cursor.fetchone()
        school_classes_ids = school_classes_ids_tuple[0]
        return school_classes_ids

    @classmethod
    def get_total_number_of_questions_in_db(cls):
        select_all_from_question_query = '''
            SELECT count(*)
            FROM question
        '''
        cls.__cursor.execute(select_all_from_question_query)
        total_number_of_questions_tuple = cls.__cursor.fetchone()
        total_number_of_questions = total_number_of_questions_tuple[0]
        return total_number_of_questions

    @classmethod
    def get_total_number_of_exams_in_db(cls):
        query = '''
            SELECT count(*)
            FROM exam
        '''
        cls.__cursor.execute(query)
        total_number_of_exams_tuple = cls.__cursor.fetchone()
        total_number_of_exams = total_number_of_exams_tuple[0]
        return total_number_of_exams

    @classmethod
    def get_total_number_of_single_answer_questions_in_db(cls):
        select_all_from_single_answer_question_query = '''
            SELECT count(*)
            FROM single_answer_question
        '''
        cls.__cursor.execute(select_all_from_single_answer_question_query)
        total_number_of_single_answer_questions_tuple = cls.__cursor.fetchone()
        total_number_of_single_answer_questions = total_number_of_single_answer_questions_tuple[0]
        return total_number_of_single_answer_questions

    @classmethod
    def get_total_number_of_multiple_answers_questions_in_db(cls):
        select_all_from_multiple_answers_question_query = '''
            SELECT count(*)
            FROM multiple_answers_question
        '''
        cls.__cursor.execute(select_all_from_multiple_answers_question_query)
        total_number_of_multiple_answers_questions_tuple = cls.__cursor.fetchone()
        total_number_of_multiple_answers_questions = total_number_of_multiple_answers_questions_tuple[0]
        return total_number_of_multiple_answers_questions

    @classmethod
    def get_total_number_of_essay_questions_in_db(cls):
        select_all_from_essay_question_query = '''
            SELECT count(*)
            FROM essay_question
        '''
        cls.__cursor.execute(select_all_from_essay_question_query)
        total_number_of_essay_questions_tuple = cls.__cursor.fetchone()
        total_number_of_essay_questions = total_number_of_essay_questions_tuple[0]
        return total_number_of_essay_questions

    @classmethod
    def get_correct_answer_string_for_single_answer_question(cls, correct_answer_list):
        correct_answer_string = correct_answer_list.pop()
        return correct_answer_string

    @classmethod
    def get_correct_answers_string_for_multiple_answers_question(cls, correct_answers_list):
        correct_answers_string = ""
        for answer in correct_answers_list:
            correct_answers_string = correct_answers_string + answer
        return correct_answers_string

    @classmethod
    def get_all_active_questions_from_db(cls):
        select_all_active_question_query='''
            SELECT question_pk
            FROM question
            WHERE active = 1
        '''
        cls.__cursor.execute(select_all_active_question_query)
        all_active_questions_tuple = cls.__cursor.fetchall()
        return all_active_questions_tuple

    @classmethod
    def get_all_exams_from_db(cls):
        query='''
            SELECT exam_pk
            FROM exam
        '''
        cls.__cursor.execute(query)
        all_exams_tuple = cls.__cursor.fetchall()
        return all_exams_tuple

    @classmethod
    def get_not_completed_exams_from_db(cls):
        query='''
            SELECT exam_pk
            FROM exam
            WHERE exam_status = ?
        '''
        cls.__cursor.execute(query, ("Not Completed", ))
        not_completed_exams_tuple = cls.__cursor.fetchall()
        return not_completed_exams_tuple

    @classmethod
    def get_question_type_by_id(cls, question_pk):
        select_question_type_by_id_query = '''
            SELECT question_type
            FROM question
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(select_question_type_by_id_query, (question_pk, ))
        question_type_tuple = cls.__cursor.fetchone()
        question_type = question_type_tuple[0]
        return question_type

    @classmethod
    def get_single_answer_question_details_by_id(cls, question_pk):
        select_single_answer_question_details_query = '''
            SELECT question_pk,
                question_type,
                points,
                year_level,
                question_tag,
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
    def get_multiple_answers_question_details_by_id(cls, question_pk):
        select_multiple_answers_question_details_query = '''
            SELECT question_pk,
                question_type,
                points,
                year_level,
                question_tag,
                question_body,
                option_A_text,
                option_B_text,
                option_C_text,
                option_D_text,
                option_E_text,
                correct_answers
            FROM question
            INNER JOIN multiple_answers_question on question_pk = question_fk
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(select_multiple_answers_question_details_query, (question_pk, ))
        question_details_list = cls.__cursor.fetchall()
        question_details = question_details_list[0]
        return question_details


    @classmethod
    def get_essay_question_details_by_id(cls, question_pk):
        select_essay_question_details_query = '''
            SELECT question_pk,
                question_type,
                points,
                year_level,
                question_tag,
                question_body
            FROM question
            INNER JOIN essay_question ON question_pk = question_fk
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(select_essay_question_details_query, (question_pk, ))
        question_details_list = cls.__cursor.fetchall()
        question_details = question_details_list[0]
        return question_details

    @classmethod
    def update_single_answer_question_details_in_db(cls, question_details):
        question_pk = question_details[0]
        question_type = question_details[1]
        points = question_details[2]
        year_level = question_details[3]
        question_tag = question_details[4]
        question_body = question_details[5]
        option_A_text = question_details[6]
        option_B_text = question_details[7]
        option_C_text = question_details[8]
        option_D_text = question_details[9]
        option_E_text = question_details[10]
        correct_answer = question_details[11]
        update_question_table_query = '''
            UPDATE question
            SET points = ?,
                year_level = ?,
                question_tag = ?
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(update_question_table_query, (points, year_level, question_tag, question_pk))
        cls.__db_connection.commit()

        update_single_answer_question_table_query = '''
            UPDATE single_answer_question
            SET question_body = ?,
                option_A_text = ?,
                option_B_text = ?,
                option_C_text = ?,
                option_D_text = ?,
                option_E_text = ?,
                correct_answer = ?
            WHERE question_fk = ?
        '''
        cls.__cursor.execute(update_single_answer_question_table_query, (question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, correct_answer, question_pk))
        cls.__db_connection.commit()

    @classmethod
    def update_multiple_answers_question_details_in_db(cls, question_details):
        question_pk = question_details[0]
        question_type = question_details[1]
        points = question_details[2]
        year_level = question_details[3]
        question_tag = question_details[4]
        question_body = question_details[5]
        option_A_text = question_details[6]
        option_B_text = question_details[7]
        option_C_text = question_details[8]
        option_D_text = question_details[9]
        option_E_text = question_details[10]
        correct_answers = question_details[11]
        update_question_table_query = '''
            UPDATE question
            SET points = ?,
                year_level = ?,
                question_tag = ?
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(update_question_table_query, (points, year_level, question_tag, question_pk))
        cls.__db_connection.commit()

        update_multiple_answers_question_table_query = '''
            UPDATE multiple_answers_question
            SET question_body = ?,
                option_A_text = ?,
                option_B_text = ?,
                option_C_text = ?,
                option_D_text = ?,
                option_E_text = ?,
                correct_answers = ?
            WHERE question_fk = ?
        '''
        cls.__cursor.execute(update_multiple_answers_question_table_query, (question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, correct_answers, question_pk))
        cls.__db_connection.commit()



    @classmethod
    def update_essay_question_details_in_db(cls, question_details):
        question_pk = question_details[0]
        question_type = question_details[1]
        points = question_details[2]
        year_level = question_details[3]
        question_tag = question_details[4]
        question_body = question_details[5]
        update_question_table_query = '''
            UPDATE question
            SET points = ?,
                year_level = ?,
                question_tag = ?
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(update_question_table_query, (points, year_level, question_tag, question_pk))
        cls.__db_connection.commit()

        update_essay_question_table_query = '''
            UPDATE essay_question
            SET question_body = ?
            WHERE question_fk = ?
        '''
        cls.__cursor.execute(update_essay_question_table_query, (question_body, question_pk))
        cls.__db_connection.commit()

    @classmethod
    def is_school_class_id_valid(cls, school_class_id):
        query = '''
                SELECT school_class_pk
                FROM school_class
                WHERE active = 1 AND school_class_pk = ?
                '''
        cls.__cursor.execute(query, (school_class_id, ))
        active_school_class = cls.__cursor.fetchone()
        return active_school_class != None

    @classmethod
    def get_school_class_details_by_id(cls, school_class_id):
        query = '''
                SELECT student_full_name
                FROM student
                INNER JOIN school_class
                ON student.school_class_fk = school_class.school_class_pk
                WHERE student.active = 1 AND school_class.active = 1 AND school_class_pk = ?
                '''
        cls.__cursor.execute(query, (school_class_id, ))
        active_students_in_school_class = cls.__cursor.fetchall()
        return active_students_in_school_class

    @classmethod
    def is_question_id_valid(cls, question_id):
        query = '''
            SELECT question_pk
            FROM question
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(query, (question_id, ))
        question_pk_tuple = cls.__cursor.fetchone()
        return question_pk_tuple != None

    @classmethod
    def set_exam_to_all_students_in_all_relevant_school_classes(cls, exam_pk, string_of_school_classes_ids):
        school_classes_ids_list = string_of_school_classes_ids.split(" ")
        students_ids_list = []
        for school_class_id in school_classes_ids_list:
            students_ids_in_school_class_string = cls.get_all_students_ids_in_school_class_by_id(school_class_id)
            if (students_ids_in_school_class_string != ""):
                students_ids_in_school_class = students_ids_in_school_class_string.split(" ")
                students_ids_list.extend(students_ids_in_school_class)
        for student_id in students_ids_list:
            if (student_id != ""):
                select_query = '''
                    SELECT not_completed_exams_ids
                    FROM student
                    WHERE student_pk = ?
                '''
                cls.__cursor.execute(select_query, (student_id, ))
                not_completed_exams_ids_string_tuple = cls.__cursor.fetchone()
                not_completed_exams_ids = not_completed_exams_ids_string_tuple[0]
                if (not_completed_exams_ids == None):
                    not_completed_exams_ids = ""
                not_completed_exams_ids = str(not_completed_exams_ids) + " " + str(exam_pk)
                update_query = '''
                    UPDATE student
                    SET not_completed_exams_ids = ?
                    WHERE student_pk = ?
                '''
                cls.__cursor.execute(update_query, (not_completed_exams_ids, student_id))
                cls.__db_connection.commit()

    @classmethod
    def get_all_students_ids_in_school_class_by_id(cls, school_class_id):
        query = '''
            SELECT student_pk
            FROM student
            INNER JOIN school_class
            ON school_class_fk = school_class_pk
            WHERE school_class_pk = ?
        '''
        cls.__cursor.execute(query, (school_class_id, ))
        students_ids_tuple = cls.__cursor.fetchall()
        students_ids = ""
        if (students_ids_tuple == None):
            return students_ids
        for (student_id,) in students_ids_tuple:
            students_ids = students_ids + str(student_id) + " "
        return students_ids

    @classmethod
    def insert_exam_result_to_db_by_exam_id(cls, exam_pk):
        query = '''
            INSERT INTO exam_result (
                exam_result_pk,
                is_result_released
                )
            VALUES (?, ?)
        '''
        cls.__cursor.execute(query, (exam_pk, False))
        cls.__db_connection.commit()

    @classmethod
    def insert_individual_student_exam_result_to_db_by_exam_id(cls, exam_pk):
        students_ids = cls.get_students_ids_in_exam_by_exam_id(exam_pk)
        for student_id in students_ids.split(" "):
            individual_student_exam_result_pk = cls.get_next_individual_student_exam_result_pk_from_db()
            query = '''
                INSERT INTO individual_student_exam_result (
                    individual_student_exam_result_pk,
                    student_id,
                    exam_id,
                    total_points_gained,
                    average_percentage_mark
                    )
                VALUES (?, ?, ?, ?, ?)
            '''
            cls.__cursor.execute(query, (individual_student_exam_result_pk, int(student_id), exam_pk, 0, 0.0))
            cls.__db_connection.commit()

    @classmethod
    def get_next_individual_student_exam_result_pk_from_db(cls):
        query = '''
            SELECT count(*)
            FROM individual_student_exam_result
        '''
        cls.__cursor.execute(query)
        total_number_of_individual_student_exam_result_tuple = cls.__cursor.fetchone()
        next_individual_student_exam_result_pk = total_number_of_individual_student_exam_result_tuple[0] + 1
        return next_individual_student_exam_result_pk

    @classmethod
    def get_students_ids_in_exam_by_exam_id(cls, exam_pk):
        query = '''
            SELECT students_ids
            FROM exam
            WHERE exam_pk = ?
        '''
        cls.__cursor.execute(query, (exam_pk, ))
        students_ids_tuple = cls.__cursor.fetchone()
        return students_ids_tuple[0].rstrip()



    def __str__(self):
        return ("This is TeacherDA Object")