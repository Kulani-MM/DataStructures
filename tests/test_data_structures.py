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

    def test_basic(self):
        input_list = ['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)

    def test_mixed_input(self):
        input_list = ['a', '1', 'b', '3', 'c', '2', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_repeated_characters(self):
        input_list = ['1', 'b', 'a', 'c', 'c', 'b', 'a', '1']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_special_characters(self):
        input_list = ['!', '@', '#', '1', '2', '3', '$', '%', '^']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_more_special_characters(self):
        input_list = ['%', '&', '*', '4', '6', '8', '(', ')', '!', 'x']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_generate_squared_dict(self):
        assert generate_squared_dict(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        self.assertEqual(generate_squared_dict(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
        self.assertEqual(generate_squared_dict(1), {1: 1})
        self.assertEqual(generate_squared_dict(0), {})

    def test_convert_word_list_sentence(self):
        sentence = "Hello, world! This is a test."
        self.assertEqual(convert_to_word_list(sentence), ['hello', 'world', 'this', 'is', 'a', 'test'])

        sentence = "Coding is fun; let's code!"
        self.assertEqual(convert_to_word_list(sentence), ['coding', 'is', 'fun', 'lets', 'code'])

        sentence = ""
        self.assertEqual(convert_to_word_list(sentence), [])
 
    def test_convert_word_list_spaces(self): pass
       

    def test_letters_count_sentence(self):
        text = "Hello, World!"
        expected_counts = {
            'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 1, 'f': 0, 'g': 0, 'h': 1, 'i': 0, 'j': 0, 'k': 0, 'l': 3,
            'm': 0, 'n': 0, 'o': 2, 'p': 0, 'q': 0, 'r': 1, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 0, 'z': 0
        }
        self.assertEqual(letters_count_map(text), expected_counts)

        text = "aaa bbb ccc ddd"
        expected_counts = {'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
                           'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
                           'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.assertEqual(letters_count_map(text), expected_counts)

        text = ""
        self.assertEqual(letters_count_map(text), {chr(i): 0 for i in range(97, 123)})

    def test_alphanumeric_1(self): pass
    
    def test_alphanumeric_2(self): pass
    
    def test_alphanumeric_3(self): pass
    

