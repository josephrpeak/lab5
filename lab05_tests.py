import lab05 as cd

import unittest
import sys

MENU = """
                CHOOSE TEST TO RUN
1. Test function character_value
2. Test function check_digit
3. Test function verify_check_digit
4. Test function get_school
5. Test function get_grade
A. Test All
Q. Quit

==> """


class CharacterValues(unittest.TestCase):

    def test_character_value_returns_0_for_A(self):

        result = cd.character_value("A")
        self.assertEqual(0, result, "When passed A character value should return 0")

    def test_character_value_returns_1_for_B(self):

        result = cd.character_value("B")
        self.assertEqual(1, result, "When passed B character value should return 1")

    def test_character_value_returns_25_for_Z(self):

        result = cd.character_value("Z")
        self.assertEqual(25, result, "When passed Z character value should return 25")

class CheckDigit(unittest.TestCase):
    def test_get_check_digit_1(self):
        result = cd.get_check_digit("ABCDE01234")
        self.assertEqual(0, result, "The check digit is incorrect for ABCDE012345")

    def test_get_check_digit_2(self):
        result = cd.get_check_digit("CBCDE01234")
        self.assertEqual(2, result, "The check digit is incorrect for CBCDE012345")

    def test_get_check_digit_3(self):
        result = cd.get_check_digit("XBCDE01234")
        self.assertEqual(3, result, "The check digit is incorrect for XBCDE012345")

    def test_get_check_digit_4(self):
        tv = "AACDE01234"
        result = cd.get_check_digit(tv)
        self.assertEqual(8, result, f"The check digit is incorrect for {tv}")

    def test_get_check_digit_5(self):
        tv = "AAZDE01234"
        result = cd.get_check_digit(tv)
        self.assertEqual(7, result, f"The check digit is incorrect for {tv}")

    def test_get_check_digit_6(self):
        tv = "ABCDE31234"
        result = cd.get_check_digit(tv)
        self.assertEqual(8, result, f"The check digit is incorrect for {tv}")
        
    def test_get_check_digit_7(self):
        tv = "ABCDE32234"
        result = cd.get_check_digit(tv)
        self.assertEqual(5, result, f"The check digit is incorrect for {tv}")

    def test_get_check_digit_8(self):
        tv = "ABCDE12334"
        result = cd.get_check_digit(tv)
        self.assertEqual(1, result, f"The check digit is incorrect for {tv}")

    def test_get_check_digit_9(self):
        tv = "ABCDE12344"
        result = cd.get_check_digit(tv)
        self.assertEqual(0, result, f"The check digit is incorrect for {tv}")

    def test_get_check_digit_10(self):
        tv = "ABCDE12386"
        result = cd.get_check_digit(tv)
        self.assertEqual(6, result, f"The check digit is incorrect for {tv}")


