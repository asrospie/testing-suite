# testing-suite
A command line based testing suite specifically designed to take command line arguments and test the output against text files.

## Purpose
The purpose of this testing suite is to test command line based programs at the university level. Often students have trouble creating test cases and dealing with the tedious nature of running test after test. This simple tool aims to solve that issue by automatically running the executable file for the program with a variety of command line arguments.

## Install
0. Make sure that python 3 is installed on your machine. It may work with python 2, but it was designed using python 3.
1. Clone the repo to the desired location with https://github.com/asrospie/testing-suite.git
2. Run the setup.py script 
	python3 setup.py path/to/desired/location/
3. Write the test cases
4. Run the suite.py script in your desired location
	python3 suite.py <flag> <executable>

### Creating Test Cases
The test case creation seems tricky but is actually simple. In the created inputs.in file, type all of the desired command line arguments with new tests being on different line. The first word of the line should be the test case file name without the extension. The test case file is to be placed in the tests-suite/. 

Here is an example of a working setup:
In the directory there is a RandomNumbers executable file. Lets say that RandomNumbers takes in four command line arguments, each a different integer. So the first test case may be something like 1 2 3 4. Take what the executable is expected to print out these four numbers in a random order. Take the expected order and place it in one.txt in the tests-suite/ directory.
 
In inputs.in the first line should read:
one 1 2 3 4

one.txt could contain the following:
3 4 2 1

The final step is to run the tests. To do so, call suite.py with python3 and the desired flag name. In this case, RandomNumbers is an executable so we will use the c flag.

python3 suite.py -c RandomNumbers

And that's it!

## Improvements
There are many improvements that could be made to make this better. I wrote this quickly in a day so that I could test simple programs I'm writing for an introduction level C class and hopefully make it easier for the students to test their code.
Pull requests are welcome and I will be updating this as I see fit.

## Langauges Currently Supported
[x] C
[ ] Java
[ ] C++
[ ] python
* More will be added if needed.

