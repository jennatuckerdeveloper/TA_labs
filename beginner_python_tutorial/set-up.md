#Set-Up Part 3:  Using your terminal 

## You already know how to do what's in this lesson 

Take just a moment to make a new folder on your desktop named *folder1*.  

You probably create new folders, move folders, look into folders, and delete folders all the time.  

As a beginner programmer, you can start doing these simple tasks using your computer's *command line*. 

The command line is often also referred to as the *terminal* or the *console*.  

While it's simple enough to manage folders the way you already know how, there are more complex ways to interact
with your computer that require you to use the command line. 

You can think of going to a computer's command line as something like looking under the hood of a car.  
When you look under the hood of a car, you have not made any major or invasive changes yet.  You can do something
minor like adding windshield washer fluid, or you can do something major like replacing a part.  Just going to
your command line will not damage your computer, but there are things you can do in the command line that require
at least some expertise to do properly and to get a beneficial result.  

You can learn to use the command line by doing familiar tasks using simple commands.  

##Open a terminal window 

***Open a terminal window  

##Move to another folder using *cd -- change directory*

When your terminal loads, it will print a line to orient you as to where you are and then wait for you to enter a  
command.

```python
MyComputer:~ MyHomeFolder$ 
```

Just like when you use your familiar way to move from one folder to another, you take one step at a time.  

So if I have a folder called *big* and inside that is a folder called *medium* and inside that is a folder called 
*small*, if I open the *big* folder, I cannot get into the *little* folder without passing through the *medium* folder.  

I could do this by using the command *cd medium* then the command *cd big* or I could *chain* these two steps
together into what's called a *pathway* and type *cd medium/little* to get into the *little* folder.  

You can move forwards or backwards, and when you want to back up, you can simply type *cd ..* to go back a step.
To go back multiple steps, you would create a pathway using multiple steps back by typing *cd ../..* for two 
steps and so on.

##See what's inside a folder using *ls -- list*

cd ls mkdir rm (resursive remove and idea of flags) mv (move) and cp(copy)

##Create a new folder using *mkdir*

##Move a folder or file using *mv*

##Copy a file or folder using *cp* 

##Delete a file or folder using *rm* (and HESITANTLY using *-r rm*)

If this were tree pruning, that little addition of *-r* would mean the difference between removing a twig and removing a 
branch.  

If this were cleaning out your fridge, it would be the difference between throwing out a bad potato and dumping your 
entire vegetable drawer in the trash when the garbage truck has already reached the neighbor's.  

Of course, it's fine to throw away a folder along with all of its contents.  

BUT DON'T USE THE COMMAND *-r rm* WITHOUT HESITATING FIRST.  

You could throw out a folder with very important contents, and like a branch on the ground or food in the dump, it's
very hard to undo.  (Not impossible but probably very expensive.)