class VerifyCheckDigit(unittest.TestCase):

    def test_verify_check_digit_returns_a_tuple(self):
        result = cd.verify_check_digit("ABCDE12386")
        self.assertIsInstance(result, tuple, "verify_check_digit_should_return_tuple")
        self.assertEqual(2, len(result), "function should return a tuple of length of 2.")
        self.assertIsInstance(result[0], bool, "Index item 0 should be a boolean")
        self.assertIsInstance(result[1], str, "Index item 1 should be a string returned")        

    def test_verify_check_digit_returns_true_with_emptystring_with_valid_value1(self):

        result, error = cd.verify_check_digit("ABCDE12386")
        self.assertTrue(result, "When passed a valid # it should return True as first parameter in tuple")
        self.assertEqual("", error, "When passed a valid # it should return an empty string as second parameter in tuple")

    def test_verify_check_digit_returns_false_with_correct_error_string_with_invalid_checkdigit(self):

        result, error = cd.verify_check_digit("ABCDE12383")
        self.assertFalse(result, "When passed an invalid # it should return False as first parameter in tuple")
        self.assertEqual("Check Digit 3 does not match calculated value 6.", error, "When passed a valid # it should return an empty string as second parameter in tuple")

    def test_verify_check_digit_when_value_passed_is_less_than_10_digits(self):

        result, error = cd.verify_check_digit("ABC12383")
        self.assertFalse(result, "When passed an short input it should return False as first parameter in tuple")
        self.assertEqual("The length of the number given must be 10", error, "When passed a short # it should return the correct error.")

    def test_verify_check_digit_when_value_passed_is_greater_than_10_digits(self):

        result, error = cd.verify_check_digit("ABCDE12345AK")
        self.assertFalse(result, "When passed an short input it should return False as first parameter in tuple")
        self.assertEqual("The length of the number given must be 10", error, "When passed a short # it should return the correct error.")

    def test_verify_check_digit_when_value_a_non_AZ_character_in_first_5_digits(self):

        for idx in range(0, 5):
            test_value = "ABCDE12345"
            test_value = test_value[:idx] + "8" + test_value[idx+1:]
            result, error = cd.verify_check_digit(test_value)
            self.assertFalse(result, "When passed an non A-Z character in first five places throws errors.")
            self.assertEqual(f"The first 5 characters must be A-Z, the invalid character is at {idx} is 8", error, "When passed an non A-Z character in first five places throws errors.")

    def test_verify_check_digit_when_value_a_non_digit_character_in_last_5_digits(self):

        for idx in range(0, 5):
            test_value = "ABCDE12345"
            test_value = test_value[:idx] + "8" + test_value[idx+1:]
            result, error = cd.verify_check_digit(test_value)
            self.assertFalse(result, "When passed an non A-Z character in first five places throws errors.")
            self.assertEqual(f"The first 5 characters must be A-Z, the invalid character is at {idx} is 8", error, "When passed an non A-Z character in first five places throws errors.")

    def test_verify_check_digit_6th_character_only_be_1_2_or_3(self):

        test_value = "ABCDE42345"
        result, error = cd.verify_check_digit(test_value)
        self.assertFalse(result, "When passed an non 1, 2 or 3 character in 5th_index it should return False")
        self.assertEqual("The sixth character must be 1 2 or 3", error, "When passed an non 12or 3 character in index 5 place returns appropriate error.")

        test_value = "ABCDE02345"
        result, error = cd.verify_check_digit(test_value)
        self.assertFalse(result, "When passed an non 1, 2, or 3 character in 5th_index it should return False")
        self.assertEqual("The sixth character must be 1 2 or 3", error, "When passed an non 12or 3 character in index 5 place returns appropriate error.")

        test_value = "ABCDE12340"
        result, error = cd.verify_check_digit(test_value)
        self.assertTrue(result, "When passed an 1, 2, or 3 character in 5th_index it should return True")

        test_value = "ABCDE22346"
        result, error = cd.verify_check_digit(test_value)
        self.assertTrue(result, "When passed an 1, 2, or 3 character in 5th_index it should return True")

        test_value = "ABCDE32342"
        result, error = cd.verify_check_digit(test_value)
        self.assertTrue(result, "When passed an 1, 2, or 3 character in 5th_index it should return True")

    def test_verify_check_digit_7th_character_only_be_1_2_3_or_4(self):

        test_value = "ABCDE15345"
        result, error = cd.verify_check_digit(test_value)
        self.assertFalse(result, "When passed an non 1, 2 3, or 4 character in 6th_index it should return False")
        self.assertEqual("The seventh character must be 1 2 3 or 4", error, "When passed an non 1,2,3 or 4 character in index 6 place returns appropriate error.")

        test_value = "ABCDE10345"
        result, error = cd.verify_check_digit(test_value)
        self.assertFalse(result, "When passed an non 1, 2 3, or 4 character in 6th_index it should return False")
        self.assertEqual("The seventh character must be 1 2 3 or 4", error, "When passed an non 1,2,3 or 4 character in index 6 place returns appropriate error.")

        test_value = "ABCDE11343"
        result, error = cd.verify_check_digit(test_value)
        self.assertTrue(result, "When passed an 1, 2, 3, or 4 character in 6th_index it should return True")

        test_value = "ABCDE12340"
        result, error = cd.verify_check_digit(test_value)
        self.assertTrue(result, "When passed an 1, 2, 3, or 4 character in 6th_index it should return True")

        test_value = "ABCDE13347"
        result, error = cd.verify_check_digit(test_value)
        self.assertTrue(result, "When passed an 1, 2, 3, or 4 character in 6th_index it should return True")

        test_value = "ABCDE14344"
        result, error = cd.verify_check_digit(test_value)
        self.assertTrue(result, "When passed an 1, 2, 3, or 4 character in 6th_index it should return True")


