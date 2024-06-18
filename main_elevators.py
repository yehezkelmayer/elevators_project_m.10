import pygame 
from building import Building
from elevator import Elevator
from floor import Floor
pygame.init()

  
num_floors = 15
num_elevators = 4


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