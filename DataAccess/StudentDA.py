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
    def get_not_completed_exams_ids_for_current_student(cls):
        query = '''
            SELECT not_completed_exams_ids
            FROM student
            WHERE student_pk = ?
        '''
        cls.__cursor.execute(query, (cls.__student_id,))
        not_completed_exams_ids_tuple = cls.__cursor.fetchone()
        not_completed_exams_ids = not_completed_exams_ids_tuple[0]
        return not_completed_exams_ids

    @classmethod
    def get_completed_exams_ids_for_current_student(cls):
        query = '''
            SELECT completed_exams_ids
            FROM student
            WHERE student_pk = ?
        '''
        cls.__cursor.execute(query, (cls.__student_id,))
        completed_exams_ids_tuple = cls.__cursor.fetchone()
        completed_exams_ids = completed_exams_ids_tuple[0]
        return completed_exams_ids

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
    def get_number_of_questions_in_exam_by_id(cls, exam_id):
        query = '''
            SELECT number_of_questions
            FROM exam
            WHERE exam_pk = ?

        '''
        cls.__cursor.execute(query, (exam_id, ))
        number_of_questions_tuple = cls.__cursor.fetchone()
        number_of_questions = number_of_questions_tuple[0]
        return number_of_questions


    @classmethod
    def get_questions_ids_of_exam_by_id(cls, exam_id):
        query = '''
            SELECT questions_ids
            FROM exam
            WHERE exam_pk = ?
        '''
        cls.__cursor.execute(query, (exam_id, ))
        questions_ids_tuple = cls.__cursor.fetchone()
        questions_ids = questions_ids_tuple[0]
        return (str(questions_ids)).rstrip()

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
            INNER JOIN single_answer_question ON question_pk = question_fk
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(select_single_answer_question_details_query, (question_pk, ))
        question_details_tuple = cls.__cursor.fetchall()
        question_details = question_details_tuple[0]
        return question_details

    @classmethod
    def get_multiple_answers_question_details_by_id(cls, question_pk):
        query = '''
            SELECT question_pk,
                points,
                question_body,
                option_A_text,
                option_B_text,
                option_C_text,
                option_D_text,
                option_E_text,
                correct_answers
            FROM question
            INNER JOIN multiple_answers_question ON question_pk = question_fk
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(query, (question_pk, ))
        question_details_tuple = cls.__cursor.fetchall()
        question_details = question_details_tuple[0]
        return question_details

    @classmethod
    def get_essay_question_details_by_id(cls, question_pk):
        query = '''
            SELECT question_pk,
                points,
                question_body
            FROM question
            INNER JOIN essay_question
            ON question_pk = question_fk
            WHERE question_pk = ?
        '''
        cls.__cursor.execute(query, (question_pk,))
        question_details_tuple = cls.__cursor.fetchone()
        return question_details_tuple

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
        is_correct = student_answer == correct_answer
        return is_correct

    @classmethod
    def are_multiple_answers_correct_by_question_id(cls, question_pk, student_answers):
        query = '''
            SELECT correct_answers
            FROM multiple_answers_question
            WHERE question_fk = ?
        '''
        cls.__cursor.execute(query, (question_pk, ))
        correct_answers_tuple = cls.__cursor.fetchone()
        correct_answers = correct_answers_tuple[0]
        student_answers = student_answers.rstrip()
        is_correct = student_answers == correct_answers
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
    def insert_single_answer_question_result_to_db(cls, question_pk, student_answer, exam_pk, student_pk, points_gained, status):
        single_answer_question_result_pk = cls.get_next_single_answer_question_result_pk()
        query = '''
            INSERT INTO single_answer_question_result (
                single_answer_question_result_pk,
                question_id,
                single_answer_question_answer,
                exam_id,
                student_id,
                points_gained,
                status
                )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        cls.__cursor.execute(query, (single_answer_question_result_pk, question_pk, student_answer, exam_pk, student_pk, points_gained, status))
        cls.__db_connection.commit()

    @classmethod
    def insert_multiple_answers_question_result_to_db(cls, question_pk, student_answers, exam_pk, student_pk, points_gained, status):
        multiple_answers_question_result_pk = cls.get_next_multiple_answers_question_result_pk()
        query = '''
            INSERT INTO multiple_answers_question_result (
                multiple_answers_question_result_pk,
                question_id,
                multiple_answers_question_answer,
                exam_id,
                student_id,
                points_gained,
                status
                )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        cls.__cursor.execute(query, (multiple_answers_question_result_pk, question_pk, student_answers, exam_pk, student_pk, points_gained, status))
        cls.__db_connection.commit()

    @classmethod
    def update_essay_question_result_in_db(cls, question_pk, student_answer, exam_pk, student_pk, points_gained, status):
        query = '''
            UPDATE essay_question_result
            SET essay_question_answer = ?,
                points_gained = ?,
                status = ?
            WHERE question_id = ?
            AND exam_id = ?
            AND student_id = ?
        '''
        cls.__cursor.execute(query, (student_answer, points_gained, status, question_pk, exam_pk, student_pk))
        cls.__db_connection.commit()

    @classmethod
    def get_next_single_answer_question_result_pk(cls):
        query = '''
            SELECT count(*)
            FROM single_answer_question_result
        '''
        cls.__cursor.execute(query)
        total_number_of_single_answer_question_result_tuple = cls.__cursor.fetchone()
        total_number_of_single_answer_question_result = total_number_of_single_answer_question_result_tuple[0]
        return total_number_of_single_answer_question_result + 1

    @classmethod
    def get_next_multiple_answers_question_result_pk(cls):
        query = '''
            SELECT count(*)
            FROM multiple_answers_question_result
        '''
        cls.__cursor.execute(query)
        total_number_of_multiple_answers_question_result_tuple = cls.__cursor.fetchone()
        total_number_of_multiple_answers_question_result = total_number_of_multiple_answers_question_result_tuple[0]
        return total_number_of_multiple_answers_question_result + 1

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
    def get_completed_questions_ids_in_current_exam_for_current_student(cls, questions_ids, exam_pk, student_pk):
        completed_questions_ids = ""
        questions_ids_list = []
        try:
            questions_ids_list = questions_ids.split(" ")
        except:
            questions_ids_list.append(questions_ids)
        for question_id in questions_ids_list:
            question_type = cls.get_question_type_by_id(question_id)
            is_question_completed = cls.is_question_completed_for_current_student(question_id, exam_pk, student_pk, question_type)
            if (is_question_completed):
                completed_questions_ids = completed_questions_ids + str(question_id) + " "
        return completed_questions_ids.rstrip()

    @classmethod
    def get_not_completed_questions_ids_in_current_exam_for_current_student(cls, questions_ids, exam_pk, student_pk):
        not_completed_questions_ids = ""
        questions_ids_list = []
        try:
            questions_ids_list = questions_ids.split(" ")
        except:
            questions_ids_list.append(questions_ids)
        for question_id in questions_ids_list:
            question_type = cls.get_question_type_by_id(question_id)
            is_question_completed = cls.is_question_completed_for_current_student(question_id, exam_pk, student_pk, question_type)
            if (not is_question_completed):
                not_completed_questions_ids = not_completed_questions_ids + str(question_id) + " "
        return not_completed_questions_ids.rstrip()

    @classmethod
    def is_question_completed_for_current_student(cls, question_id, exam_id, student_id, question_type):
        if (question_type == "Single Answer"):
            return cls.is_single_answer_question_completed_for_current_student(question_id, exam_id, student_id)
        elif (question_type == "Multiple Answers"):
            return cls.is_multiple_answers_question_completed_for_current_student(question_id, exam_id, student_id)
        elif (question_type == "Essay"):
            return cls.is_essay_question_completed_for_current_student(question_id, exam_id, student_id)

    @classmethod
    def is_single_answer_question_completed_for_current_student(cls, question_id, exam_id, student_id):
        query = '''
            SELECT single_answer_question_result_pk
            FROM single_answer_question_result
            WHERE question_id = ?
            AND exam_id = ?
            AND student_id = ?
            AND status = ?
        '''
        cls.__cursor.execute(query, (question_id, exam_id, student_id, "Completed"))
        single_answer_question_result_pk_tuple = cls.__cursor.fetchone()
        return single_answer_question_result_pk_tuple != None

    @classmethod
    def is_multiple_answers_question_completed_for_current_student(cls, question_id, exam_id, student_id):
        query = '''
            SELECT multiple_answers_question_result_pk
            FROM multiple_answers_question_result
            WHERE question_id = ?
            AND exam_id = ?
            AND student_id = ?
            AND status = ?
        '''
        cls.__cursor.execute(query, (question_id, exam_id, student_id, "Completed"))
        multiple_answers_question_result_pk_tuple = cls.__cursor.fetchone()
        return multiple_answers_question_result_pk_tuple != None

    @classmethod
    def is_essay_question_completed_for_current_student(cls, question_id, exam_id, student_id):
        query = '''
            SELECT essay_question_result_pk
            FROM essay_question_result
            WHERE question_id = ?
            AND exam_id = ?
            AND student_id = ?
            AND status = ?
        '''
        cls.__cursor.execute(query, (question_id, exam_id, student_id, "Completed"))
        essay_question_result_pk_tuple = cls.__cursor.fetchone()
        return essay_question_result_pk_tuple != None

    @classmethod
    def update_exam_status_to_completed_for_current_student_in_db(cls, exam_id, student_id):
        query = '''
            UPDATE individual_student_exam_result
            SET status = ?
            WHERE exam_id = ?
            AND student_id = ?
        '''
        cls.__cursor.execute(query, ("Completed", exam_id, student_id))
        cls.__db_connection.commit()

    @classmethod
    def update_not_completed_exams_ids_for_student_in_db(cls, exam_id, student_id):
        not_completed_exams_string = cls.get_not_completed_exams_ids_for_student(student_id)
        not_completed_exams_list = []
        try:
            not_completed_exams_list = not_completed_exams_string.split(" ")
        except:
            not_completed_exams_list.append(str(not_completed_exams_string))
        try:
            not_completed_exams_list.remove(str(exam_id))
        except:
            pass
        new_not_completed_exams_string = cls.make_list_to_string(not_completed_exams_list)
        cls.update_not_completed_exams_ids_string_for_student(new_not_completed_exams_string)

    @classmethod
    def update_completed_exams_ids_for_student_in_db(cls, exam_id, student_id):
        completed_exams_string = cls.get_completed_exams_ids_for_student(student_id)
        completed_exams_list = []
        if (completed_exams_string == ""):
            completed_exams_list.append(str(exam_id))
        else:
            try:
                completed_exams_list = completed_exams_string.split(" ")
                completed_exams_list.append(completed_exams_string)
            except:
                pass
        new_completed_exams_string = cls.make_list_to_string(completed_exams_list)
        cls.update_completed_exams_ids_string_for_student(new_completed_exams_string)

    @classmethod
    def get_not_completed_exams_ids_for_student(cls, student_id):
        query = '''
            SELECT not_completed_exams_ids
            FROM student
            WHERE student_pk = ?
        '''
        cls.__cursor.execute(query, (student_id, ))
        not_completed_exams_ids_tuple = cls.__cursor.fetchone()
        not_completed_exams_ids = not_completed_exams_ids_tuple[0]
        if (not_completed_exams_ids == None):
            return ""
        return not_completed_exams_ids

    @classmethod
    def get_completed_exams_ids_for_student(cls, student_id):
        query = '''
            SELECT completed_exams_ids
            FROM student
            WHERE student_pk = ?
        '''
        cls.__cursor.execute(query, (student_id, ))
        completed_exams_ids_tuple = cls.__cursor.fetchone()
        completed_exams_ids = completed_exams_ids_tuple[0]
        if (completed_exams_ids == None):
            return ""
        return completed_exams_ids

    @classmethod
    def make_list_to_string(cls, any_list):
        result_string = ""
        for list_item in any_list:
            result_string = result_string + str(list_item) + " "
        result_string = result_string.rstrip()
        return result_string

    @classmethod
    def update_not_completed_exams_ids_string_for_student(cls, not_completed_exams_string):
        query = '''
            UPDATE student
            SET not_completed_exams_ids = ?
            WHERE student_pk = ?
        '''
        cls.__cursor.execute(query, (not_completed_exams_string, cls.__student_id))
        cls.__db_connection.commit()

    @classmethod
    def update_completed_exams_ids_string_for_student(cls, completed_exams_string):
        query = '''
            UPDATE student
            SET completed_exams_ids = ?
            WHERE student_pk = ?
        '''
        cls.__cursor.execute(query, (completed_exams_string, cls.__student_id))
        cls.__db_connection.commit()

    @classmethod
    def are_essay_questions_ready_to_be_marked_in_exam(cls, exam_id):
        essay_questions_ids_string = cls.get_essay_questions_ids_in_exam(exam_id)
        essay_questions_ids_list = cls.make_string_to_list(essay_questions_ids_string)
        students_ids_string = cls.get_all_students_of_exam_by_id(exam_id)
        students_ids_list = cls.make_string_to_list(students_ids_string)
        for essay_question_id in essay_questions_ids_list:
            for student_id in students_ids_list:
                essay_question_status = cls.get_essay_question_status_for_student_in_exam_by_id(essay_question_id, student_id, exam_id)
                if (essay_question_status == "Not Completed"):
                    return False
        return True

    @classmethod
    def update_essay_questions_status_to_ready_to_be_marked_in_exam_in_db(cls, exam_id):
        essay_questions_ids_string = cls.get_essay_questions_ids_in_exam(exam_id)
        essay_questions_ids_list = cls.make_string_to_list(essay_questions_ids_string)
        students_ids_string = cls.get_all_students_of_exam_by_id(exam_id)
        students_ids_list = cls.make_string_to_list(students_ids_string)
        for essay_question_id in essay_questions_ids_list:
            for student_id in students_ids_list:
                cls.update_essay_question_status_to_ready_to_be_marked_for_student_in_exam_by_id(essay_question_id, student_id, exam_id)

    @classmethod
    def get_essay_question_status_for_student_in_exam_by_id(cls, question_id, student_id, exam_id):
        query = '''
            SELECT status
            FROM essay_question_result
            WHERE question_id = ?
            AND student_id = ?
            AND exam_id = ?
        '''
        cls.__cursor.execute(query, (question_id, student_id, exam_id))
        status_tuple = cls.__cursor.fetchone()
        status = status_tuple[0]
        return status

    @classmethod
    def update_essay_question_status_to_ready_to_be_marked_for_student_in_exam_by_id(cls, question_id, student_id, exam_id):
        query = '''
            UPDATE essay_question_result
            SET status = ?
            WHERE question_id = ?
            AND student_id = ?
            AND exam_id = ?
        '''
        cls.__cursor.execute(query, ("Ready To Be Marked", question_id, student_id, exam_id))
        cls.__db_connection.commit()

    @classmethod
    def get_essay_questions_ids_in_exam(cls, exam_id):
        query = '''
            SELECT essay_questions_ids
            FROM exam
            WHERE exam_pk = ?
        '''
        cls.__cursor.execute(query, (exam_id, ))
        essay_questions_ids_tuple = cls.__cursor.fetchone()
        essay_questions_ids = essay_questions_ids_tuple[0]
        return essay_questions_ids

    @classmethod
    def make_string_to_list(cls, any_string):
        any_string = str(any_string)
        any_string.strip()
        any_list = any_string.split(" ")
        return any_list

    def __str__(self):
        return ("This is StudentDA Object")