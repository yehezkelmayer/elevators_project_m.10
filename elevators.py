import pygame as game

# refresh_rate = 60
# def_colors
black = (0, 0, 0)
white = (250, 250, 250)
color = (200, 100, 170)

# keep_image
image = '/home/mefathim/Documents/elv.png'

# init_name
game.display.set_caption("elevator game")

# init_game_window
screen = game.display.set_mode((700, 700), 0, 32)
screen.fill(color)
game.draw.rect(screen, (250, 250, 250), (20, 15, 40, 30))

# show_image
img = game.image.load(image)
image = game.transform.scale(img, (50, 50))
image_rect = image.get_rect()
image_rect.topleft = (35, 25)

screen.blit(image, image_rect)



game.display.flip()
# clock = game.time.Clock()

# window_loop
finish = False
while not finish:
    for event in game.event.get():
        if event.type == game.QUIT:
            finish = True
    




game.quit()


