import unittest
from data_structures import *


class MyTestCase(unittest.TestCase):
    def test_generate_random_list(self):
        self.assertTrue(len(generate_random_list(5)) == 5)
        with self.assertRaises(ValueError):
            generate_random_list(0)
            generate_random_list(-1)
        for number in generate_random_list(5):
            self.assertTrue(number <= 100)
            self.assertTrue(number >= 0)

    def test_find_max(self):
        self.assertEqual(find_max([1, 3, 5, 7, 9]), 9)
        self.assertEqual(find_max([-1, -3, -5, -7]), -1)
        self.assertEqual(find_max([5]), 5)

    def test_find_min(self):
        self.assertEqual(find_min([1, 3, 5, 7, 9]), 1)
        self.assertEqual(find_min([-1, -3, -5, -7]), -7)
        self.assertEqual(find_min([5]), 5)

    def test_find_average(self):
        self.assertAlmostEqual(find_average([1, 3, 5, 7, 9]), 5.0)
        self.assertAlmostEqual(find_average([10, 20, 30]), 20.0)
        self.assertAlmostEqual(find_average([0, 10, 20, 30]), 15.0)

    def test_find_all_even_numbers(self):
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5]), (2, 4))
        self.assertEqual(find_even_numbers([1, 3, 5]), ())
        self.assertEqual(find_even_numbers([2, 4, 6, 8]), (2, 4, 6, 8))

    def test_find_all_odd_numbers(self):
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5]), (1, 3, 5))
        self.assertEqual(find_odd_numbers([2, 4, 6]), ())
        self.assertEqual(find_odd_numbers([1, 3, 5, 7]), (1, 3, 5, 7))

    def test_find_total_number_of_even_numbers(self):
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5]), 2)
        self.assertEqual(find_number_of_even_numbers([1, 3, 5]), 0)
        self.assertEqual(find_number_of_even_numbers([2, 4, 6, 8]), 4)

    def test_find_total_number_of_odd_numbers(self):
        self.assertEqual(find_number_of_odd_numbers([1, 2, 3, 4, 5]), 3)
        self.assertEqual(find_number_of_odd_numbers([2, 4, 6]), 0)
        self.assertEqual(find_number_of_odd_numbers([1, 3, 5, 7]), 4)

    def test_return_list_stats(self):
        stats = return_list_stats([1, 2, 3, 4, 5])
        self.assertEqual(stats["min"], 1)
        self.assertEqual(stats["max"], 5)
        self.assertEqual(stats["average"], 3.0)

        stats = return_list_stats([0, 0, 0])
        self.assertEqual(stats["min"], 0)
        self.assertEqual(stats["max"], 0)
        self.assertEqual(stats["average"], 0.0)

        stats = return_list_stats([2, 4, 6, 8])
        self.assertEqual(stats["even_numbers"], (2, 4, 6, 8))
        self.assertEqual(stats["number_of_even_numbers"], 4)
        self.assertEqual(stats["number_of_odd_numbers"], 0)

        stats = return_list_stats([3, 5, 7, 9])
        self.assertEqual(stats["odd_numbers"], (3, 5, 7, 9))
        self.assertEqual(stats["number_of_odd_numbers"], 4)
        self.assertEqual(stats["number_of_even_numbers"], 0)

        stats = return_list_stats([2])
        self.assertEqual(stats["min"], 2)
        self.assertEqual(stats["max"], 2)


    def test_basic(self):
        input_list = ["a", "1", "b", "3", "c", "@", "5", "d", "e"]
        result_alphabets, result_numbers = process_characters(input_list)

        for letter in result_alphabets:
            self.assertNotEqual(letter, "@")
            self.assertTrue(letter in string.ascii_lowercase)
        
        for number in result_numbers:
            self.assertTrue(number in string.digits)



    def test_mixed_input(self):
        input_list = ["a", "1", "b", "3", "c", "2", "@", "5", "d", "e"]
        result_alphabets, result_numbers = process_characters(input_list)

    def test_repeated_characters(self):
        input_list = ["1", "b", "a", "c", "c", "b", "a", "1"]
        result_alphabets, result_numbers = process_characters(input_list)\
        
        self.assertEqual(result_alphabets, ["a", "b", "c"])
        self.assertEqual(result_numbers, [1])

    def test_special_characters(self):
        input_list = ["!", "@", "#", "1", "2", "3", "$", "%", "^"]
        result_alphabets, result_numbers = process_characters(input_list)

        for letter in result_alphabets:
            self.assertFalse(letter in string.ascii_lowercase)

    def test_more_special_characters(self):
        input_list = ["%", "&", "*", "4", "6", "8", "(", ")", "!", "x"]
        result_alphabets, result_numbers = process_characters(input_list)
    
        self.assertEqual(result_alphabets[0], "x")
        self.assertEqual(len(result_alphabets), 1)

    def test_generate_squared_dict(self):
        assert generate_squared_dict(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        self.assertEqual(generate_squared_dict(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
        self.assertEqual(generate_squared_dict(1), {1: 1})
        self.assertEqual(generate_squared_dict(0), {})

    def test_convert_word_list_sentence(self):
        sentence = "Hello, world! This is a test."
        self.assertEqual(
            convert_to_word_list(sentence),
            ["hello", "world", "this", "is", "a", "test"],
        )

        sentence = "Coding is fun; let's code!"
        self.assertEqual(
            convert_to_word_list(sentence), ["coding", "is", "fun", "lets", "code"]
        )

        sentence = ""
        self.assertEqual(convert_to_word_list(sentence), [])

    def test_convert_word_list_spaces(self):
        list = convert_to_word_list("hello, world!")
        self.assertEqual(list, ["hello", "world"])
        self.assertEqual(convert_to_word_list(",:!'"), [])

    def test_letters_count_sentence(self):
        input = letters_count_map("hello")

        self.assertEqual(input["h"], 1)
        self.assertEqual(input["e"], 1)
        self.assertEqual(input["l"], 2)
        self.assertEqual(input["o"], 1)
             
    def test_alphanumeric_1(self):
        pass

    def test_alphanumeric_2(self):
        pass

    def test_alphanumeric_3(self):
        pass
