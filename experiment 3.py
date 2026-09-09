1.Aim

To write a python program to implement various string operations

2.Algorithm

1.start the program.
2.create a string variable s="hello pytho".
3.Display the original string.
4.find and display the length of the string.
5.covert the string to uppercase and display it.
6.Convert the string to lowercase ans display it.
7.Access and display the character at index 6.
8.find the position of the word"python" in the stsring
9.Extract ans display a substring usning slicing.
10.Replace "pytho" with "world" and display the result
11.Check wheather "python" is present in the string.
12.Concatrenate another string to the original string and display it.
13Create a string with extra spacese and remove leading and trailing spacese using strip().
14.Display the trimmed string.
15.stop the program.

3.Source Code

s="hello python"
print("original string:",s)
print("lenghth:",len(s))
print("uppercase:",s.upper())
print(";owercase:",s.lower())
print("character at index 6:",s[6])
print("position of python:",s.find("python"))
print("slice:",s[6])
print("replace:",s.replace("python","world"))
print(s)
print("contains python:","python" in s)
print("concentraction:",s+"programming")
s2=" hello world "
print("Trim:",s2.strip())

4.output

original string: hello python
lenghth: 12
uppercase: HELLO PYTHON
lowercase: hello python
character at index 6: p
position of python: 6
slice: p
replace: hello world
hello python
contains python: True
concentraction: hello pythonprogramming
Trim: hello world

