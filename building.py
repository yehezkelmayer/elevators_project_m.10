import pygame
import time
from floor import Floor
from elevator import Elevator

# Initialize pygame
pygame.init()

# Constants
speed = 3.6
green = (10, 240, 10)
red = (255, 0, 0)
black = (0, 0, 0)
white = (250, 250, 250)
color = (50, 180, 100)
ding_sound = pygame.mixer.Sound('ding.mp3')
wait_time1 = 2  

class Building:
    def __init__(self, num_of_floors, num_of_elevators):
        self.floors = [Floor(i) for i in range(num_of_floors + 1)]
        self.elevators = [Elevator(i) for i in range(num_of_elevators)]
        

    def build_floors(self, screen, height):
        current_height = height
        for floor in self.floors:
            floor.draw_floor(screen, current_height - 70, floor)
            current_height -= 37

    def build_elevators(self, screen, height, x=200):   
        for elevator in self.elevators:
            elevator.draw_elevator(screen, height - 70, x)
            elevator.arrival_time = None 
            elevator.current_wait_time = 0  
            x += 30

    def find_elevator(self, floor):
        for elevator in self.elevators:
            if any(task[0] == floor.rect.centery for task in elevator.tasks_queue):
                return None  

        best_elevator = None
        shortest_time = float('inf')
        travel_time = 0
        for elevator in self.elevators:
            if elevator.tasks_queue:
                last_destination = elevator.tasks_queue[-1][0]
                current_distance = abs(floor.rect.centery - last_destination)
            else:
                last_destination = elevator.rect.centery
                current_distance = abs(floor.rect.centery - last_destination)
            
            travel_time = current_distance

            if elevator.arrival_time:
                additional_time = max(wait_time1 - (time.time() - elevator.arrival_time), 0)
            else:
                additional_time = 0

            current_queue_time = 0
            if elevator.tasks_queue:
                current_queue_time = elevator.tasks_queue[-1][1] + wait_time1 * 74
            
            total_time = current_queue_time + travel_time + additional_time
            if total_time < shortest_time:
                shortest_time = total_time
                best_elevator = elevator
        
        if best_elevator:
            best_elevator.insert_task(floor.rect.centery, shortest_time)  
            return best_elevator

    def calculate_time(self, elevator, floor):
        current_position = elevator.rect.centery
        travel_time = 0
        wait_time = 0
        tasks_queue = elevator.tasks_queue.copy()

        for task in tasks_queue:
            task_destination = task[0]
            travel_distance = abs(task_destination - current_position)
            travel_time += travel_distance / 74

            if task_destination == floor.rect.centery:
                return travel_time + elevator.current_wait_time

            current_position = task_destination
            wait_time += wait_time1 

        final_travel_distance = abs(floor.rect.centery - current_position)
        travel_time += final_travel_distance / 74
        return travel_time + wait_time + (elevator.current_wait_time - elevator.start_time)

    def move(self, screen, button, new_click):

        if new_click:
            for floor in self.floors:
                if floor.button.collidepoint(button):
                    assigned_elevator = self.find_elevator(floor)
                    if assigned_elevator:
                        floor.timer = True
                        floor.button_color = green

        for elevator in self.elevators:
            if elevator.tasks_queue:
                destination = elevator.tasks_queue[0][0]
                distance = destination - elevator.rect.centery

                if abs(distance) >= speed:
                    if not elevator.arrival_time: 
                        elevator.start_time = time.time()
                        move_step = speed if distance > 0 else -speed
                        elevator.rect.centery += move_step
                else:
                    elevator.rect.centery = destination
                    if not elevator.arrival_time:
                        pygame.mixer.Sound.play(ding_sound)
                        elevator.arrival_time = time.time() 
                        elevator.current_wait_time = wait_time1

                    

                    if time.time() - elevator.arrival_time >= wait_time1:
                        elevator.pop_task()
                        elevator.arrival_time = None  
                        elevator.current_wait_time = 0
                        elevator.start_time = None

                    for floor in self.floors:
                        if floor.rect.centery == destination:
                            floor.button_color = red
                            floor.timer = None

        screen.fill(color)
        
        for elevator in self.elevators:
            screen.blit(elevator.image, elevator.rect)
        
        for floor in self.floors:
            screen.blit(floor.image, floor.rect)
            pygame.draw.line(screen, black, [40, floor.y - 4], [190, floor.y - 4], width=7)
            pygame.draw.circle(screen, (floor.button_color), (115, floor.y + 17), 13)
            font = pygame.font.Font(None, 25)
            text = font.render(f"{floor.floor_number}", True, white)
            screen.blit(text, (111, floor.y + 10))

            # Display_timer
            if floor.timer:
                for elevator in self.elevators:
                    if elevator.tasks_queue:
                        if any(task[0] == floor.rect.centery for task in elevator.tasks_queue):
                            remaining_time = self.calculate_time(elevator, floor)
                            time_text = font.render(f"{remaining_time:.1f}", True, (250, 250, 250))
                            screen.blit(time_text, (8, floor.rect.centery - 10))  

        pygame.display.flip()
        pygame.time.Clock().tick(60)

