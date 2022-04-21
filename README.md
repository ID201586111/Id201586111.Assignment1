# 201586111.github.io
 Assignment 1
 
201586111.github.io
Assignment 1

Title: GEOG5003M Assignment 1, Online Portfolio

Contents:
•	.gitattributes - automatically created by github for repository.

•	LICENSE - MIT license file- short/simple permissive license. conditions only requiring preservation of copyright&license notices stipulates the open source licence for code.

•	README.md - THIS File which provides instructions and overview for the project.

•	agentframework.py - the module which is used by the main model.py.

•	in.txt - Raster file as text document

•	index.html - The HTML file for the webpage that links to this project. 

•	model.py - the main code which runs the model.


Description:
The project can be run from command prompt or through Spyder software. It is recommended the use should use Spyder if they want to change the number of coordinates plotted, number of iterations they move or the size of the neighbourhood. The main files for code are; 'model.py' and 'agentframework.py' and you will also need a raster file, there is one included called in.txt

The project creates a pop out window showing an environment with 10 random coordinates plotted (agents). These agents have been randomly moved 100 times, each impacting the surrounding environment. The agents ‘eat away’ the environment which they move through, and these values are stored. Text files are generated which list the new environment and the agents coordinates.
'agentframework.py' is an object-oriented code which encapsulates the agents' properties and behaviour, as well as the agents' environment. This agent framework code is used by the main 'model.py'. In 'agentframework.py' the class 'Agent' is defined creating self.x and self.y coordinates- also defining getx/y, setx/y and delx/y. The code also defines 'move' which randomly moves x and y by 1 unit. This is carried out 100 times (but can be changed in main model). 'agentframework.py' also contains code that defines 'eat' and 'share_with_neibours' these allow the agents to interact with the environment changing it as they move. Currently the neighbourhood the agents 'eat' is set to 20 units but this can also be changed in the main model. Also contained in this code is defined 'distance_between' which uses pythagoras' theorem (c2 = a2 + b2), to find the distance between 2 points where the distance between to points is the hypotenuse (c2). The Environment is also defined as 'get_data', this creates an empty list called environment and creates a new list for each row of values for the environment.

'model.py' is the main model and is the code that the user can run. The model has a timer which starts before the first line of code and ends after the last line of code for the model, printing 'time=' and the time the code took to process. Also, before the code starts there is an option to set the random seed for reproducible results. The environment is set from 'agentframework.py' next the user can control how many agents are plotted, how many iterations the random movement of agents happen, and control the size of the neighbourhood. Next using a loop, and the 'Agent' class from 'agentframework.py' the agents are created. The using a nested loop and the 'move', 'eat' and 'share_with_neighbours' code from 'agentframework.py', the agents are moved, eaten, and shared with neighbours. Next is some code to find the distance between the agents, using pythagoras' theorem from 'agentframework.py'. The original code has been left in to show how you would measure all agents against each other. However, this has been commented out and after it there is code that optimises this code so that it iterates through each coordinate and does not repeat i.e. measures point 1 to point 3 then measures point 3 to point 1. It also makes sure each coordinate is not measured against itself, returning zero units. The model then uses the 'max' and 'min' functions to print the maximum distance between the agents and the minimum distance. The environment is then printed in a separate textfile using 'fileinput.input' which writes files. Lastly using 'matplotlib' the environment is drawn over a grid (0,99 on x/y axis) and the agents are plotted over it.

The raster text file contains comma separated variable data, each value being equivalent to a pixel in an image.

How to Run/Use Project: 
Download the three files; 'model.py' and 'agentframework.py' and raster data (in.txt). 'model.py' will be the file where you can change the inputs, 'agentframework.py' should not be edited unless you are changing the raster file for the environment. If you have your own raster data in a txt file copy that to the same folder as the python files and call it 'in.txt' deleting the 'in.txt' file from the project folder. If you would like to keep the 'in.txt' file from the project folder and another raster you will need to edit line 74 in 'agentframework.py' to 'f = open('YOUR RASTER TEXT FILE NAME HERE.txt', newline ='')'.
In the 'model.py' file you can edit row 51 to control the number of agents (coordinates) you want to show. Edit row 53 to control the number of iterations the 'move' function will carry out. Edit row 55 to control the number in the neighbourhood.

Also if you would like to set the random seed or turn it off edit the number in row 38.

Credits: Student ID: 201586111 Using code from University of Leeds, MSc, GEOG5003M.

Testing: The model was tested throughout using the timer to try and optimise the code and debugging to solve any issues.

