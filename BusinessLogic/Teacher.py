from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QDialog

from OOPCourseWorkTwo.DataAccess.TeacherDA import TeacherDA

from OOPCourseWorkTwo.GUI.TeacherGUI import TeacherGUI

class Teacher():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, connection, ui_mainwindow, mainwindow):
        cls.__ui_mainwindow = ui_mainwindow
        cls.__mainwindow = mainwindow
        TeacherDA.setup(connection)
        TeacherGUI.setup(ui_mainwindow)

    @classmethod
    def display_saved_questions(cls):
        all_active_questions = TeacherDA.get_all_active_questions_from_db()
        TeacherGUI.display_all_active_questions(all_active_questions)

    @classmethod
    def display_saved_school_classes(cls):
        all_active_school_classes = TeacherDA.get_all_active_school_classes_from_db()
        TeacherGUI.display_all_active_school_classes(all_active_school_classes)

    @classmethod
    def display_saved_exams(cls):
        all_exams = TeacherDA.get_all_exams_from_db()
        TeacherGUI.display_all_exams(all_exams)

    @classmethod
    def display_not_completed_exams(cls):
        not_completed_exams = TeacherDA.get_not_completed_exams_from_db()
        TeacherGUI.display_not_completed_exams(not_completed_exams)

    @classmethod
    def display_ready_to_be_marked_exams(cls):
        ready_to_be_marked_exams = TeacherDA.get_ready_to_be_marked_exams_from_db()
        TeacherGUI.display_ready_to_be_marked_exams(ready_to_be_marked_exams)

    @classmethod
    def display_marked_exams(cls):
        marked_exams = TeacherDA.get_marked_exams_from_db()
        TeacherGUI.display_marked_exams(marked_exams)

    @classmethod
    def display_exam_results(cls):
        exam_results = TeacherDA.get_exam_results_from_db()
        TeacherGUI.display_exam_results(exam_results)

    @classmethod
    def actions(cls):
        cls.create_single_answer_question_button_pressed()
        cls.preview_single_answer_question_button_pressed()
        cls.create_multiple_answers_question_button_pressed()
        cls.preview_multiple_answers_question_button_pressed()
        cls.create_essay_question_button_pressed()
        cls.preview_essay_question_button_pressed()
        cls.load_question_details_by_id_button_pressed()
        cls.modify_question_button_pressed()
        cls.view_students_in_school_class_by_id_button_pressed()
        cls.add_question_to_exam_by_id_button_pressed()
        cls.remove_question_from_exam_by_id_button_pressed()
        cls.add_school_class_to_exam_by_id_button_pressed()
        cls.remove_school_class_from_exam_by_id_button_pressed()
        cls.create_exam_button_pressed()
        cls.view_exam_details_by_id_button_pressed()
        cls.mark_exam_button_pressed()
        cls.mark_student_questions_answers_button_pressed()
        cls.mark_question_button_pressed()
        cls.release_exam_result_button_pressed()
        cls.load_exam_result_details_by_id_button_pressed()
        cls.view_school_class_exam_result_by_id_button_pressed()
        cls.view_individual_student_exam_result_by_student_full_name_button_pressed()
        cls.close_button_pressed()

    @classmethod
    def create_single_answer_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton.clicked.connect(cls.create_single_answer_question)

    @classmethod
    def preview_single_answer_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_5.clicked.connect(cls.preview_single_answer_question)

    @classmethod
    def create_multiple_answers_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_7.clicked.connect(cls.create_multiple_answers_question)

    @classmethod
    def preview_multiple_answers_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_6.clicked.connect(cls.preview_multiple_answers_question)

    @classmethod
    def create_essay_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_28.clicked.connect(cls.create_essay_question)

    @classmethod
    def preview_essay_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_29.clicked.connect(cls.preview_essay_question)

    @classmethod
    def load_question_details_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_8.clicked.connect(cls.load_question_details_by_id)

    @classmethod
    def modify_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_9.clicked.connect(cls.modify_question)

    @classmethod
    def view_students_in_school_class_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_30.clicked.connect(cls.view_students_in_school_class_by_id)

    @classmethod
    def add_question_to_exam_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_10.clicked.connect(cls.add_question_to_exam_by_id)

    @classmethod
    def remove_question_from_exam_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_12.clicked.connect(cls.remove_question_from_exam_by_id)

    @classmethod
    def add_school_class_to_exam_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_11.clicked.connect(cls.add_school_class_to_exam_by_id)

    @classmethod
    def remove_school_class_from_exam_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_13.clicked.connect(cls.remove_school_class_from_exam_by_id)

    @classmethod
    def create_exam_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_14.clicked.connect(cls.create_exam)

    @classmethod
    def view_exam_details_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_15.clicked.connect(cls.view_exam_details_by_id)

    @classmethod
    def mark_exam_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_31.clicked.connect(cls.mark_exam)

    @classmethod
    def mark_student_questions_answers_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_33.clicked.connect(cls.mark_student_questions_answers)

    @classmethod
    def mark_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_34.clicked.connect(cls.mark_question)

    @classmethod
    def close_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_4.clicked.connect(cls.close_application)

    @classmethod
    def release_exam_result_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_32.clicked.connect(cls.release_exam_result)

    @classmethod
    def load_exam_result_details_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_24.clicked.connect(cls.load_exam_details)

    @classmethod
    def view_school_class_exam_result_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_25.clicked.connect(cls.view_school_class_exam_result)

    @classmethod
    def view_individual_student_exam_result_by_student_full_name_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_26.clicked.connect(cls.view_individual_student_exam_result)


    @classmethod
    def create_single_answer_question(cls):
        single_answer_question_details = TeacherGUI.get_single_answer_question_details()
        if (single_answer_question_details == None):
            TeacherGUI.display_invalid_single_answer_question_creation_message()
            return
        TeacherDA.insert_single_answer_question_into_db(single_answer_question_details)
        all_active_questions = TeacherDA.get_all_active_questions_from_db()
        TeacherGUI.display_all_active_questions(all_active_questions)
        TeacherGUI.display_create_single_answer_question_success()
        TeacherGUI.refresh_create_single_answer_question_page()

    @classmethod
    def preview_single_answer_question(cls):
        TeacherGUI.display_single_answer_question_dialog_preview()

    @classmethod
    def create_multiple_answers_question(cls):
        multiple_answers_question_details = TeacherGUI.get_multiple_answers_question_details()
        if (multiple_answers_question_details == None):
            TeacherGUI.display_invalid_multiple_answers_question_creation_message()
            return
        TeacherDA.insert_multiple_answers_question_into_db(multiple_answers_question_details)
        all_active_questions = TeacherDA.get_all_active_questions_from_db()
        TeacherGUI.display_all_active_questions(all_active_questions)
        TeacherGUI.display_create_multiple_answers_question_success()
        TeacherGUI.refresh_create_multiple_answers_question_page()

    @classmethod
    def preview_multiple_answers_question(cls):
        TeacherGUI.display_multiple_answers_question_dialog_preview()

    @classmethod
    def create_essay_question(cls):
        essay_question_details = TeacherGUI.get_essay_question_details()
        if (essay_question_details == None):
            TeacherGUI.display_invalid_essay_question_creation_message()
            return
        TeacherDA.insert_essay_question_into_db(essay_question_details)
        all_active_questions = TeacherDA.get_all_active_questions_from_db()
        TeacherGUI.display_all_active_questions(all_active_questions)
        TeacherGUI.display_create_essay_question_success()
        TeacherGUI.refresh_create_essay_question_page()

    @classmethod
    def preview_essay_question(cls):
        TeacherGUI.display_essay_question_dialog_preview()

    @classmethod
    def load_question_details_by_id(cls):
        question_id = TeacherGUI.get_question_id_to_load()
        is_question_id_valid = cls.is_question_id_valid(question_id)
        if (not is_question_id_valid):
            TeacherGUI.display_question_id_invalid_to_load_message()
            return
        question_type = TeacherDA.get_question_type_by_id(question_id)

        TeacherGUI.refresh_view_or_modify_question_page()

        if (question_type == "Single Answer"):
            single_answer_question_details = TeacherDA.get_single_answer_question_details_by_id(question_id)
            TeacherGUI.load_single_answer_question_details(single_answer_question_details)

        elif (question_type == "Multiple Answers"):
            multiple_answers_question_details = TeacherDA.get_multiple_answers_question_details_by_id(question_id)
            TeacherGUI.load_multiple_answers_question_details(multiple_answers_question_details)

        elif (question_type == "Essay"):
            essay_question_details = TeacherDA.get_essay_question_details_by_id(question_id)
            TeacherGUI.load_essay_question_details(essay_question_details)

    @classmethod
    def modify_question(cls):
        question_type = TeacherGUI.get_question_type_to_modify()
        if (question_type == "Single Answer"):
            single_answer_question_details = TeacherGUI.get_single_answer_question_details_to_modify()
            if (single_answer_question_details == None):
                TeacherGUI.display_invalid_modification_message()
                return
            TeacherDA.update_single_answer_question_details_in_db(single_answer_question_details)
            TeacherGUI.refresh_view_or_modify_question_page()
            TeacherGUI.display_modification_success_message()
        elif (question_type == "Multiple Answers"):
            multiple_answers_question_details = TeacherGUI.get_multiple_answers_question_details_to_modify()
            if (multiple_answers_question_details == None):
                TeacherGUI.display_invalid_modification_message()
                return
            TeacherDA.update_multiple_answers_question_details_in_db(multiple_answers_question_details)
            TeacherGUI.refresh_view_or_modify_question_page()
            TeacherGUI.display_modification_success_message()
        elif (question_type == "Essay"):
            essay_question_details = TeacherGUI.get_essay_question_details_to_modify()
            if (essay_question_details == None):
                TeacherGUI.display_invalid_modification_message()
                return
            TeacherDA.update_essay_question_details_in_db(essay_question_details)
            TeacherGUI.refresh_view_or_modify_question_page()
            TeacherGUI.display_modification_success_message()
        else:
            TeacherGUI.display_invalid_modification_message()

    @classmethod
    def view_students_in_school_class_by_id(cls):
        school_class_id = TeacherGUI.get_school_class_id_to_view_students()
        school_class_id_valid = TeacherDA.is_school_class_id_valid(school_class_id)
        if (not school_class_id_valid):
            TeacherGUI.display_invalid_school_class_id_message()
            return
        school_class_details = TeacherDA.get_school_class_details_by_id(school_class_id)
        TeacherGUI.display_school_class_details(school_class_details)
        TeacherGUI.refresh_view_school_class_details_page()


    @classmethod
    def is_question_id_valid(cls, question_id):
        if (question_id == None):
            return False
        if (question_id < 1):
            return False
        total_number_of_questions_in_db = TeacherDA.get_total_number_of_questions_in_db()
        if (question_id > total_number_of_questions_in_db):
            return False
        return True

    @classmethod
    def add_question_to_exam_by_id(cls):
        number_of_questions_in_current_exam = TeacherGUI.get_number_of_questions_in_current_exam()
        if (number_of_questions_in_current_exam == 10):
            TeacherGUI.display_number_of_questions_full_in_current_exam_message()
            return
        question_id = TeacherGUI.get_question_id_to_add_to_exam()
        question_id_valid = TeacherDA.is_question_id_valid(question_id)
        if (not question_id_valid):
            TeacherGUI.display_question_id_invalid_message()
            return
        question_id_already_added_to_current_exam = TeacherGUI.is_question_id_already_added_to_current_exam(question_id)
        if (question_id_already_added_to_current_exam):
            TeacherGUI.display_question_id_already_added_to_current_exam_message()
            return
        TeacherGUI.add_question_id_to_current_exam(question_id)

    @classmethod
    def remove_question_from_exam_by_id(cls):
        number_of_questions_in_current_exam = TeacherGUI.get_number_of_questions_in_current_exam()
        if (number_of_questions_in_current_exam == 0):
            TeacherGUI.display_no_question_in_current_exam_message()
            return
        question_id = TeacherGUI.get_question_id_to_remove_from_exam()
        question_id_valid = TeacherDA.is_question_id_valid(question_id)
        if (not question_id_valid):
            TeacherGUI.display_question_id_invalid_message()
            return
        question_id_already_added_to_current_exam = TeacherGUI.is_question_id_already_added_to_current_exam(question_id)
        if (not question_id_already_added_to_current_exam):
            TeacherGUI.display_question_id_not_already_in_current_exam_message()
            return
        TeacherGUI.remove_question_id_from_current_exam(question_id)

    @classmethod
    def add_school_class_to_exam_by_id(cls):
        number_of_school_classes_in_current_exam = TeacherGUI.get_number_of_school_classes_in_current_exam()
        if (number_of_school_classes_in_current_exam == 5):
            TeacherGUI.display_number_of_school_classes_full_in_current_exam_message()
            return
        school_class_id = TeacherGUI.get_school_class_id_to_add_to_exam()
        school_class_id_valid = TeacherDA.is_school_class_id_valid(school_class_id)
        if (not school_class_id_valid):
            TeacherGUI.display_school_class_id_invalid_message()
            return
        school_class_id_already_added_to_current_exam = TeacherGUI.is_school_class_id_already_added_to_current_exam(school_class_id)
        if (school_class_id_already_added_to_current_exam):
            TeacherGUI.display_school_class_id_already_added_to_current_exam_message()
            return
        TeacherGUI.add_school_class_id_to_current_exam(school_class_id)

    @classmethod
    def remove_school_class_from_exam_by_id(cls):
        number_of_school_classes_in_current_exam = TeacherGUI.get_number_of_school_classes_in_current_exam()
        if (number_of_school_classes_in_current_exam == 0):
            TeacherGUI.display_no_school_class_in_current_exam_message()
            return
        school_class_id = TeacherGUI.get_school_class_id_to_remove_from_exam()
        school_class_id_valid = TeacherDA.is_school_class_id_valid(school_class_id)
        if (not school_class_id_valid):
            TeacherGUI.display_school_class_id_invalid_message()
            return
        school_class_id_already_added_to_current_exam = TeacherGUI.is_school_class_id_already_added_to_current_exam(school_class_id)
        if (not school_class_id_already_added_to_current_exam):
            TeacherGUI.display_school_class_id_not_already_in_current_exam_message()
            return
        TeacherGUI.remove_school_class_id_from_current_exam(school_class_id)

    @classmethod
    def create_exam(cls):
        string_of_question_ids = TeacherGUI.get_string_of_question_ids_in_current_exam()
        string_of_school_classes_ids = TeacherGUI.get_string_of_school_classes_ids_in_current_exam()
        total_number_of_exams = TeacherDA.get_total_number_of_exams_in_db()
        exam_pk = total_number_of_exams + 1
        string_of_essay_questions_ids = TeacherDA.get_essay_questions_ids_string_from_questions_ids(string_of_question_ids)
        TeacherDA.insert_exam_into_db(exam_pk, string_of_question_ids, string_of_school_classes_ids, "Not Completed", string_of_essay_questions_ids)
        TeacherDA.set_exam_to_all_students_in_all_relevant_school_classes(exam_pk, string_of_school_classes_ids)
        all_exams = TeacherDA.get_all_exams_from_db()
        TeacherGUI.display_all_exams(all_exams)
        TeacherGUI.display_create_exam_success_message()
        TeacherGUI.refresh_create_exam_page()
        TeacherDA.insert_exam_result_to_db_by_exam_id(exam_pk)
        TeacherDA.insert_individual_student_exam_result_to_db_by_exam_id(exam_pk)
        not_completed_exams = TeacherDA.get_not_completed_exams_from_db()
        TeacherGUI.display_not_completed_exams(not_completed_exams)
        string_of_students_ids = TeacherDA.get_students_ids_in_exam_by_exam_id(exam_pk)
        TeacherDA.insert_essay_questions_results_in_to_db(string_of_essay_questions_ids, string_of_students_ids, exam_pk)

    @classmethod
    def view_exam_details_by_id(cls):
        TeacherGUI.refresh_view_exam_details_by_id_page()
        exam_id = TeacherGUI.get_exam_id_to_view_details()
        if (exam_id == None):
            return
        TeacherGUI.diaplay_exam_id_on_view_exam_details_page(exam_id)
        questions_ids = TeacherDA.get_questions_ids_in_exam(exam_id)
        TeacherGUI.display_questions_on_view_exam_details_page(questions_ids)
        school_classes_ids = TeacherDA.get_school_classes_ids_in_exam_by_exam_id(exam_id)
        school_classes_ids_list = cls.make_string_to_list(school_classes_ids)
        try:
            first_school_class_id = school_classes_ids_list[0]
            students_full_names = TeacherDA.get_students_full_names_by_school_class_id(first_school_class_id)
            TeacherGUI.display_first_school_class_details_on_view_exam_details_page(first_school_class_id, students_full_names)
        except:
            pass
        try:
            second_school_class_id = school_classes_ids_list[1]
            students_full_names = TeacherDA.get_students_full_names_by_school_class_id(second_school_class_id)
            TeacherGUI.display_second_school_class_details_on_view_exam_details_page(second_school_class_id, students_full_names)
        except:
            pass
        try:
            third_school_class_id = school_classes_ids_list[2]
            students_full_names = TeacherDA.get_students_full_names_by_school_class_id(third_school_class_id)
            TeacherGUI.display_third_school_class_details_on_view_exam_details_page(third_school_class_id, students_full_names)
        except:
            pass
        try:
            fourth_school_class_id = school_classes_ids_list[2]
            students_full_names = TeacherDA.get_students_full_names_by_school_class_id(fourth_school_class_id)
            TeacherGUI.display_fourth_school_class_details_on_view_exam_details_page(fourth_school_class_id, students_full_names)
        except:
            pass
        try:
            fifth_school_class_id = school_classes_ids_list[2]
            students_full_names = TeacherDA.get_students_full_names_by_school_class_id(fifth_school_class_id)
            TeacherGUI.display_fifth_school_class_details_on_view_exam_details_page(fifth_school_class_id, students_full_names)
        except:
            pass



    @classmethod
    def mark_exam(cls):
        exam_id = TeacherGUI.get_exam_id_to_mark()
        TeacherGUI.display_exam_id_on_marking_exam_page(exam_id)
        students_full_names_list = cls.get_students_full_names_who_have_questions_ready_to_be_marked_by_exam_id(exam_id)
        TeacherGUI.display_students_full_names_with_questions_ready_to_be_marked(students_full_names_list)
        TeacherGUI.refresh_mark_exam_drop_box()

    @classmethod
    def get_students_full_names_who_have_questions_ready_to_be_marked_by_exam_id(cls, exam_id):
        students_ids = TeacherDA.get_students_ids_in_exam_by_exam_id(exam_id)
        students_with_questions_ready_to_be_marked = []
        for student_id in students_ids.split(" "):
            if (TeacherDA.does_student_have_questions_ready_to_be_marked_for_exam(student_id, exam_id)):
                students_with_questions_ready_to_be_marked.append(student_id)
        students_full_names_list = TeacherDA.get_students_full_names_by_ids(students_with_questions_ready_to_be_marked)
        return students_full_names_list

    @classmethod
    def mark_student_questions_answers(cls):
        student_name = TeacherGUI.get_student_name_to_mark_answers()
        exam_id = TeacherGUI.get_exam_id_to_mark_student_answers()
        student_id = TeacherDA.get_student_id_by_name(student_name)
        TeacherGUI.display_exam_id_on_mark_student_answers_page(exam_id)
        TeacherGUI.display_student_id_on_mark_student_answers_page(student_id)
        TeacherGUI.display_student_name_on_mark_student_answers_page(student_name)
        questions_ready_to_be_marked = TeacherDA.get_questions_ready_to_be_marked_for_student_in_exam(student_id, exam_id)
        TeacherGUI.display_questions_ready_to_be_marked(questions_ready_to_be_marked)
        TeacherGUI.refresh_drop_student_to_mark_questions_box()

    @classmethod
    def mark_question(cls):
        question_id = TeacherGUI.get_question_id_to_mark()
        if (question_id == None):
            TeacherGUI.display_no_question_selected_to_mark_message()
            return
        exam_id = TeacherGUI.get_exam_id_on_marking_question_page()
        student_id = TeacherGUI.get_student_id_on_marking_question_page()
        essay_question_details = TeacherDA.get_essay_question_details_to_mark_by_id(question_id, exam_id, student_id)
        cls.__ui_dialog = TeacherGUI.setup_essay_question_ui_dialog_to_mark(essay_question_details)
        cls.__ui_dialog.pushButton.clicked.connect(cls.submit_essay_question_mark)

    @classmethod
    def submit_essay_question_mark(cls):
        question_mark = TeacherGUI.get_essay_question_marked_points()
        exam_id = TeacherGUI.get_exam_id_on_marking_question_page()
        student_id = TeacherGUI.get_student_id_on_marking_question_page()
        question_id = TeacherGUI.get_question_id_to_mark()
        TeacherDA.update_essay_question_mark_in_db(question_mark, exam_id, student_id, question_id)
        TeacherGUI.refresh_drop_question_to_mark_box()
        questions_ready_to_be_marked = TeacherDA.get_questions_ready_to_be_marked_for_student_in_exam(student_id, exam_id)
        if (questions_ready_to_be_marked == []):
            TeacherGUI.refresh_mark_student_questions_answers_page()
            TeacherGUI.display_no_more_questions_to_mark_message()
            students_full_names_list = cls.get_students_full_names_who_have_questions_ready_to_be_marked_by_exam_id(exam_id)
            if (students_full_names_list == []):
                TeacherDA.update_exam_status_to_marked_by_id_in_db(exam_id)
                ready_to_be_marked_exams = TeacherDA.get_ready_to_be_marked_exams_from_db()
                TeacherGUI.display_ready_to_be_marked_exams(ready_to_be_marked_exams)
            TeacherGUI.display_students_full_names_with_questions_ready_to_be_marked(students_full_names_list)
        TeacherGUI.display_questions_ready_to_be_marked(questions_ready_to_be_marked)
        marked_exams = TeacherDA.get_marked_exams_from_db()
        TeacherGUI.display_marked_exams(marked_exams)

    @classmethod
    def release_exam_result(cls):
        exam_id = TeacherGUI.get_exam_id_to_release_result()
        students_ids = TeacherDA.get_students_ids_in_exam_by_exam_id(exam_id)
        TeacherDA.update_total_points_gained_for_each_student_in_exam(students_ids, exam_id)
        TeacherDA.update_average_percentage_mark_for_each_student_in_exam(students_ids, exam_id)
        TeacherDA.update_exam_status_to_result_released_by_exam_id_in_db(exam_id)
        TeacherDA.update_exam_result_to_released_by_exam_result_id_in_db(exam_id)
        result_released_exams = TeacherDA.get_result_released_exams_from_db()
        TeacherGUI.display_result_released_exams(result_released_exams)
        marked_exams = TeacherDA.get_marked_exams_from_db()
        TeacherGUI.display_marked_exams(marked_exams)
        TeacherGUI.refresh_drop_exam_to_release_result_box()
        TeacherDA.update_completed_exams_ids_for_students_in_db(exam_id, students_ids)
        TeacherDA.update_exam_results_ids_for_students_in_db(exam_id, students_ids)
        TeacherDA.update_individual_student_exam_result_status_to_result_released_for_all_students_in_exam_in_db(exam_id)



    @classmethod
    def load_exam_details(cls):
        TeacherGUI.refresh_students_table_on_view_exam_result_details_page()
        TeacherGUI.refresh_school_classes_table_on_view_exam_result_details_page()
        exam_result_id = TeacherGUI.get_exam_result_id_to_load_details()
        is_exam_result_released = TeacherDA.is_exam_result_released_by_exam_id(exam_result_id)
        if (not is_exam_result_released):
            TeacherGUI.display_exam_result_id_invalid_message()
            TeacherGUI.refresh_load_exam_result_details_page()
            return
        TeacherGUI.refresh_exam_result_id_validity_error_message()
        school_classes_ids = TeacherDA.get_school_classes_ids_in_exam_by_exam_id(exam_result_id)
        TeacherGUI.display_school_classes_to_view_exam_result_details(school_classes_ids)
        TeacherGUI.display_exam_result_id_on_view_exam_result_details_page(exam_result_id)
        TeacherGUI.refresh_school_class_id_input_box_on_view_exam_result_details_page()
        TeacherGUI.refresh_school_class_id_invalid_to_view_exam_result_error_label()
        TeacherGUI.refresh_student_exam_result_details()


    @classmethod
    def view_school_class_exam_result(cls):
        school_class_id = TeacherGUI.get_school_class_id_to_view_exam_result()
        if (school_class_id == None):
            TeacherGUI.display_school_class_id_invalid_to_view_result_message()
            TeacherGUI.refresh_school_class_details_table_on_view_exam_result_page()
            TeacherGUI.refresh_student_exam_result_details()
            return
        exam_id = TeacherGUI.get_exam_result_id_on_view_exam_result_page()
        if (exam_id == None):
            TeacherGUI.display_no_exam_result_id_selected_message()
            TeacherGUI.refresh_school_class_details_table_on_view_exam_result_page()
            TeacherGUI.refresh_student_exam_result_details()
            return
        is_school_class_id_valid = TeacherDA.is_school_class_id_in_exam(school_class_id, exam_id)
        if (not is_school_class_id_valid):
            TeacherGUI.display_school_class_id_invalid_to_view_result_message()
            TeacherGUI.refresh_school_class_details_table_on_view_exam_result_page()
            TeacherGUI.refresh_student_exam_result_details()
            return
        students_full_names = TeacherDA.get_students_full_names_by_school_class_id(school_class_id)
        TeacherGUI.display_students_full_names_to_view_exam_result(students_full_names)
        TeacherGUI.refresh_school_class_id_invalid_to_view_exam_result_error_label()

    @classmethod
    def view_individual_student_exam_result(cls):
        student_full_name = TeacherGUI.get_student_full_name_to_view_exam_result()
        exam_result_id = TeacherGUI.get_exam_result_id_on_view_exam_result_page()
        exam_result_details = TeacherDA.get_student_exam_result_details_by_id(student_full_name, exam_result_id)
        TeacherGUI.display_student_exam_result_details(exam_result_details)
        TeacherGUI.refresh_drop_student_to_view_exam_result_details_box()


    @classmethod
    def close_application(cls):
        cls.__mainwindow.close()

    @classmethod
    def make_string_to_list(cls, any_string):
        any_string = str(any_string)
        any_list = any_string.split(" ")
        return any_list

    def __str__(self):
        return ("This is Teacher Object")