# Getting Started with Python

## Setup
1. Make sure you have python installed. I suggest you use [Anaconda](https://www.continuum.io/downloads)
2. Install [PyCharm](https://www.jetbrains.com/pycharm/)

## Hello World

Let's get going with a very simple "hello world" program in python. There's a number of ways to write this very simple python program, and you should be familiar with them. We'll cover three ways here. 

The first way utilizes interactive python, or "ipython".

    $ ipython

Within the ipython shell, type

    $ print 'hello world'
    $ print 'hello again'

when you hit 'enter', ipython should print out the specified text. You can exit ipython using ctrl + d.

The second way way to get python to print out 'hello world' uses standard command line python. Using a text editor, make a file called "hello.py". The file contents should be as follows:

```
print 'hello world'
print 'hello again'
```

From within the same directory, type 

    $ python hello.py

when you hit 'enter', python should print out the specified text.

A third way to get python to print out 'hello world' utilizes an integrated development environment called PyCharm. This is going to be our preferred way of writing python during this course. It's more complicated to set up a PyCharm project, but it's worth it for lots of reasons that will become clear as we go on. So let's get a 'hello world' PyCharm project going.

1) make a directory called /helloTest
2) open PyCharm
3) On the Welcome screen, click Create New Project
4) specify that the project should live in /helloTest
5) be sure to choose the anaconda interpreter
6) Click Create
7) in the project explorer, right click the 'helloTest directory', and add a new file called 'hello.py'
8) fill 'hello.py' with 
```
print 'hello world'
print 'hello again'
```





