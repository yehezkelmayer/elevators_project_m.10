import pygame
from class_floor import Floor
from class_elevator import Elevator

class Building():
    def __init__(self, num_of_floors, num_of_elevators) -> None:
        self.__floors = []
        for i in range (num_of_floors + 1):
            self.__floors.append(Floor(i))
        
        self.__elevator = []
        for i in range (num_of_elevators):
            self.__elevator.append(Elevator(i))
       
    
    def build(self, screen, height,):
        current_height = height

        for floor in self.__floors:
            floor.init_floor(screen, current_height - 70)
            current_height -= 37
    
    def build1(self, screen, height, a =200):    
        for elevator in self.__elevator:
            elevator.init_elevator(screen, height-70, a)   
            a += 30
    
    # def build(self, screen, width, height):  
    #     for floor in self.__floors:
    #         Floor.init_floor(screen, height - 70)
    #         height -= 37
    #     for elevator in self.__elevator:
    #         Elevator.init_elevator(screen, height - 70)   
    #         width -= 30 
        
        