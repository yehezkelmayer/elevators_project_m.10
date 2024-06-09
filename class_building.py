import pygame
from class_floor import Floor
from class_elevator import Elevator

# Initialize pygame
pygame.init()

# Constants
speed = 1
green = (10, 240, 10)
red = (255, 0, 0)
color = (50, 180, 100)
ding_sound = pygame.mixer.Sound('ding.mp3')
elevator = None


class Building:
    def __init__(self, num_of_floors, num_of_elevators):
        self.floors = [Floor(i) for i in range(num_of_floors + 1)]
        self.elevators = [Elevator(i) for i in range(num_of_elevators)]
        self.current_elevator = None
        self.current_floor = None


    def build_floors(self, screen, height):
        current_height = height
        for floor in self.floors:
            floor.init_floor(screen, current_height - 70, floor)
            current_height -= 37
    
    def build_elevators(self, screen, height, a=200):   
        for elevator in self.elevators:
            elevator.init_elevator(screen, height - 70, a)
            a += 30



    def find_elevator(self, floor):
        best_elevator = None
        shortest_time = float('inf')
        for elevator in self.elevators:
            if elevator.tasks_queue:
                last_destination = elevator.tasks_queue[-1]
            else:
                last_destination = elevator.rect.centery
            
            current_distance = abs(floor.rect.centery - last_destination)
            travel_time = current_distance / (37 * 2)

            current_queue_time = 0
            for i in range(len(elevator.tasks_queue) - 1):
                current_queue_time += abs(elevator.tasks_queue[i] - elevator.tasks_queue[i + 1]) / (37 * 2)
                # current_queue_time += 2  

            total_time = current_queue_time + travel_time

            if total_time < shortest_time:
                shortest_time = total_time
                best_elevator = elevator

        if best_elevator:
            best_elevator.time_to_arrival += shortest_time
            best_elevator.insert_task(floor.rect.centery)
            return best_elevator

    def move(self, screen, button, new_click):
        if new_click:
            for floor in self.floors:
                if floor.button.collidepoint(button):
                    selected_elevator = self.find_elevator(floor)
                    selected_elevator.insert_task(floor.rect.centery)
                    floor.timer = True
                    # floor.show_timer(screen, selected_elevator)
                    floor.button_color = green

        for elevator in self.elevators:
            if elevator.tasks_queue:
                destination = elevator.tasks_queue[0]
                distance = destination - elevator.rect.centery

                if abs(distance) >= speed:
                    move_step = speed if distance > 0 else -speed
                    elevator.rect.centery += move_step

                    print(elevator.time_to_arrival)
                else:
                    elevator.rect.centery = destination
                    pygame.mixer.Sound.play(ding_sound)
                    elevator.pop_task()

                    for floor in self.floors:
                        if floor.rect.centery == destination:
                            floor.button_color = red
                            floor.timer = None

        for elevator in self.elevators:
            if elevator.time_to_arrival > 0:
                elevator.time_to_arrival -= 1 / 74  
                if elevator.time_to_arrival < 0:
                    elevator.time_to_arrival = 0

        screen.fill(color)
        
        for elev in self.elevators:
            screen.blit(elev.image, elev.rect)
        
        for flr in self.floors:
            screen.blit(flr.image, flr.rect)
            pygame.draw.line(screen, (0, 0, 0), [40, flr.y - 4], [190, flr.y - 4], width=7)
            pygame.draw.circle(screen, (flr.button_color), (115, flr.y + 17), 13)
            font = pygame.font.Font(None, 25)
            text = font.render(f"{flr.floor_number}", True, (250, 250, 250))
            screen.blit(text, (111, flr.y + 10))

            for elevator in self.elevators:
                if flr.timer:
                    if elevator.time_to_arrival > 0:
                        time_text = font.render(f"{elevator.time_to_arrival:.1f}", True, (250, 250, 250))
                        screen.blit(time_text, (10, flr.y + 10))  
            
        
        pygame.display.flip()
        pygame.time.Clock().tick(74)




