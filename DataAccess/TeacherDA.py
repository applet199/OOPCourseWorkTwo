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
    def insert_single_answer_question_into_db(cls, single_answer_question_details):
        total_number_of_questions_tuple = cls.get_total_number_of_questions_in_db()
        question_pk = total_number_of_questions_tuple[0] + 1

        total_number_of_single_answer_questions_tuple = cls.get_total_number_of_single_answer_questions_in_db()
        single_answer_question_pk = total_number_of_single_answer_questions_tuple[0] + 1

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
            VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)
        '''
        cls.__cursor.execute(insert_into_single_answer_question_table_query, (single_answer_question_pk, question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, correct_ansewr, question_pk))
        cls.__db_connection.commit()


    @classmethod
    def insert_multiple_answers_question_into_db(cls, multiple_answers_question_details):
        total_number_of_questions_tuple = cls.get_total_number_of_questions_in_db()
        question_pk = total_number_of_questions_tuple[0] + 1

        total_number_of_multiple_answers_questions_tuple = cls.get_total_number_of_multiple_answers_questions_in_db()
        multiple_answers_question_pk = total_number_of_multiple_answers_questions_tuple[0] + 1

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
              correct_answers
              )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cls.__cursor.execute(insert_into_multiple_answers_question_table_query, (multiple_answers_question_pk, question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, correct_ansewrs))
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
        total_number_of_multiple_answers_questions = cls.__cursor.fetchone()
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
            correct_answers_string = correct_answers_string + answer + " "
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



    def __str__(self):
        return ("This is TeacherDA Object")