import unittest
from inspect import getsourcefile
import os.path
import sys
from unittest.mock import patch
import shutil
from distutils.dir_util import copy_tree
import filecmp
from io import StringIO

current_path = os.path.abspath(getsourcefile(lambda: 0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from text_file_manager import TextFileManager
from text_formatter import TextFormatter
from file_copier import FileCopier


class TestClass(unittest.TestCase):
    test_cases_folder = "/test_cases"

    def setUp(self):
        self.main_dir = os.path.dirname(os.path.abspath(__file__)) + "/" + "tmp"

        if os.path.exists(self.main_dir):
            shutil.rmtree(self.main_dir)
            os.mkdir(self.main_dir)
        else:
            os.mkdir(self.main_dir)

        folder_to_copy = os.path.dirname(os.path.abspath(__file__)) + self.test_cases_folder
        copy_tree(folder_to_copy, self.main_dir)

        self.patcher = patch('text_file_manager.TextFileManager.path', new=self.main_dir)
        self.patcher.start()

    def tearDown(self):
        shutil.rmtree(self.main_dir)
        self.patcher.stop()

    def test_tfm_hashfile(self):
        text_file_manager = TextFileManager(None, True, None)
        h = text_file_manager.hashfile(self.main_dir + "/lorem_different_indents.txt")
        self.assertEqual(h, "567110f6cb0ec6ee37a19f6cc03737da")

    def tes_tfm_find_dup(self):
        text_file_manager = TextFileManager(None, True, None)
        dup = text_file_manager.find_dup(self.main_dir)
        self.assertEqual(len(dup["c7e25fc2db5dfe618c064534f6a3c64e"]), 3)
        self.assertEqual(len(dup["567110f6cb0ec6ee37a19f6cc03737da"]), 2)
        self.assertEqual(len(dup["ebf3c9927b85a1327262d24ddcff526e"]), 1)
        self.assertEqual(len(dup["e3b63cdaccd4d8f72610ef904562eb5a"]), 1)

    def test_tfm_get_file_to_format(self):
        text_file_manager = TextFileManager("spaces", True, 4)
        text_file_manager.path = self.main_dir
        files = text_file_manager.get_file_to_format()
        self.assertEqual(len(files), 7)

    def test_tf_get_all_file_lines(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents.txt", 4)
        lines_len = len(text_formatter.lines)
        self.assertEqual(lines_len, 43)

    def test_tf_space_to_tab_4(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents.txt", 4)
        text_formatter.space_to_tab()
        edited_file = self.main_dir + "/lorem_different_indents.txt"
        correct_edited_file = os.path.abspath(__file__ +
                                              "/../correct_edited_files/lorem_different_indents_space_to_tab_4.txt")
        self.assertEqual(True, filecmp.cmp(edited_file, correct_edited_file))

    def test_tf_space_to_tab_12(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents.txt", 12)
        text_formatter.space_to_tab()
        edited_file = self.main_dir + "/lorem_different_indents.txt"
        correct_edited_file = os.path.abspath(__file__ +
                                              "/../correct_edited_files/lorem_different_indents_space_to_tab_12.txt")
        self.assertEqual(True, filecmp.cmp(edited_file, correct_edited_file))

    def test_tf_space_to_tab_1(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents.txt", 1)
        text_formatter.space_to_tab()
        edited_file = self.main_dir + "/lorem_different_indents.txt"
        correct_edited_file = os.path.abspath(__file__ +
                                              "/../correct_edited_files/lorem_different_indents_space_to_tab_1.txt")
        self.assertEqual(True, filecmp.cmp(edited_file, correct_edited_file))

    def test_tf_space_to_tab_3(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents.txt", 3)
        text_formatter.space_to_tab()
        edited_file = self.main_dir + "/lorem_different_indents.txt"
        correct_edited_file = os.path.abspath(__file__ +
                                              "/../correct_edited_files/lorem_different_indents_space_to_tab_3.txt")
        self.assertEqual(True, filecmp.cmp(edited_file, correct_edited_file))

    def test_tf_tab_4_to_space(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents.txt", 4)
        text_formatter.tab_to_space()
        edited_file = self.main_dir + "/lorem_different_indents.txt"
        correct_edited_file = os.path.abspath(__file__ +
                                              "/../correct_edited_files/lorem_different_indents_tab_4_to_space.txt")
        self.assertEqual(True, filecmp.cmp(edited_file, correct_edited_file))

    def test_tf_tab_5_to_space(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents_tab_5.txt", 5)
        text_formatter.tab_to_space()
        edited_file = self.main_dir + "/lorem_different_indents_tab_5.txt"
        correct_edited_file = os.path.abspath(__file__ +
                                              "/../correct_edited_files/lorem_different_indents_tab_5_to_space.txt")
        self.assertEqual(True, filecmp.cmp(edited_file, correct_edited_file))

    def test_tf_tab_12_to_space(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents_tab_12.txt", 12)
        text_formatter.tab_to_space()
        edited_file = self.main_dir + "/lorem_different_indents_tab_12.txt"
        correct_edited_file = os.path.abspath(__file__ +
                                              "/../correct_edited_files/lorem_different_indents_tab_12_to_space.txt")
        self.assertEqual(True, filecmp.cmp(edited_file, correct_edited_file))

    def test_tf_tab_3_to_space(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents_tab_3.txt", 3)
        text_formatter.tab_to_space()
        edited_file = self.main_dir + "/lorem_different_indents_tab_3.txt"
        correct_edited_file = os.path.abspath(__file__ +
                                              "/../correct_edited_files/lorem_different_indents_tab_3_to_space.txt")
        self.assertEqual(True, filecmp.cmp(edited_file, correct_edited_file))

    def test_tf_get_empty_space_from_tab_value_5(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents_tab_3.txt", 3)
        res = text_formatter.get_empty_space_from_tab_value(5)

        self.assertEqual(res, "     ")

    def test_tf_get_empty_space_from_tab_value_12(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents_tab_3.txt", 3)
        res = text_formatter.get_empty_space_from_tab_value(12)

        self.assertEqual(res, "            ")

    def test_tf_get_empty_space_from_tab_value_1(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents_tab_3.txt", 3)
        res = text_formatter.get_empty_space_from_tab_value(1)

        self.assertEqual(res, " ")

    def test_tf_analyze_file(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents.txt", 4)
        res = text_formatter.analyze_file()
        spaces_len = len(res[0])
        tabs_len = len(res[1])
        self.assertEqual(spaces_len, 11) and self.assertEqual(tabs_len, 10)

    def test_tf_print_analyze_file(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents.txt", 4)
        res = text_formatter.analyze_file()

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            text_formatter.print_analyze_file(res[0], res[1])
            x = fakeOutput.getvalue().strip().split("\n")
            self.assertEqual(x[0], 'The program founded 11 spaces in rows:  4, 6, 8, 12, 14, 17, 19, 23, 25, 34, 43, ')
            self.assertEqual(x[1], "The program founded 10 tabs in rows:  2, 10, 16, 21, 26, 28, 30, 32, 37, 41, ")

    def test_tf_print_edited_rows(self):
        text_formatter = TextFormatter(self.main_dir, "lorem_different_indents.txt", 4)

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            text_formatter.print_edited_rows([1, 2, 3, 4, 5])
            self.assertEqual(fakeOutput.getvalue().strip(), 'The program edited 5 rows')

    def test_fc_get_correct_filename_without_extension(self):
        file_copier = FileCopier(self.main_dir, "lorem_different_indents.txt")

        res = file_copier.get_filename_without_extension()

        self.assertEqual(res, "lorem_different_indents")

    def test_get_none_from_fc_get_filename_without_extension(self):
        file_copier = FileCopier(self.main_dir, "")

        res = file_copier.get_filename_without_extension()

        self.assertEqual(res, None)

    def test_get_none_1_from_fc_get_filename_without_extension(self):
        file_copier = FileCopier(self.main_dir, None)

        res = file_copier.get_filename_without_extension()

        self.assertEqual(res, None)

    def test_fc_copy_file(self):
        file_copier = FileCopier(self.main_dir, "lorem_different_indents.txt")
        res = file_copier.copy_file()
        self.assertEqual(True, filecmp.cmp(self.main_dir + "/lorem_different_indents.txt", res))

    def test_fc_copy_file_with_empty_string_as_filename(self):
        file_copier = FileCopier(self.main_dir, "")
        res = file_copier.copy_file()
        self.assertEqual(res, None)

    def test_fc_copy_file_without_filename(self):
        file_copier = FileCopier(self.main_dir, None)
        res = file_copier.copy_file()
        self.assertEqual(res, None)

    def test_tf_convert_text_without_copying(self):
        TextFileManager("spaces", True, 4)

        files = os.listdir(self.main_dir)

        for f in files:
            print(f)

        self.assertEqual(len(files), 10)

    def test_tf_convert_text(self):
        TextFileManager("spaces", False, 4)

        files = os.listdir(self.main_dir)

        self.assertEqual(len(files), 17)

    def test_tf_convert_text_f_spaces(self):
        TextFileManager("spaces", False, 4)

        edited_file = self.main_dir + "/lorem_different_indents.txt"
        correct_edited_file = os.path.abspath(__file__ +
                                              "/../correct_edited_files/lorem_different_indents_space_to_tab_4.txt")
        self.assertEqual(True, filecmp.cmp(edited_file, correct_edited_file))

    def test_tf_convert_text_f_tabs(self):
        TextFileManager("tabs", False, 4)

        edited_file = self.main_dir + "/lorem_different_indents.txt"
        correct_edited_file = os.path.abspath(__file__ +
                                              "/../correct_edited_files/lorem_different_indents_tab_4_to_space.txt")
        self.assertEqual(True, filecmp.cmp(edited_file, correct_edited_file))

    def test_tf_convert_text_only_r_param(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            TextFileManager(None, False, None)
            x = fakeOutput.getvalue().strip().split("\n")
            self.assertEqual(x[12], 'The program founded 11 spaces in rows:  4, 6, 8, 12, 14, 17, 19, 23, 25, 34, 43, ')
            self.assertEqual(x[19], 'The program founded 44 tabs in rows:  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,'
                                    ' 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,'
                                    ' 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, ')
            self.assertEqual(x[25], 'The program founded 11 spaces in rows:  4, 6, 8, 12, 14, 17, 19, 23, 25, 34, 43, ')

    def test_tf_convert_text_without_params(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            TextFileManager(None, None, None)
            files = os.listdir(self.main_dir)
            x = fakeOutput.getvalue().strip().split("\n")
            self.assertEqual(x[26], 'The program founded 10 tabs in rows:  2, 10, 16, 21, 26, 28, 30, 32, 37, 41, ')
            self.assertEqual(len(files), 10)


if __name__ == '__main__':
    unittest.main()
