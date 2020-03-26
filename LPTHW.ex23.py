import sys 
# usual command line argument handling
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
#defined our main function with these
	line = language_file.readline()
	# the first thing we're doing here is reading one line from the language file we're giving it 	
	if line:
		print_line(line, encoding, errors)
		# the variables for print_line are line, encoding, and errors
		return main(language_file, encoding, errors)
		# we're calling main inside main
		# we're creating a loop here 
# as long as readline returns something, this will be true, so then code lines 9-10 will run. if nothing is in the readline file, then 9-10 will not fun because it is false	
		
def print_line(line, encoding, errors):
# defining a new function print_line with the variables line, encoding, and errors
	next_lang = line.strip( )
	#this is a simple stripping of the trailing \n on the line strings
	raw_bytes = next_lang.encode(encoding, errors=errors)
	# encode and decode are commands for python to do a specific action that is given
	cooked_string = raw_bytes.decode(encoding, errors=errors)
	
	print(raw_bytes, "<===>", cooked_string)
	
languages = open("languages.txt", encoding="utf-8")
# breaking it number 3 = encoding="b ' '" 

main(languages, encoding, error)

# some notes
"""
 a byte = a sequence of 8 bits (1s and 0s)
 
 Once we have the ASCII convention for encoding a character using 8 bits (a byte), we can then ”string”
them together to make a word. If I want to write my name ”Zed A. Shaw,” I just use a sequence of bytes
that are [90, 101, 100, 32, 65, 46, 32, 83, 104, 97, 119].

The problem with ASCII is that it only encodes English and maybe a few other similar languages.

To solve this problem a group of people created Unicode. It sounds like ”encode,” and it is meant to be a
”universal encoding” of all human languages. The solution Unicode provides is like the ASCII table, but
it’s huge by comparison.

"DBES" mnemonic "Decode Bytes, Encode Strings" 

"""

# buffer overflow
# how much data can python's data string decode before it does a buffer overflow / break?
