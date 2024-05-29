import pygame 
from class_building import Building
from class_elevator import Elevator
from class_floor import Floor

num_floors = int(input("choose a number of floors:"))
while not 0 < num_floors <= 50:
    num_floors = int(input(" please choose a number between 0 and 50:"))
num_elevators = int(input("choose a number of elevators:")) 
while not 0 < num_elevators <= 30 :
    num_floors = int(input(" please choose a number between 0 and 30:"))
  


# def_colors
black = (0, 0, 0)
white = (250, 250, 250)
color = (200, 100, 170)

# d
width = 400 + 30 * num_elevators
height = 400 + 30 * num_floors


# init_name
pygame.display.set_caption("elevator game")

# init_game_screen
screen = pygame.display.set_mode((width, height))
screen.fill(color)


# pygame.draw.rect(screen, (250, 250, 250), (20, 15, 40, 30))

#show_elevators
# item = Elevator(1)
# item.init_elevator(screen, height - 70)


builder1 = Building(num_floors, num_elevators)  
builder1.build(screen, height)  
builder1.build1(screen, height)    


#show_floors
# a = Floor(0)
# a.init_floor(screen, height - 70)



#move_image







pygame.display.flip()


# clock = pygame.time.Clock()


# screen_loop
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    


pygame.quit()


