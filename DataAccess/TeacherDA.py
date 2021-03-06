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
    def insert_exam_into_db(cls, exam_pk, questions_ids, school_classes_ids, exam_status, essay_questions_ids):
        total_available_points = cls.get_total_available_points_by_questions_ids(questions_ids)
        number_of_questions = len(questions_ids.split(" "))
        students_ids = cls.get_students_ids_in_exam_by_school_classes_ids(school_classes_ids)
        query = '''
            INSERT INTO exam (
              exam_pk,
              questions_ids,
              school_classes_ids,
              status,
              total_available_points,
              number_of_questions,
              students_ids,
              essay_questions_ids
              )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cls.__cursor.execute(query, (exam_pk, questions_ids, school_classes_ids, exam_status, total_available_points, number_of_questions, students_ids, essay_questions_ids))
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
            students_ids_in_exam = students_ids_in_exam + students_ids_in_school_class + " "
        return students_ids_in_exam.strip()

    @classmethod
    def get_school_classes_ids_in_exam_by_exam_id(cls, exam_pk):
        query = '''
            SELECT school_classes_ids
            FROM exam
            WHERE exam_pk = ?
        '''
        cls.__cursor.execute(query, (exam_pk,))
        school_classes_ids_tuple = cls.__cursor.fetchone()
        return school_classes_ids_tuple[0]

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
            WHERE status = ?
        '''
        cls.__cursor.execute(query, ("Not Completed", ))
        not_completed_exams_tuple = cls.__cursor.fetchall()
        return not_completed_exams_tuple

    @classmethod
    def get_ready_to_be_marked_exams_from_db(cls):
        query='''
            SELECT exam_pk
            FROM exam
            WHERE status = ?
        '''
        cls.__cursor.execute(query, ("Ready To Be Marked", ))
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
                not_completed_exams_ids.strip()
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
        return students_ids.rstrip()

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
                    average_percentage_mark,
                    status
                    )
                VALUES (?, ?, ?, ?, ?, ?)
            '''
            cls.__cursor.execute(query, (individual_student_exam_result_pk, int(student_id), exam_pk, 0, 0.0, "Not Completed"))
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
        students_ids = students_ids_tuple[0]
        return str(students_ids).strip()

    @classmethod
    def have_all_students_completed_this_exam(cls, exam_id):
        query = '''
            SELECT status
            FROM individual_student_exam_result
            WHERE exam_id = ?
        '''
        cls.__cursor.execute(query, (exam_id,))
        all_students_exam_statuses = cls.__cursor.fetchall()
        for (status, ) in all_students_exam_statuses:
            if (status == "Not Completed"):
                return False
        return True

    @classmethod
    def update_exam_status_to_ready_to_be_marked_by_exam_id(cls, exam_id):
        query = '''
            UPDATE exam
            SET status = ?
            WHERE exam_pk = ?
        '''
        cls.__cursor.execute(query, ("Ready To Be Marked", exam_id))
        cls.__db_connection.commit()

    @classmethod
    def does_student_have_questions_ready_to_be_marked_for_exam(cls, student_id, exam_id):
        query = '''
            SELECT essay_question_result_pk
            FROM essay_question_result
            WHERE student_id = ?
            AND exam_id = ?
            AND status = ?
        '''
        cls.__cursor.execute(query, (student_id, exam_id, "Ready To Be Marked"))
        essay_question_result_list = cls.__cursor.fetchall()
        return essay_question_result_list != []


    @classmethod
    def get_essay_questions_ids_string_from_questions_ids(cls, questions_ids):
        essay_questions_ids = []
        for question_id in questions_ids.split(" "):
            question_type = cls.get_question_type_by_id(question_id)
            if (question_type == "Essay"):
                essay_questions_ids.append(question_id)
        essay_questions_ids_string = cls.make_list_to_string(essay_questions_ids)
        return essay_questions_ids_string

    @classmethod
    def insert_essay_questions_results_in_to_db(cls, essay_questions_ids, students_ids, exam_id):
        if (essay_questions_ids == ""):
            return
        essay_questions_ids_list = essay_questions_ids.split(" ")
        students_ids_list = students_ids.split(" ")
        for student_id in students_ids_list:
            for essay_question_id in essay_questions_ids_list:
                query = '''
                    INSERT INTO essay_question_result (
                        essay_question_result_pk,
                        question_id,
                        exam_id,
                        student_id,
                        status
                        )
                    VALUES (?, ?, ?, ?, ?)
                '''
                essay_question_result_pk = cls.get_next_essay_question_result_pk()
                cls.__cursor.execute(query, (essay_question_result_pk, essay_question_id, exam_id, student_id, "Not Completed"))
                cls.__db_connection.commit()

    @classmethod
    def get_next_essay_question_result_pk(cls):
        query = '''
            SELECT count(*)
            FROM essay_question_result
        '''
        cls.__cursor.execute(query)
        total_number_of_essay_question_result_tuple = cls.__cursor.fetchone()
        total_number_of_essay_question_result = total_number_of_essay_question_result_tuple[0]
        return total_number_of_essay_question_result + 1

    @classmethod
    def make_list_to_string(cls, any_list):
        result_string = ""
        for item in any_list:
            result_string = result_string + str(item) + " "
        return result_string.strip()

    @classmethod
    def get_students_full_names_by_ids(cls, students_ids):
        students_full_names = []
        for student_id in students_ids:
            student_name = cls.get_student_full_name_by_id(student_id)
            students_full_names.append(student_name)
        return students_full_names

    @classmethod
    def get_student_full_name_by_id(cls, student_id):
        query = '''
            SELECT student_full_name
            FROM student
            WHERE student_pk = ?
        '''
        cls.__cursor.execute(query, (student_id, ))
        student_full_name_tuple = cls.__cursor.fetchone()
        student_full_name = student_full_name_tuple[0]
        return student_full_name

    @classmethod
    def get_student_id_by_name(cls, student_full_name):
        query = '''
            SELECT student_pk
            FROM student
            WHERE student_full_name = ?
        '''
        cls.__cursor.execute(query, (student_full_name, ))
        student_id_tuple = cls.__cursor.fetchone()
        student_id = student_id_tuple[0]
        return student_id

    @classmethod
    def get_questions_ready_to_be_marked_for_student_in_exam(cls, student_id, exam_id):
        query = '''
            SELECT question_id
            FROM essay_question_result
            WHERE student_id = ?
            AND exam_id = ?
            AND status = ?
        '''
        cls.__cursor.execute(query, (student_id, exam_id, "Ready To Be Marked"))
        questions_ids_tuple = cls.__cursor.fetchall()
        return questions_ids_tuple

    @classmethod
    def get_essay_question_details_to_mark_by_id(cls, question_id, exam_id, student_id):
        query = '''
            SELECT question_body,
                essay_question_answer,
                points
            FROM essay_question
            INNER JOIN essay_question_result
            ON essay_question.question_fk = essay_question_result.question_id
            INNER JOIN question
            ON essay_question.question_fk = question.question_pk
            WHERE essay_question_result.question_id = ?
            AND essay_question_result.exam_id = ?
            AND essay_question_result.student_id = ?
        '''
        cls.__cursor.execute(query, (question_id, exam_id, student_id))
        essay_questions_details_tuple = cls.__cursor.fetchone()
        return essay_questions_details_tuple

    @classmethod
    def update_essay_question_mark_in_db(cls, points, exam_id, student_id, question_id):
        query = '''
            UPDATE essay_question_result
            SET points_gained = ?,
                status = ?
            WHERE question_id = ?
            AND exam_id = ?
            AND student_id = ?
        '''
        cls.__cursor.execute(query, (points, "Marked", question_id, exam_id, student_id))
        cls.__db_connection.commit()

    @classmethod
    def update_exam_status_to_marked_by_id_in_db(cls, exam_id):
        query = '''
            UPDATE exam
            SET status = ?
            WHERE exam_pk = ?
        '''
        cls.__cursor.execute(query, ("Marked", exam_id))
        cls.__db_connection.commit()

    @classmethod
    def get_marked_exams_from_db(cls):
        query = '''
            SELECT exam_pk
            FROM exam
            WHERE status = ?
        '''
        cls.__cursor.execute(query, ("Marked", ))
        marked_exams_list = cls.__cursor.fetchall()
        return marked_exams_list

    @classmethod
    def update_exam_status_to_result_released_by_exam_id_in_db(cls, exam_id):
        query = '''
            UPDATE exam
            SET status = ?
            WHERE exam_pk = ?
        '''
        cls.__cursor.execute(query, ("Result Released", exam_id))
        cls.__db_connection.commit()

    @classmethod
    def get_result_released_exams_from_db(cls):
        query = '''
            SELECT exam_pk
            FROM exam
            WHERE status = ?
        '''
        cls.__cursor.execute(query, ("Result Released", ))
        result_released_exams = cls.__cursor.fetchall()
        return result_released_exams

    @classmethod
    def update_exam_result_to_released_by_exam_result_id_in_db(cls, exam_id):
        query = '''
            UPDATE exam_result
            SET is_result_released = ?
            WHERE exam_result_pk = ?
        '''
        cls.__cursor.execute(query, (1, exam_id))
        cls.__db_connection.commit()

    @classmethod
    def get_exam_results_from_db(cls):
        query = '''
            SELECT exam_result_pk
            FROM exam_result
            WHERE is_result_released = ?
        '''
        cls.__cursor.execute(query, (1, ))
        exam_results = cls.__cursor.fetchall()
        return exam_results

    @classmethod
    def get_students_full_names_by_school_class_id(cls, school_class_id):
        query = '''
            SELECT student_full_name
            FROM student
            WHERE school_class_fk = ?
        '''
        cls.__cursor.execute(query, (school_class_id, ))
        students_full_names_list = cls.__cursor.fetchall()
        return students_full_names_list

    @classmethod
    def get_student_exam_result_details_by_id(cls, student_full_name, exam_result_id):
        query = '''
            SELECT student_pk,
                student_full_name,
                date_of_birth,
                school_class_fk,
                exam_id,
                total_available_points,
                total_points_gained,
                average_percentage_mark
            FROM individual_student_exam_result
            INNER JOIN student
            ON individual_student_exam_result.student_id = student.student_pk
            INNER JOIN exam
            ON individual_student_exam_result.exam_id = exam.exam_pk
            WHERE student.student_full_name = ?
            AND exam.exam_pk = ?
        '''
        cls.__cursor.execute(query, (student_full_name, exam_result_id))
        exam_result_details_tuple = cls.__cursor.fetchone()
        return exam_result_details_tuple

    @classmethod
    def update_total_points_gained_for_each_student_in_exam(cls, students_ids, exam_id):
        students_ids_list = cls.make_string_to_list(students_ids)
        questions_ids = cls.get_questions_ids_in_exam(exam_id)
        questions_ids_list = cls.make_string_to_list(questions_ids)
        for student_id in students_ids_list:
            total_points_gained = 0
            for question_id in questions_ids_list:
                question_type = cls.get_question_type_by_id(question_id)
                points_gained_for_question = 0
                if (question_type == "Single Answer"):
                    points_gained_for_question = cls.get_points_gained_for_single_answser_question(exam_id, student_id, question_id)
                elif (question_type == "Multiple Answers"):
                    points_gained_for_question = cls.get_points_gained_for_multiple_answsers_question(exam_id, student_id, question_id)
                elif (question_type == "Essay"):
                    points_gained_for_question = cls.get_points_gained_for_essay_question(exam_id, student_id, question_id)
                total_points_gained = total_points_gained + points_gained_for_question
            cls.update_total_points_gained_for_student(student_id, total_points_gained, exam_id)

    @classmethod
    def update_average_percentage_mark_for_each_student_in_exam(cls, students_ids, exam_id):
        students_ids_list = cls.make_string_to_list(students_ids)
        for student_id in students_ids_list:
            total_available_points = cls.get_total_available_points_in_exam(exam_id)
            total_points_gained = cls.get_total_points_gained_for_student_in_exam(student_id, exam_id)
            average_percentage_mark = (total_points_gained / total_available_points) * 100
            query = '''
                UPDATE individual_student_exam_result
                SET average_percentage_mark = ?
                WHERE student_id = ?
                AND exam_id = ?
            '''
            cls.__cursor.execute(query, (average_percentage_mark, student_id, exam_id))
            cls.__db_connection.commit()

    @classmethod
    def get_total_points_gained_for_student_in_exam(cls, student_id, exam_id):
        query = '''
            SELECT total_points_gained
            FROM individual_student_exam_result
            WHERE exam_id = ?
            AND student_id = ?
        '''
        cls.__cursor.execute(query, (exam_id, student_id))
        total_points_gained_tuple = cls.__cursor.fetchone()
        return total_points_gained_tuple[0]

    @classmethod
    def get_total_available_points_in_exam(cls, exam_id):
        query = '''
            SELECT total_available_points
            FROM exam
            WHERE exam_pk = ?
        '''
        cls.__cursor.execute(query, (exam_id, ))
        total_available_points_tuple = cls.__cursor.fetchone()
        return total_available_points_tuple[0]



    @classmethod
    def update_total_points_gained_for_student(cls, student_id, total_points_gained, exam_id):
        query = '''
            UPDATE individual_student_exam_result
            SET total_points_gained = ?
            WHERE student_id = ?
            AND exam_id = ?
        '''
        cls.__cursor.execute(query, (total_points_gained, student_id, exam_id))
        cls.__db_connection.commit()



    @classmethod
    def get_questions_ids_in_exam(cls, exam_id):
        query = '''
            SELECT questions_ids
            FROM exam
            WHERE exam_pk = ?
        '''
        cls.__cursor.execute(query, (exam_id, ))
        questions_ids_tuple = cls.__cursor.fetchone()
        return questions_ids_tuple[0]

    @classmethod
    def get_points_gained_for_single_answser_question(cls, exam_id, student_id, question_id):
        query = '''
            SELECT points_gained
            FROM single_answer_question_result
            WHERE exam_id = ?
            AND student_id = ?
            AND question_id = ?
            AND status = ?
        '''
        cls.__cursor.execute(query, (exam_id, student_id, question_id, "Marked"))
        points_gained_tuple = cls.__cursor.fetchone()
        return points_gained_tuple[0]

    @classmethod
    def get_points_gained_for_multiple_answsers_question(cls, exam_id, student_id, question_id):
        query = '''
            SELECT points_gained
            FROM multiple_answers_question_result
            WHERE exam_id = ?
            AND student_id = ?
            AND question_id = ?
            And status= ?
        '''
        cls.__cursor.execute(query, (exam_id, student_id, question_id, "Marked"))
        points_gained_tuple = cls.__cursor.fetchone()
        return points_gained_tuple[0]

    @classmethod
    def get_points_gained_for_essay_question(cls, exam_id, student_id, question_id):
        query = '''
            SELECT points_gained
            FROM essay_question_result
            WHERE exam_id = ?
            AND student_id = ?
            AND question_id = ?
            AND status = ?
        '''
        cls.__cursor.execute(query, (exam_id, student_id, question_id, "Marked"))
        points_gained_tuple = cls.__cursor.fetchone()
        return points_gained_tuple[0]

    @classmethod
    def update_completed_exams_ids_for_students_in_db(cls, exam_id, students_ids):
        students_ids_list = cls.make_string_to_list(students_ids)
        for student_id in students_ids_list:
            new_completed_exams_ids = cls.get_updated_completed_exams_ids_by_deletion(exam_id, student_id)
            cls.update_completed_exams_ids_for_student(new_completed_exams_ids, student_id)

    @classmethod
    def make_string_to_list(cls, any_string):
        any_string = str(any_string)
        any_list = any_string.split(" ")
        return any_list

    @classmethod
    def update_exam_results_ids_for_students_in_db(cls, exam_id, students_ids):
        students_ids_list = cls.make_string_to_list(students_ids)
        for student_id in students_ids_list:
            new_exam_results_ids = cls.get_updated_exam_results_ids_by_addition(exam_id, student_id)
            cls.update_exam_results_ids_for_student(new_exam_results_ids, student_id)

    @classmethod
    def get_updated_completed_exams_ids_by_deletion(cls, exam_id, student_id):
        old_completed_exams_ids = cls.get_completed_exams_ids_for_student_from_db(student_id)
        old_completed_exams_ids_list = cls.make_string_to_list(old_completed_exams_ids)
        old_completed_exams_ids_list.remove(str(exam_id))
        new_completed_exams_ids = cls.make_list_to_string(old_completed_exams_ids_list)
        return new_completed_exams_ids

    @classmethod
    def get_completed_exams_ids_for_student_from_db(cls, student_id):
        query = '''
            SELECT completed_exams_ids
            FROM student
            WHERE student_pk = ?
        '''
        cls.__cursor.execute(query, (student_id, ))
        completed_exams_ids_tuple = cls.__cursor.fetchone()
        return completed_exams_ids_tuple[0]

    @classmethod
    def update_completed_exams_ids_for_student(cls, new_completed_exams_ids, student_id):
        query = '''
            UPDATE student
            SET completed_exams_ids = ?
            WHERE student_pk = ?
        '''
        cls.__cursor.execute(query, (new_completed_exams_ids, student_id))
        cls.__db_connection.commit()


    @classmethod
    def get_updated_exam_results_ids_by_addition(cls, exam_id, student_id):
        old_exam_results_ids = cls.get_exam_results_ids_for_student_from_db(student_id)
        old_exam_results_ids_list = cls.make_string_to_list(old_exam_results_ids)
        old_exam_results_ids_list.append(str(exam_id))
        new_exam_results_ids = cls.make_list_to_string(old_exam_results_ids_list)
        return new_exam_results_ids

    @classmethod
    def get_exam_results_ids_for_student_from_db(cls, student_id):
        query = '''
            SELECT exam_results_ids
            FROM student
            WHERE student_pk = ?
        '''
        cls.__cursor.execute(query, (student_id, ))
        exam_results_ids_tuple = cls.__cursor.fetchone()
        exam_results_ids = exam_results_ids_tuple[0]
        if (exam_results_ids == None):
            return ""
        return exam_results_ids

    @classmethod
    def update_exam_results_ids_for_student(cls, new_exam_results_ids, student_id):
        query = '''
            UPDATE student
            SET exam_results_ids = ?
            WHERE student_pk = ?
        '''
        cls.__cursor.execute(query, (new_exam_results_ids, student_id))
        cls.__db_connection.commit()


    @classmethod
    def is_exam_result_released_by_exam_id(cls, exam_result_pk):
        query = '''
            SELECT exam_result_pk
            FROM exam_result
            WHERE is_result_released = ?
            AND exam_result_pk = ?
        '''
        cls.__cursor.execute(query, (1, exam_result_pk))
        exam_result_id_tuple = cls.__cursor.fetchone()
        if (exam_result_id_tuple == None):
            return False
        exam_result_id = exam_result_id_tuple[0]
        if (exam_result_id == None):
            return False
        return True

    @classmethod
    def is_school_class_id_in_exam(cls, school_class_id, exam_id):
        school_classes_ids = cls.get_school_classes_ids_in_exam_by_exam_id(exam_id)
        school_classes_ids_list = cls.make_string_to_list(school_classes_ids)
        return (school_classes_ids_list.count(str(school_class_id)) == 1)

    @classmethod
    def update_individual_student_exam_result_status_to_result_released_for_all_students_in_exam_in_db(cls, exam_id):
        query = '''
            UPDATE individual_student_exam_result
            SET status = ?
            WHERE exam_id = ?
        '''
        cls.__cursor.execute(query, ("Result Released", exam_id))
        cls.__db_connection.commit()

    def __str__(self):
        return ("This is TeacherDA Object")