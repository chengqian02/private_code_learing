

from hashlib import new
from msilib.schema import Class
from queue import Queue
import random
import re
from tkinter.messagebox import NO

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages

    def waitTiem(self, currenttime):
        return currenttime - self.timestamp

class Printer:
    def __init__(self, ppm) -> None:
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining -1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
        
    def startNext(self, newTask: Task):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages()\
            *60/self.pagerate

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue(30)
    waitingtimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.put(task)

        if (not labprinter.busy() and (not printQueue.empty())):
            nexttask:Task = printQueue.get()
            waitingtimes.append(nexttask.waitTiem(currentSecond))
            labprinter.startNext(nexttask)
        
        labprinter.tick()
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait, printQueue.qsize()))


def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False


if __name__ == "__main__":
    for i in range(10):
        simulation(3600, 5)