import pygame
from class_floor import Floor

ding_sound = 'ding.mp3'
elevator_speed = 5

class Elevator():
    def __init__(self, num) -> None:
        self.current_floor = num
        self.rect = None 
        self.image = None 
        # self.y = None
    
    
    
    def init_elevator(self, screen, elevator_y, elevator_location_w):
        image_elevator = 'elv.png'
        img = pygame.image.load(image_elevator)
        self.image = pygame.transform.scale(img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.topleft = (elevator_location_w, elevator_y)
        screen.blit(self.image, self.rect)  
        pygame.display.flip()  
    
    # def move(self, new_y):
    #     while self.rect.y != new_y:
    #         self.rect.y -= 10
        
    


     





