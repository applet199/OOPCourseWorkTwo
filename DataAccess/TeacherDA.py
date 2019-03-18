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
              correct_answer
              )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cls.__cursor.execute(insert_into_single_answer_question_table_query, (single_answer_question_pk, question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, correct_ansewr))
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
    def get_total_number_of_questions_in_db(cls):
        select_all_from_question_query = '''
            SELECT count(*)
            FROM question
        '''
        cls.__cursor.execute(select_all_from_question_query)
        total_number_of_questions = cls.__cursor.fetchone()
        return total_number_of_questions

    @classmethod
    def get_total_number_of_single_answer_questions_in_db(cls):
        select_all_from_single_answer_question_query = '''
        SELECT count(*)
        FROM single_answer_question
        '''
        cls.__cursor.execute(select_all_from_single_answer_question_query)
        total_number_of_single_answer_questions = cls.__cursor.fetchone()
        return total_number_of_single_answer_questions

    @classmethod
    def get_total_number_of_multiple_answers_questions_in_db(cls):
        select_all_from_multiple_answers_question_query = '''
        SELECT count(*)
        FROM multiple_answers_question
        '''
        cls.__cursor.execute(select_all_from_multiple_answers_question_query)
        total_number_of_multiple_answers_questions = cls.__cursor.fetchone()
        return total_number_of_multiple_answers_questions

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

    def __str__(self):
        return ("This is TeacherDA Object")