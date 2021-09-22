print('we are using here escape charactor like "\n" , "\t" """"tripal queots""""  ')
# using \n to next line.
# using \t to space on string.
# """" trippal queot to resolve issue of writing single or double multiple writing.

SplitString = ' hi we are using \n split \n escape \n charactor on \n string'
print(SplitString)
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('Is your home town deoghar "\'e\' s no no... this is my own\'s town" .')
#or
print("Is your home town deoghar '\"e\" s no no... this is my own\'s town' .")

# now we resolve this backslash issue with the help of triple queots
print("""Is your home town deoghar "\'e\' s no no... this is my own\'s town" .\n""")

# with the help of we can split without using \n
print("""Is your home town deoghar 
"\'e\' s no no... 
this is my work\'s town" .""")

# how can i make a single line with using split or backslash
print("""Is your home town deoghar \
"\'e\' s no no... \
this is my work\'s town" .""")

#some time backslash making error in this situation how we can handle..print('C:\Users\tim\noun.txt')
print('C:\\Users\\tim\\noun.txt')
print(r'C:\Users\tim\noun.txt')



