# Lesson 2 - Assign strings to variables  

## What to do... 

Open your *lesson1.py* file that reads: 

```python
print("Hello, World!")
```

On lines beneath this first line, write:

```python
greeting = "Hello, again World!"

print(greeting)
```

Your entire script should look like:

```python
print("Hello, World!")
greeting = "Hello, again World!"
print(greeting)
```

Save your file and run it in the terminal using the same command as in lesson 1 with the command:  

```python 
:~$ python lesson1.py 
```

The following should appear in your terminal window:

```python 
Hello, World! 
Hello, again World! 
```

If you get an error message, make sure your script matches this text exactly.  
Look especially at the parentheses and quotation marks.  
If you are really stuck, try copying and pasting the script shown in your file.  
If this runs, then try again to type it manually and see if you can catch your previous error.

## What you just did...

In the last lesson, you wrote a single line of code to print the phrase, "Hello, World!" to your terminal console.  
In this lesson, you added two lines of code that printed another phrase to your console.  
The difference was that this time, you *assigned the phrase to a variable*.  

In Python, when you write something in either single quotes or double quotes, the computer understands this as a *string*.

A string is a particular *type* of data.  

So what happens if you enter text and do not put single or double quotes around it?  
With a handful of exceptions, the computer understands words written without quotes around them as variable names.  

Let's do a little experiment.  

## Let's do some more... 

Add a line of code to the bottom of your *lesson1.py* script:


```python
Hey
```

Now save your file, and run it in your console.  

Rather than printing what you might expect, which would be something like:

```python 
Hello, World! 
Hello, again World! 
Hey
```

Your console will have an error that reads:  

```python 
  File "lesson1.py", line 7, in <module>
    Hey
NameError: name 'Hey' is not defined
```

The reason is that Python read your new addition as a variable name, and you did not *assign* any data to the variable.  

This is what Python means when it tells you in the error message that the word *Hey* is not defined.  

We can fix this in several ways.  

First, change the last line in your *lesson1.py* script to:

```python
'Hey'
```

Now, when you save and run your script, instead of the error message, you should see:

```python 
Hello, World! 
Hello, again World! 
```

But what happened to that last line you wrote?  
Python read that line as a string and understood it, so there was no error message.  
But that was all, since you did not tell Python to do anything with the string.  
If you want to simply see the string when you run the script, you would tell Python to print it to your console.  
Let's do this, so you can see it.  

Change the last line of your *lesson1.py* script to:  

```python
print('Hey')
```

You should now see:  

```python 
Hello, World!
Hello, again World!
Hey
```

When Python reads the string that you wrote in your script, it reads the print command, as well.  
So Python prints your string to the console.  


Typically, you will want to do something more than to a piece of string data than simply printing it.  
In order to be able to work with a bit of data, you *assign it to a variable*.  

You can think of a variable name as a labeled box that your computer uses to store something you're working with.  
You will find that you can empty out that box or change its contents - that is *reassign* or *mutate* data.     
We'll see this happen as we go along.  For now, focus on seeing if a bit of text in a script is a string or a variable.  

Add these two lines of code to the end of your script:  

```python
hi = 'Hey'
print(hi)
```

Save your file, and run it in your terminal.  
What do you expect to see?  

```python 
Hello, World!
Hello, again World!
Hey
Hey
```

You now have four strings printed to your console.  
Two of those strings are stored as variables.  

## Want to try this again?  
Write a script of six lines by doing the following:  
Using any three phrases, write three strings. 
Choose three variable names.  
Use the equals sign to assign each string to a variable.  
Write the print command and then the variable name inside of parentheses.  
Save and run your script in your terminal.  

An example of a script like this would be:  

```python 
dogs = "I love dogs."
cats = "And I love cats."
want = "But I would prefer to get a dog."
print(dogs)
print(cats)
print(want)
```

And when this script was saved and run in the terminal, the output would be:

```python 
I love dogs.
And I love cats.
But I would prefer to get a dog.
```

