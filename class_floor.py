import pygame
pygame.init()
from class_elevator import Elevator




class Floor():
    def __init__(self, floor_num) -> None:
       
        self.floor_number = floor_num
        self.button = None
        self.button_color = (255, 0, 0)
        self.clock = 0
        self.rect = None
        self.y = None
        self.timer = None
        
        
      
    def init_floor(self, screen, floor_location, floor_num):
        
        pygame.draw.line(screen,(0, 0, 0), [40, floor_location - 4], [190, floor_location - 4], width=7)
        
        image_floor = 'Pasted image (3).png' 
        img = pygame.image.load(image_floor)
        self.image = pygame.transform.scale(img, (150, 30))
        self.rect = self.image.get_rect()
        self.rect.topleft = (40, floor_location)
        screen.blit(self.image, self.rect)  
        self.y = floor_location
        
        
        circle_radius = 13

        # pygame.draw.rect(screen, self.button_color, self.rect)
        self.button = pygame.draw.circle(screen, (self.button_color), (115, floor_location + 17), circle_radius )

        font = pygame.font.Font(None, 25)
        text = font.render(f"{floor_num}", True, (250, 250, 250))
        screen.blit(text, (111, floor_location + 10))  
        # self.timer(screen, 2)
        
        
        pygame.display.flip()
    
    def __str__(self) -> str:
        return f'{self.floor_number}'


    # def show_timer(self, screen, elevator):
    #     if elevator.timer == True:
    #         font = pygame.font.Font(None, 25)
    #         text = font.render(f"{elevator.time_to_arrival:.1f}", True, (250, 250, 250))
    #         screen.blit(text, (11, self.y + 10))
