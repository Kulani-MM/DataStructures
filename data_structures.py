import random
import re
import string

def generate_random_list(length):
    """Generate a list of random numbers of a given length
     Examples: generate_random_list(5)
     Output: [81, 96, 77, 64, 49]
        >>>
    """

    if length < 1:
        raise ValueError("Length is not valid")
    
    return [random.randint(0, 100) for number in range(length)]

def find_max(numbers):
    """Find the maximum number in a list of numbers
     Examples: find_max(5)
     Output: 96
    """
    
    return max(numbers)


def find_min(numbers):
    """Find the minimum number in a list of numbers
    Examples: find_min([1, 2, 3, 4, 5])
     Output: 1
    """
    
    return min(numbers)


def find_average(numbers):
    """Find the average of a list of numbers
    Examples: find_average([1, 2, 3, 4, 5])
     Output: 3.0
    """
    
    return sum(numbers) / len(numbers)
 

def find_number_of_even_numbers(numbers):
    """Find the number of even numbers in a list of numbers
    Examples: find_number_of_even_numbers([1, 2, 3, 4, 5])
     Output: 2
    """
    return len([num for num in numbers if num % 2 == 0 ])

def find_number_of_odd_numbers(numbers):
    """Find the number of odd numbers in a list of numbers
    Examples: find_number_of_odd_numbers([1, 2, 3, 4, 5])
     Output: 3
    """
    return len([num for num in numbers if num % 2 != 0 ])


def find_even_numbers(numbers):
    """Find the number of even numbers in a list of numbers
    Examples: find_even_numbers([1, 2, 3, 4, 5])
     Output: (2, 4)
    """
    num = [num for num in numbers if num % 2 == 0 ]
    return tuple(num)


            
def find_odd_numbers(numbers):
    """Find the number of odd numbers in a list of numbers
    Examples: find_odd_numbers([1, 2, 3, 4, 5])
     Output: (1, 3, 5)
    """
    num = [num for num in numbers if num % 2 != 0 ]
    return tuple(num)



def return_list_stats(the_list):
    """Return a dictionary containing the max, min, mean, and average of a list of numbers
    Examples: return_list_stats([1, 2, 3, 4, 5])
     Output: {  "unique_numbers": {1, 2, 3, 4, 5},
                "min": 1, "max": 5, "average": 3.0,
                "even_numbers": (2, 4),
                "odd_numbers": (1, 3, 5),
                "number_of_even_numbers": 2,
                "number_of_odd_numbers": 3
            }
    """

    return {"unique_numbers": {num for i,num in enumerate(the_list)}, 
            "min": min(the_list), 
            "max": max(the_list),  
            "average": round((sum(the_list) / len(the_list)) ,1), 
            "even_numbers": find_even_numbers(the_list), 
            "odd_numbers": find_odd_numbers(the_list), 
            "number_of_even_numbers": find_number_of_even_numbers(the_list), "number_of_odd_numbers": find_number_of_odd_numbers(the_list) }

def process_characters(input_list):
    """
    Process a list of characters, separating alphabets and numbers,
    removing duplicates and returning them in sorted order.

    Parameters:
    - input_list (list): A list containing characters.

    Returns:
    - Two lists - sorted alphabets as strings and sorted numbers as integers.
    Examples: 
    >>> process_characters(['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e'])
    Output: ['a', 'b', 'c', 'd', 'e'], [1, 3, 5]
    """
    letters = []
    numbers = []
    for letter in input_list:
        if letter in string.ascii_lowercase and letter not in letters:
                letters.append(letter)
            
    for num in input_list:
        if num.isnumeric() and int(num) not in numbers:
                numbers.append(int(num))

    return  sorted(letters), sorted(numbers)

def generate_squared_dict(n):
    """
    Generate a dictionary containing numbers and their squares.

    Given a positive integer `n`, this function will generate a dictionary
    that contains numbers from 1 to n as keys and their squares as values.

    Parameters:
        n (int): The upper limit for the numbers in the dictionary.

    Returns: ..
        dict: A dictionary with numbers and their squares.

    Example:
        >>> generate_squared_dict(5)
        Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    """
    if n > 0:
        return {num: num*num  for num in  range(1, n + 1)}
    else:
        return {num: num*num  for num in  range(n, 0)}


def convert_to_word_list(text):
    """
    Returns all words in a senctence as a list without the punctuation and spaces.
    Example:
        >>>  convert_to_word_list("There is only one to fear and his name is Death,"
        +" and there is only one thing we say to Death: 'Not today!")
        
    Output: ['there', 'is', 'only', 'one', 'to', 'fear', 'and', 
        'his', 'name', 'is', 'death', 'and', 'there', 'is', 'only', 
        'one', 'thing', 'we', 'say', 'to', 'death', 'not', 'today']
    """
    return "".join( [word.strip(",:!'").lower()  for word in text] ).split()


def letters_count_map(text):
    """
    Map the total count of each letter to the alphabet and return this as a dictionary.
    Example:  letters_count_map(
            "There is only one to fear and his name is Death,"
        +" and there is only one thing we say to Death: 'Not today!")
    
    Output: {'a': 8, 'b': 0, 'c': 0, 'd': 5, 'e': 11, 'f': 1, 'g': 1, 'h': 6, 'i': 5, 'j': 0, 'k': 0, 'l': 2, 'm': 1,
             'n': 9, 'o': 8, 'p': 0, 'q': 0, 'r': 3, 's': 5, 't': 9, 'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 4, 'z': 0}
    """
    return {letter: (text.lower()).count(letter) for letter in string.ascii_lowercase }


def text_to_morse(text):
    """
    Convert a given string to its Morse code equivalent.

    The function takes an input string containing alphanumeric characters in lower or upper case,
    along with special characters that are handled in Morse code, including commas, colons, apostrophes,
    periods, exclamation marks, and question marks. It returns the Morse code representation of the input string.

    Parameters:
        text (str): The input string to be converted to Morse code.

    Returns:
        str: The Morse code representation of the input string.

    Morse Code Mapping:
        Alphanumeric characters (case-insensitive) and digits 0-9 are mapped to their respective Morse code representations.
        Special characters are also handled accordingly as follows:
            ',' (comma) : '--..--'
            ':' (colon) : '---...'
            "'" (apostrophe) : '.----.'
            '.' (period) : '.-.-.-'
            '!' (exclamation mark) : '-.-.--'
            '?' (question mark) : '..--..'
            Space (' ') : ' '

    Examples:
        >>> text_to_morse("Hello World 123")
        Output: '.... . .-.. .-.. ---   .-- --- .-. .-.. -..   .---- ..--- ...-- '
    """
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ',': '--..--', ':': '---...', "'": '.----.', '.': '.-.-.-', '!': '-.-.--', '?': '..--..', ' ': ' '
    }
    
    return " ".join([morse_code_dict[i.upper()]  for i in  text]) 
