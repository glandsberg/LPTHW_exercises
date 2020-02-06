# Exercise 10 - repeating for github and practice
"""
What was that?
the backslash character \ encodes difficult-to-type characters into a string
one of various "escape sequences"
an important escape sequence is to escape single quote or double quote
if you want to use quotes in a string
you need a way to tell python that the " inside the string isn't real

"I am 6'2\" tall." # escape double-quote inside string
'I am 6'2\" tall.' # escape single-quote inside string

"""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# escape sequences listed on page 65

