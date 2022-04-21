

# -*- coding: utf-8 -*-
"""
Title: Model.py
Created on Mon Mar 28 12:58:01 2022
Version: 1
@author: StudentID: 201586111

The project creates a pop out window showing an environment with 10 random 
coordinates plotted (agents). These agents have been randomly moved 100 
times, each impacting the surrounding environment. The agents ‘eat away’ 
the environment which they move through, and these values are stored. 
Text files are generated which list the new environment and the agents 
coordinates.
Users can edit: the amount of agents plotted, the number of times they move
and the neibourhood size in which they move/eat.
"""

'''
please not an attempt was made to code the following:
An Animated pop up environment &
A text file generated to list the agent values
These codes have been kept in to show they have been attempted however 
they are either '#' out or edited out with 3 commas.
'''
#import the following built in modules 
import random
import matplotlib.pyplot
#import matplotlib.animation
import time
import csv
#import the agent framework module created for this project.
import agentframework

# Set the random seed for reproducible results. This enables testing.
#Please '#' out for random results each time.
random.seed(0)
#random.seed(1)

#start the clock so testing can be done.
start = time.process_time()

environment = agentframework.get_data()

'''
Set the controls, users can edit the amount of: 
agents, iterations and neibourhood.
'''
#Control How many agents we have
num_of_agents = 10
#control how many iterations we have
num_of_iterations = 100
#control neighbourhood- search distance around the agents.
neighbourhood = 20

#create empty list for agents, to add coords to.
agents =[]

'''
#create figure grid for the animation.
fig = matplotlib.pyplot.figure(figsize=(7, 7)) #agent size on grid
ax = fig.add_axes([0, 0, 100, 100]) #grid size

'''
'''
# Make the agents by appending Agents class within the agentframework module
to the number_of_agents, using  'for' loop to num_of_iterations.
Also links the envronment to the agents list.
'''
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Move the agents, eat agents using neibourhood size.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

'''
#The follow code is the attepmt at getting an animated grid working.

def update(frame_number):
    
    fig.clear()   

    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 100 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 100
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 100 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 100 
        
   
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        print(agents[i][0],agents[i][1])


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
'''
'''
#Fist code to find distance between agents.        
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = agentframework.Agent.distance_between\
        (agents_row_a, agents_row_b)
        #print (distance)
'''
#Optimise distance code so no repeats
#iterate through each coordinate
for agents_row_a in agents:
    for agents_row_b in agents:
        if agents_row_a != agents_row_b and agents_row_a.getx()\
            < agents_row_b.getx():
            distance = agentframework.Agent.distance_between\
            (agents_row_a, agents_row_b)
            distance_list= []
            distance_list.append(distance)
            #print("Distance:", str(distance))
            
'''       
Distance list. No longer required 

distances = []
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = agentframework.Agent.distance_between(agents_row_a,\
                                                         agents_row_b)
        distances.append(distance)
        #print(distance)
'''

#Find Maxium and Minium distances from list of distances and prints them.
maxd = agentframework.Agent.distance_between(agents[0], agents[1])
mind = agentframework.Agent.distance_between(agents[0], agents[1])
distances = []
for i in range(0, num_of_agents, 1):
    for j in range(i+1, num_of_agents, 1):
    #for j in range(0, num_of_agents, 1):
        if (i < j):
        #if (i != j):
            #print(i, j)
            distance = agentframework.Agent.distance_between\
            (agents[i], agents[j])
            maxd = max(maxd, distance)
            mind = min(mind, distance)
print("maxd", maxd)       
print("mind", mind)       
        
#Write Environment as text file using csv writer.
write_environment= open("Environment.txt", "w", newline='') #blank text file
writer  =csv.writer(write_environment, delimiter= ",")
#Write each row in the environment
for row in environment:
    writer.writerow(row)
write_environment.close() 

'''
#Write Agents as text file
write_agents= open("Agent_Values.txt", "a")#blank text file called Agent_Values
#Write each agent as string with comma between
for row in range(num_of_agents):
    write_agents.write(str(agentframework.Agent.getstore()), ",")
write_agents.write("\n") #new line
write_agents.close() #close
'''

#Plot on graph
matplotlib.pyplot.xlim(0, 99) #x axis
matplotlib.pyplot.ylim(0, 99) #y axis
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
#end timer
end = time.process_time()

print ("time= " +str(end - start))