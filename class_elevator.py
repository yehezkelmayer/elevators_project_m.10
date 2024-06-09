import pygame
from collections import deque

ding_sound = 'ding.mp3'
speed = 3
green = (10, 240, 10)
red = (255, 0, 0)
color = (50, 180, 100)
ding_sound = pygame.mixer.Sound('ding.mp3')
elevator = None


class Elevator:
    def __init__(self, num):
        self.tasks_queue = deque([])
        self.current_floor = num
        self.rect = None
        self.image = None
        self.time_to_arrival = 0
        # self.timer = None


    def init_elevator(self, screen, elevator_y, elevator_location_w):
        image_elevator = 'elv.png'
        img = pygame.image.load(image_elevator)
        self.image = pygame.transform.scale(img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.topleft = (elevator_location_w, elevator_y)
        screen.blit(self.image, self.rect)
        pygame.display.flip()
    
    def insert_task(self, destination):
        self.tasks_queue.append(destination)
    
    
    def pop_task(self):
        if self.tasks_queue:
            self.tasks_queue.popleft()

   