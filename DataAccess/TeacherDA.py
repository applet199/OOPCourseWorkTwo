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
        total_number_of_questions = cls.get_total_number_of_questions_in_db()
        total_number_of_five_options_questions = cls.get_total_number_of_five_options_questions_in_db()
        question_body = five_options_question_details[0]
        option_A = five_options_question_details[1]
        option_B = five_options_question_details[2]
        option_C = five_options_question_details[3]
        option_D = five_options_question_details[4]
        option_E = five_options_question_details[5]
        year_level = five_options_question_details[6]
        phrase_tag = five_options_question_details[7]
        correct_ansewrs = five_options_question_details[8]
        insert_into_question_table_query = '''
                                           INSERT INTO question (
                                             question_pk,
                                             question_type,
                                             marking_type,
                                             points,
                                             year_level,
                                             question_tag
                                             )
                                           VALUES (?, ?, ?, ?, ?, ?)
                                           '''
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






    def __str__(self):
        return ("This is TeacherDA Object")