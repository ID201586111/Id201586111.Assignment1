# -*- coding: utf-8 -*-
"""
Title: agentframework.py
Created on Mon Apr 11 13:58:19 2022
Version: 1
@author: StudentID: 201586111

This file is for use with 'model.py' to be imported as a module.
The file contains an Agent class object with an __init__ defined in oder to
create an agent framework. It also contains code which takes in an environment
from a seperate text document, as well as providing code using pythagoras' 
theorm to measure distances between agents.
"""
#Import the following built in modules.
import random
import csv

'''
Make Agents.
Define a class with init function (label as self).
Create  self.x and self.y random between 0-99. Use underscore as saftey net
as to not accidently change x and y e.g (self._x).
Create environment to take in environment information.
Use, get(), set() and del() to allow users to get, set or delete the x/y values. 
'''
#Make Agents
class Agent():
    def __init__(self, environment, agents):
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agents = agents
        
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property")
                 
    
    def gety(self):
        return self._y
    def sety(self, value):
        self._y = value
    def dely(self):
        del self._y
    y = property(gety, sety, dely, "I'm the 'y' property")

    def getstore(self):
        return self._store
    
#Move agents. Tarus code stops agents from falling outside of specified grid.
    def move(self):
        if random.random() <0.5:
            self._y = (self._y + 1) %100
        else:
            self._y = (self._y - 1) %100
        if random.random() <0.5:
            self._x = (self._x + 1) %100
        else:
            self._x = (self._x - 1) %100
            
          
#eat self makes agents eat the surounding environment.
#if there are over 10 units in the environment, it eats 10 and adds 10
#to the store. If under 10 units in environmet the remaining value from the
#envronment is removed
    def eat(self):
        if self.environment[self._y][self._x] > 10: #if the env over 10
            self.environment[self._y][self._x] -= 10 #take 10 off 
            self.store += 10 #add 10 to store
        elif self.environment[self._y][self._x] < 10: #if the env under 10
            self.environment[self._y][self._x] -=self.environment % 10 #remiander  
            
#share_with_neibours loops through the agents calling distance_between them as
#the variable. If distance is less than or equal to the neigbourhood value
#then the average is calculated which distributes them evenly. If distance is
#greater than the neighbourhood value then return 0.      
    def share_with_neighbours(self, neighbourhood):
         for agent in self.agents:
             dist = self.distance_between(agent)
             if dist <= neighbourhood and dist != 0:
                 sum = self.store + agent.store
                 ave = sum /2
                 self.store = ave
                 agent.store = ave
             else:
                ave = 0
                 #print("sharing " + str(dist) + " " + str(ave))
                 
#Distance between points using pythagoras' theorm
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5 

#Environment 
def get_data():
    #Add this data, to 2d list
    environment = []    #Make empty list before any processing done
    f = open('in.txt', newline ='')
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist =[]     #Make new list before each row is processed
        for value in row:
            rowlist.append(value) #Append the values to the rowlist
        environment.append(rowlist)
    f.close()
    return environment