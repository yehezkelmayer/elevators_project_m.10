import pygame
from collections import deque

ding_sound = 'ding.mp3'
green = (10, 240, 10)
red = (255, 0, 0)
color = (50, 180, 100)
ding_sound = pygame.mixer.Sound('ding.mp3')
elevator = None


class Elevator:
    def __init__(self, num):
        self.tasks_queue = deque([])
        self.rect = None
        self.image = None
        self.arrival_time = None
        self.current_wait_time = 0
        # self.start_time = None
        # self.travel_time =None


    def draw_elevator(self, screen, elevator_y, elevator_location_w):
        image_elevator = 'elv.png'
        img = pygame.image.load(image_elevator)
        self.image = pygame.transform.scale(img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.topleft = (elevator_location_w, elevator_y)
        screen.blit(self.image, self.rect)
        pygame.display.flip()
    
    def insert_task(self, destination , finish_time):
        self.tasks_queue.append((destination, finish_time))
    
    
    def pop_task(self):
        if self.tasks_queue:
            self.tasks_queue.popleft()

   