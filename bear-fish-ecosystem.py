'''An ecosystem containing: bears and fish, with a river modeled as a relatively large list.
Each element of the list should be filled with either a Bear object, a Fish object or None.

In each step, each animal RANDOMLY either attempts to move into an adjacent list location 
or stay where it is. If two SAME TYPE ANIMALS COLLIDE, then they stay where they are,
and they will CREATE a new instance (baby) in a random empty (previously None). 
If a bear and a fish collide, however, then the fish DIES (i.e., it disappears).

Write an initializer for the river length, the number of fishes and bears, N-simulation steps.

Before the simulation, fishes and bears should be allocated randomly into the river. The
ecosystem class should also contain a simulation() method, which will simulate the next
N steps of the random moving process. The animals on the left will take actions first.

For example, N N F N N N B N B N N -> N F N N N N N B B N N. The first fish move to the left, 
the first bear move to the right, and the second bear will remain still.'''

import random

class Ecosystem:
    def __init__(self, length = 10):    #default river length is set to 10, it is changable
        self.__rivLength = length
        self.__eco = []
        for i in range(self.__rivLength):
            ran = random.randint(1,3)
            if ran == 1:
                self.__eco.append("B")  #denote bear
            elif ran == 2:
                self.__eco.append("F")  #denote fish
            else:
                self.__eco.append("N")  #denote none
    def addAnimal(self, animal):
        choices = []
        for i in range(self.__rivLength):
            if self.__eco[i] == 'N':
                choices.append(i)
        index = random.choice(choices)  #randomly give index of a None
        self.__eco[index] = animal
    def printRiver(self):
        print(*self.__eco, sep = '')    #print out the ecosystem
    def updateRiver(self):              #checking each object from the left
        for i in range(self.__rivLength):
            self.updatePerCell(i)
    def updatePerCell(self, i):         #checking which object will move
        if self.__eco[i] != 'N':
            move = random.randint(-1,1)
            if move != 0 and 0 <= i + move < self.__rivLength:
                if self.__eco[i+move] == 'N':   #move towards None
                    self.__eco[i], self.__eco[i+move] = self.__eco[i+move], self.__eco[i]
                    # print(self.__eco) #to check each movement
                elif self.__eco[i+move] == self.__eco[i]:   #same type of animal = mating
                    if self.__eco[i] == 'B':
                        self.addAnimal('B')
                    else:
                        self.addAnimal('F')
                    # print(self.__eco) #to check each movement
                else:       #bear and fish meet, resulting the fish to die
                    self.__eco[i] = 'N'
                    self.__eco[i+move] = 'B'
                    # print(self.__eco) #to check each movement
    def Simulation(self, N):
        for i in range(N+1):
            print("Step", i)
            self.printRiver()
            self.updateRiver()

N = int(input("Enter number of steps:"))
river = Ecosystem()
river.Simulation(N)
