import pygame



class Floor():
    def __init__(self, num) -> None:
       
        self.floor_number = None
        self.button_color = (20, 20, 20)
        self.clock = (70, 70, 70)
        

    def get_number(self):
        return self.floor_number
    


    def set_number(self):
        if not self.floor_number():
            self.floor_number = 0
        else:
            self.floor_number += 1    
            



    def init_floor(self, screen, floor_location):
        pygame.draw.line(screen,(0, 0, 0), [40, floor_location - 5], [190, floor_location - 5], width=7)
        image_floor = '/home/mefathim/Documents/Pasted image (3).png'
        img = pygame.image.load(image_floor)
        image = pygame.transform.scale(img, (150, 30))
        image_rect = image.get_rect()
        image_rect.topleft = (40, floor_location)
        screen.blit(image, image_rect)  
        pygame.display.flip()  
    




