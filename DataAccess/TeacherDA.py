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
    def insert_five_options_question_into_db(cls, five_options_question_details):
        total_number_of_questions_tuple = cls.get_total_number_of_questions_in_db()
        question_pk = total_number_of_questions_tuple[0] + 1

        total_number_of_five_options_questions_tuple = cls.get_total_number_of_five_options_questions_in_db()
        five_options_question_pk = total_number_of_five_options_questions_tuple[0] + 1

        question_body = five_options_question_details[0]
        option_A_text = five_options_question_details[1]
        option_B_text = five_options_question_details[2]
        option_C_text = five_options_question_details[3]
        option_D_text = five_options_question_details[4]
        option_E_text = five_options_question_details[5]
        year_level = int(five_options_question_details[6])
        question_tag = five_options_question_details[7]
        correct_ansewrs = cls.get_correct_answers_string_for_five_options_question(five_options_question_details[8])
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
        cls.__cursor.execute(insert_into_question_table_query, (question_pk, "Five Options", 10, year_level, question_tag))
        cls.__db_connection.commit()
        insert_into_five_options_question_table_query = '''
            INSERT INTO five_options_question (
              five_options_question_pk,
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
        cls.__cursor.execute(insert_into_five_options_question_table_query, (five_options_question_pk, question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, correct_ansewrs))
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
    def get_total_number_of_five_options_questions_in_db(cls):
        select_all_from_five_options_question_query = '''
        SELECT count(*)
        FROM five_options_question
        '''
        cls.__cursor.execute(select_all_from_five_options_question_query)
        total_number_of_five_options_questions = cls.__cursor.fetchone()
        return total_number_of_five_options_questions

    @classmethod
    def get_correct_answers_string_for_five_options_question(cls, correct_answers_list):
        correct_answers_string = ""
        for answer in correct_answers_list:
            correct_answers_string = correct_answers_string + answer + " "
        return correct_answers_string

    @classmethod
    def get_all_active_questions_from_db(cls):
        pass

    def __str__(self):
        return ("This is TeacherDA Object")