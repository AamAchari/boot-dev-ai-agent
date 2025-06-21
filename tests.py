import unittest
# from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
class TestFilesInfo(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    # def test_1_get_file_info(self):
    #     try:
    #         result = get_files_info("calculator", ".")
    #         print(result)
    #     except Exception as e:
    #         print(e)
    # def test_2_get_file_info(self):
    #     try:
    #         result = get_files_info("calculator", "pkg")
    #         print(result)
    #     except Exception as e:
    #         print(e)
    # def test_3_get_file_info(self):
    #     try:
    #         result = get_files_info("calculator", "/bin")
    #         print(result)
    #     except Exception as e:
    #         print(e)
    # def test_4_get_file_info(self):
    #     try:
    #         result = get_files_info("calculator", "../")
    #         print(result)
    #     except Exception as e:
    #         print(e)
    # def test_1_get_file_content(self):
    #     try:
    #         result = get_file_content("calculator", "main.py")
    #         print(result)
    #     except Exception as e:
    #         print(e)
    # def test_2_get_file_content(self):
    #     try:
    #         result = get_file_content("calculator", "pkg/calculator.py")
    #         print(result)
    #     except Exception as e:
    #         print(e)
    # def test_3_get_file_content(self):
    #     try:
    #         result = get_file_content("calculator", "/bin/cat")
    #         print(result)
    #     except Exception as e:
    #         print(e)
    # def test_4_get_file_content(self):
    #     try:
    #         result = get_file_content("calculator", "lorem.txt")
    #         print(result)
    #     except Exception as e:
    #         print(e)
    def test_1_write_file_content(self):
        try:
            result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
            print(result)
        except Exception as e:
            print(e)
    def test_2_write_file_content(self):
        try:
            result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
            print(result)
        except Exception as e:
            print(e)
    def test_3_write_file(self):
        try:
            result = write_file("calculator","/tmp/temp.txt", "this should not be allowed")
            print(result)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    unittest.main()
