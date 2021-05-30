
############################ STRING METHODS ############################

# dir(str)
    # The dir() function returns all properties and methods of the string object:

dir(str)

# help(str.method) is used to display the information about the method:

help(str.strip)
help(str.capitalize)

################################# 1.len(str) ########################################

# The method is used  to get the length of the given string, array, list, tuple, dictionary, etc.

notes = [1, 2, 3, 4]
len(notes)

################################ 2. count() ########################################

fruits = ['apple', 'banana', 'cherry','strawberry','apple', 'plum', 'watermelon', 'banana']
fruits.count("banana")
fruits.count("strawberry")


################################# 3.upper() & lower() ########################################

#  The method is used  to get the length of the given string, array, list, tuple, dictionary, etc.

    # upper() method is converts all the characters of a string to uppercase.
    # lower() method is converts all the characters of a string to lowercase.

students = ["John", "Mark", "Venessa", "Mariam"]
students[0].upper()
students[2].lower()

################################# 4.capitalize() ########################################

# The method converts the first character of the string to a capital (uppercase) letter while making all other characters to lowercase.

students = ["JOHN", "MARK", "VENESSA", "MARIAM"]
students[2].capitalize()
students[3].capitalize()

################################# 5.swapcase() ########################################

# The method returns a string where all the upper case letters are lowercase and vice versa.

name = ["John", "maRIAM"]
name[0].swapcase()
name[1].swapcase()

################################# 6. replace(searchvalue, newvalue) ########################################

#  The method searches for a specified value in a string and returns the result by replacing it with the specified value.

text = "this is a string method!"
text.replace(" is", " was")


############################ 7.str.maketrans(x, y, z) & translate() ########################################
# translate() is used to make transitions of the characters in the string.
    #  This function uses the translation mapping specified using the maketrans().


# maketrans () method provides  to create character mappings conversion table. The method  takes 3 parameters;
    # x: Specifies the list of characters that need to be replaced.
    # y: The list of characters by which is to be transformed.
    # z : Specifies the list of characters that needs to be deleted.


# Replacing Turkish characters with English characters:

text = "Bu ifade İçerisindekı TÜrkçe karakterleri İngilizce karakterlerle değiştiriniz"
letters_to_change = "çÇğĞıİöÖşŞüÜ"
letters_tobe_converted = "cCgGiIoOsSuU"

text_conversion = str.maketrans(letters_to_change, letters_tobe_converted)
text.translate(text_conversion)


################################# 8. strip(char) ########################################

# Removes leading and trailing spaces of the given characters based on its default value and returns it without spaces.
#  However, if a different expression is specified instead of "character", strip(character = optional) removes them and returns the string.

print(" Hello AI ".strip())
print("**Hello AI!**".strip("**"))
print(" **Hello AI!** ".strip().strip("**"))

################################# 9.split(seperator) ########################################

# split() method is used to split an array into new substrings and returns the new substrings into a list.
    # separator is a delimiter. If is not provided then any white space is a separator.

print("The_method_is_used_to_split_an_array_into_new_substrings".split("_"))
    """
    ['The', 'method', 'is', 'used', 'to', 'split', 'an', 'array', 'into', 'new', 'substrings']
    """

print("Hello AI Era".split())
    """ 
        ['Hello', 'AI', 'Era']
    """"

################################ 10.isalnum()  ########################################

# isalnum() method checks if all the characters are alphanumeric (alphabet letter (a-z) or numbers(0-9)), if it provides the condition returns "True"

"Hello".isalnum()
"123".isalnum()

"Hello123".isalnum()

################################ 11.isnumeric() ########################################

# isnumeric() method returns True if all the characters are numeric (0-9).

"99".isnumeric()

"Hello123".isnumeric()
"Hello".isnumeric()

################################ 12.isalpha() ########################################

# isalpha() returns True if all the characters are alphabet letters (a-z)

name="venessa"
print(name.isalpha())

name=" venessa "
print(name.isalpha())
    """Returns false if there is a space in the string  """

################################ 13. index(start_index) ########################################
# index() is a built-in-function for using to search for a given element from the start of the list and returns the first occurrence of the element.
# start_index is optional.  If is not provided, then start searching from the first element of the list.

letters = ["e","a","u","i","a","e","a"]
letters.index("a")

letters = ["e","a","u","i","a","e","a"]
letters.index("a",2)
""" Start searcing from index 2."""

################################ 14. startswith() & endswith() ########################################

# startswith() method returns True if a string starts with the specified prefix(string). However it is case sensitive.
# endswith() method returns True if a string ends with the specified prefix(string). However it is case sensitive.

text ="Python is easy to learn"
text.startswith("Python")
text.startswith("is easy")

# Returns false because it is case sensitive.
text.startswith("python")

text.endswith("earn")
# Returns false because it is case sensitive.
text.endswith("Earn")

################################ 15. sorted() ########################################

# The function returns a sorted list of the specified iterable object.

# Sort ascending:
print(sorted("notebook"))

# Sort descending:
print(sorted("notebook" , reverse=True))

set_obj = {'e', 'a', 'u', 'o', 'i'}
print(sorted(set_obj, reverse=True))

# dictionary
dict_obj = {'d': 1, 'b': 2, 's': 3, 'e': 4, 'a': 5}
print(sorted(dict_obj))


################################ 16. Join() ########################################
# A string method which returns a string in which the elements of sequence have been joined by str separator.

text = ["A","string","method","which","is","used","to","concatenate","the","elements"]
sep = " "
sep.join(text)

list = ['1','2','3','4']
"_".join(list)

seq = ("a", "b", "c")
"*".join(seq)

################################ 17. str.contains() ########################################

# The contains() is a string method that checks if a string contains the given character.

fruits = ['apple', 'banana', 'cherry','strawberry','apple', 'plum', 'watermelon', 'apple', 'banana']

import pandas as pd
fruits_series = pd.Series(fruits)
fruits_series[fruits_series.str.contains("ap")]
fruits_series.str.contains("ap").sum()

fruits_series.str.contains("ba").sum()
