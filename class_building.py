import pygame
from class_floor import Floor
from class_elevator import Elevator

image_floor = '/home/mefathim/Documents/Pasted image (3).png'
image_elevator = '/home/mefathim/Documents/elv.png'
speed =  1 / 5
green = (0, 255, 0)
color = (50, 180, 100)
ding_sound = pygame.mixer.Sound('ding.mp3')
class Building():
    def __init__(self, num_of_floors, num_of_elevators) -> None:
        
        self.__floors = []
        for i in range (num_of_floors + 1):
            self.__floors.append(Floor(i))
        
        self.__elevator = []
        for i in range (num_of_elevators):
            self.__elevator.append(Elevator(i))
        
        
       
    def build_floors(self, screen, height):
        current_height = height
        for floor in self.__floors:
            floor.init_floor(screen, current_height - 70, floor)
            current_height -= 37
    
    
    def build_elevators(self, screen, height, a =200):   
        for elevator in self.__elevator:
            elevator.init_elevator(screen, height-70, a)  
            a += 30
    
    
    
    def move(self, screen, button):
      
        for floor in self.__floors:
            if floor.button.collidepoint(button):
            # if floor.rect.center[0] + 15 >= button[0] >= floor.rect.center[0] - 15 \
            #     and floor.rect.center[1] + 15 >= button[1] >= floor.rect.center[1] - 15: 

                    destination =  floor.rect.center[1] 
                    # - self.__elevator[0].rect.center[1] 
                    # if destination != 0:
                    if destination > self.__elevator[0].rect.centery:
                        screen.fill(color)
                        
                        destination *= speed
                        self.__elevator[0].rect.centery -= destination
                    
                    elif destination < self.__elevator[0].rect.centery:
                        destination *= speed
                        self.__elevator[0].rect.centery += destination
                        
                    else:
                        pygame.mixer.Sound.play(ding_sound)    
                        
                        
                        # self.__elevator[0].rect.centery = floor.rect.centery
                        button = None   

                    for elevator in self.__elevator:
                        screen.blit(elevator.image, elevator.rect) 
                    for floor in self.__floors:
                        screen.blit(floor.image, floor.rect)         
                    for floor in self.__floors:
                        pygame.draw.line(screen,(0, 0, 0), [40, floor.y - 4], [190, floor.y - 4], width=7)
                        pygame.draw.circle(screen, (floor.button_color), (115, floor.y + 17), 13)
                        font = pygame.font.Font(None, 25)
                        text = font.render(f"{floor.floor_number}", True, (250, 250, 250))
                        screen.blit(text, (111, floor.y + 10))  

                    # else:
                    # pygame.mixer.Sound.play(ding_sound)
            
                    # return
                
       
        
