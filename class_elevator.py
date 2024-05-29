import pygame


class Elevator():
    def __init__(self, num) -> None:
        self.__current_floor = 0
        self.__image = None
        
        
    def init_elevator(self, screen, elevator_location_h, elevator_location_w):
        image_elevator = '/home/mefathim/Documents/elv.png'
        img = pygame.image.load(image_elevator)
        image = pygame.transform.scale(img, (30, 30))
        image_rect = image.get_rect()
        image_rect.topleft = (elevator_location_w, elevator_location_h)
        screen.blit(image, image_rect)  
        pygame.display.flip()  
    
    
            
        
    def move_up(self):
       pass 
        
        
    def move_down(self):
        pass    






