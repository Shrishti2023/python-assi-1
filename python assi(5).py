#Write a program that takes a string input from the user and writes it to a text file.
str=input("enter a string:")
file=open('C:/myfile/str.txt','w')
file.write(str)
print("The string has been written to file")
