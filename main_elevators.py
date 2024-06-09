import pygame 
from class_building import Building
from class_elevator import Elevator
from class_floor import Floor
pygame.init()

# num_floors = int(input("choose a number of floors:"))
# while not 0 < num_floors <= 25:
#     num_floors = int(input(" please choose a number between 0 and 50:"))
# num_elevators = int(input("choose a number of elevators:")) 
# while not 0 < num_elevators <= 10 :
#     num_floors = int(input(" please choose a number between 0 and 30:"))
  
num_floors = 15
num_elevators = 6


# def_colors
black = (0, 0, 0)
white = (250, 250, 250)
red = (0, 0, 0)
green = (0, 255, 0)
color = (50, 180, 100)
ding_sound = pygame.mixer.Sound('ding.mp3')

# d
width = 250 + 30 * num_elevators
height = 300 + 30 * num_floors


# init_name
pygame.display.set_caption("elevator game")

# init_game_screen
screen = pygame.display.set_mode((width, height))
screen.fill(color)

#build_the_building
builder = Building(num_floors, num_elevators)  
builder.build_floors(screen, height)  
builder.build_elevators(screen, height)    

click_position = None
new_click = None

# screen_loop
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_position = event.pos
            new_click = True
    if click_position:
        finished = builder.move(screen, click_position, new_click)
        new_click = False
        pygame.display.flip()   
        if finished: click_position = None