class GetSchoolTests(unittest.TestCase):

    def test_get_school_returns_SCE_when_passed_1_in_index_5(self):
        result = cd.get_school("ABCDE12386")
        self.assertEqual(result, "School of Computing and Engineering SCE", "A value of 1 in index 5 should return SCE")

    def test_get_school_returns_SOL_when_passed_2_in_index_5(self):
        result = cd.get_school("ABCDE22386")
        self.assertEqual(result, "School of Law", "A value of 2 in index 5 should return School of Law")

    def test_get_school_returns_CAS_when_passed_3_in_index_5(self):
        result = cd.get_school("ABCDE32386")
        self.assertEqual(result, "College of Arts and Sciences", "A value of 3 in index 5 should return College of Arts and Sciences")

    def test_get_school_returns_InvalidSchool_when_passed_invalidvalue_in_index_5(self):
        result = cd.get_school("ABCDE82386")
        self.assertEqual(result, "Invalid School", "A value of 8 in index 5 should return Invalid School")


class GetGradeTests(unittest.TestCase):

    def test_get_grade_returns_Freshman_when_passed_1_in_index_6(self):
        result = cd.get_grade("ABCDE11386")
        self.assertEqual(result, "Freshman", "A value of 1 in index 7 should return Freshman")

    def test_get_grade_returns_sophomore_when_passed_2_in_index_6(self):
        result = cd.get_grade("ABCDE12386")
        self.assertEqual(result, "Sophomore", "A value of 2 in index 7 should return Sophomore")

    def test_get_grade_returns_junior_when_passed_3_in_index_6(self):
        result = cd.get_grade("ABCDE13386")
        self.assertEqual(result, "Junior", "A value of 3 in index 7 should return Junior")

    def test_get_grade_returns_senior_when_passed_4_in_index_6(self):
        result = cd.get_grade("ABCDE14386")
        self.assertEqual(result, "Senior", "A value of 4 in index 7 should return senior")

    def test_get_grade_returns_invalidgrade_when_passed_7_in_index_6(self):
        result = cd.get_grade("ABCDE17386")
        self.assertEqual(result, "Invalid Grade", "A value of 7 in index 7 should return Invalid Grade")


def main_menu():

    while True:

        result = input(MENU).upper()
        if result == "1":
            unittest.main(cv, exit=False)
        elif result == "2":
            unittest.main(checkdigit, exit=False)
        elif result == "3":
            unittest.main(vcd, exit=False)
        elif result == "4":
            unittest.main(gst, exit=False)
        elif result == "5":
            unittest.main(ggt, exit=False)
        elif result == "A":
            unittest.main(exit=False)
        elif result == "Q":
            return
        else:
            print("Enter a value from the menu given ")

if __name__ == "__main__":
    __unittest = True

    cv = CharacterValues()
    checkdigit = CheckDigit()
    vcd = VerifyCheckDigit()
    gst = GetSchoolTests()
    ggt = GetGradeTests()
    
    main_menu()
