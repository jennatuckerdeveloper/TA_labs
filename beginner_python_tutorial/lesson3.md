#Lesson 3 - Using error messages for debugging  

So far, you have seen at least one error message in your terminal and very likely more.  

Whether or not Python produces an error message when it reads a particular script, if the script does not do what you
expect or want it to do, the script has at least one *bug* in it.  

*Debugging* a piece of code is the process of going through it to remove and fix errors in the code.  

An error message is there to help you find a bug and recognize, and before long, you'll be able to read them in a flash.  

When an error message appears, Python is saying, "Wait, I can't understand this part."  

Error messages are helpful, but it takes a little practice reading and applying them to make them really useful.  

## What to do... 

Let's do a little debugging now.  

What do you expect to see when you run this bit of code?  

Hint:  There is a bug in this code that will not allow this string to print.  

Can you find the bug just by looking?  


```python
print("Hello, World!)
```

Copy and past this line of code into a new script, save it, and run it in your terminal.  

You will get the following error message in your terminal:  

```python
  File "lesson1.py", line 1
    print("Hello, World!)
                        ^
SyntaxError: EOL while scanning string literal
```
If you copy and past the last line with the syntax error message into a search browser, you will find pages of people 
asking what the error message means and trying to figure out what is wrong with particular bits of code.  Give it a try!

*EOL* stands for "End Of Line," so what Python is saying is that it was reading a string (it specifies a string 
literal, but we can ignore the literal part for now), and the line ended unexpectedly.  

If you look closely, Python is pointing to the closing parentheses that tells it where the line ends.  

The line ends before the string, so what's missing is the end of the string!  

Where was the string supposed to end?  

After the exclamation point and before the end parentheses, and there is no end 
quotation mark there.  

If you add this missing end quotation mark, the script will run properly.  

Let's take a look at another example.  

What do you expect to see when you run this bit of code?

```python
print"Hello, World!") 
```

Once again, if you copy and paste this script, save it, and run it in your terminal, you will get an error message.

This time, it's a different error message that reads:  

```python
  File "lesson1.py", line 1
    print"Hello, World!")
                       ^
SyntaxError: invalid syntax
```

This error message just says that there is invalid syntax in your code, and it's pointing to the end quotation mark.

Scanning through this line, you can see that the print statement touches the string, and there is an end parentheses
that appears without an opening parentheses.  

Even though Python's error message did not point to the precise place where the bug was in this line of code, it did
point to the specific line that had the bug, and this is incredibly useful in a long script.  
 
Let's do one more.  

What do you expect to see when you run this bit of code?

```python
print("Helo, World!")

greeting = "Hello, world!"

print(greeting

print('Hey')
```

Copy and past this line of code into a new script, save it, and run it in your terminal.  

You will get the following error message in your terminal:  

```python
  File "lesson1.py", line 7
    print('Hey')
        ^
SyntaxError: invalid syntax
```

This is the kind of error message that drives early programmers crazy... 

There is no bug on this line of code.  The string has it's opening and closing quotation marks.  The print statement
has it's opening and closing parentheses.  If you were to copy this one line, save it in a script, and run it, it 
would print and there would be no error message.  

Look at the of code before this one.  Do you see that the end parentheses is missing?  

```python
print(greeting
```

This is the bug, and Python thinks this line did not end.  So it thinks the next print statement is an error.  

Whenever you receive an error message on a line of code and cannot find a bug in that line of code, look at the line
before to see if that line is closed!

## What you just did...

You just removed three bugs from someone else's code!  

You also stepped past the early tendencies of programmers.  

First, beginner programmers ignore error messages.  

Second, beginner programmers trust error messages too much and become frustrated.  

Third, beginner programmers feel stuck on error messages they have not seen before, rather than just throwing the error
message into a browser search.  

As you can imagine, there is a huge presence of programmers online, and figuring out how to troubleshoot using quick
searches and online communities is a huge part of being a programmer.  

## Want to try this again?  

Copy some of your working code from lessons 1 and 2 and save it in another *.py* file.
Make an error in the script / insert a bug.  
Run the code and see what happens.  
Did you get any new error messages?
How accurate were the error messages to where you put the new bug?


