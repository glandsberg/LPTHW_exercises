# What do you know so far?

| Term, method,character      | Definition          | Example |
| ------------- |:-------------:| -----:|
| print    | prints to the screen | print("Hello ya'll") |
| ' ' single quotes     | string can be placed inside single quotes      |   name = 'Grace' |
| " " double quotes | string can be placed inside double quotes      |    name = "Grace" |
| # hash sign | used to comment out of lines text NOT to be coded | # this is a comment |
| + plus sign | concatination - putting stuff together | var1 = 'Cheese' var2 = 'burger' var1 + var2 |
| + plus sign | addition | 4 + 2 |
| - minus sign | subtraction | 9 - 3 |
| / slash | division | 8 / 2 |
| * asterisk | multiplication | 9 * 3 |
| % percent | modulus, the remainder | 9 % 4 |
| < left bracket | less than | 8 < 10 |
| > right bracket | greater than | 22 > 10 |
| <= right bracket - equal | less than equal | 12 <= 12.5 |
| >= left bracket-equal | greater than equal | 12.5 >= 12 |
| var = x | variables are to hold data and assigned with the = operator | car = "mazda" |
| print(f"{var}") | format string. like string interpolation (interpolation = variable substitution) | print(f"My car is a {car}.") |
| .format() | formats values from variables & inserts them into a string placeholder {} | print("My name is {0}".format("Grace")) |
| \n Linefeed | inserts a linefeed (new line, like a return) into a string | print("Eggs\nMilk\nButter") |
| print("some_string", var) | the variable will be tacked onto the end of the string | snack = "Twix" print("Favorite candy: " , snack ) |
| """ 3 quotes | print out a multi-line string | print(""" lines of text with returns """ ) |
| \t tab | insert a tab in a string when it prints | dalmation= "tI have spots" |
| \ backslash | insert a backslash in a string when it prints | dob = "7\12\1995" print(dob) |
| \' Single quote | escape a single-quote in a string when it prints | job = 'I\'m a teacher' |
| \" Double quote | escape a double-quote in a string when it prints | quote =  "They said, \"Learn Python\"" |
| \r | carriage return | all the characters after the \r move left that many characters (overwrites) |
| end=' ' | assigns a space & when printing, it won't print a newline | print("Hello", end=' '); print("Autumn") |
| exit() | exit the REPL | >>> exit() |
| input() | pauses the program and waits for user input, then assigns it to a variable | name = input("What is your name? " ) |
| pydoc | documentation module. run the command like man pages | pydoc sys |
| help() | help from within the REPL | >>> help () |
| from sys import argv | sys is a module that gives access to variables and functions. import adds features, like adding argv. Argv holds the arguments passed to it on the command line when you run your script | from sys import argv |
| script, some_param = argv | This line will unpack the argv and all of it's arguments passed on the command line. argv[0] is always the name of the script, the 1st argument passed in | python LPTHW.ex14.py name |
| int() |Converts string to numbers. Anything from an input is a string, so this is useful if you need it to be an integer | age = input("what is your age?") |
| open() | opens a file and returns it as an object | somefile = open(filename) |
| read() | reads the contents of a file | print(somefile.read()) |
| close() | closes a file after its been opened | close(somefile) |
| readline() | reads just one line of text in a file | readline(somefile) |
| truncate() | clears a file. be careful | truncate(somefile) |
| write() | appends to a file | somefile.write("put stuff in the file") |
| seek() | moves to a new position in filestream | somefile.seek(0) |
| open(somefile,'w') | the w argument means you want to open a file in write mode | open(file1,'w') |
| open(somefile, 'r') | the r argument means you want to open a file in read mode | open(file1,'r') |
| open(somefile,'a') | the a argument means you want to open a file in append mode | open(file1, 'a') |
| open(somefile,'r+') | the r+ argument means you want to read and write to the file | open(file1,'r+') |
| open(somefile,'w+') | the w+ argument means you want to write and read to the file | open(file1,'w+') |
| open(somefile,'a+') | the a+ argument means you want to append and write to the end file | open(file1, 'a+') |
| os.path | module that provides useful functions on pathnames | from os.path import exists |
| from os.path import exists export | returns true if the pathname path exists, false if it doesn't or if you don't have access | from os.path import exists export |
| def | defining a function | function definition must end in a : and the function body begins with 4 spaces | def add(var1, var2):