import pygame
import time
import random
pygame.init()


# giới hạn màn hình
display_width = 800
display_hieght = 600



## color
black = (0,0,0)
white = (255,255,255)
white_gray = (150,232,232)
red   = (255,0,0)
green = (234,91,91)
blue  = (13,13,255)
yellow = (0,255,0)
block_color = (53,115,255)
green_light = (120,229,135)
red_light = (242,100,100)
light_blue = (164,191,245)
bright_green = (220,165,165)
organge = (82,244,109)
brown = (140,57,57)
light_brown = (198,141,141)
### set Screen
screen_display = pygame.display.set_mode((display_width,display_hieght))
pygame.display.set_caption("Game debut")
clock = pygame.time.Clock()


def createSnake():
	length = 5
	snake = [[]]
	for i in range(0,length - 1):
		snake.append(i)
	for i in range(0,len(snake)):
		print(i)

def gameRun():
	game_exit = False
	while not game_exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			# ## event key----
			# if event.type == pygame.KEYDOWN:
			# 	if event.key == pygame.K_LEFT:
			# 		pos_x_change = -3
			# 	if event.key == pygame.K_RIGHT:
			# 		pos_x_change = 3
			# 	if event.key == pygame.K_UP:
			# 		pos_y_change = -3
			# 	if event.key == pygame.K_DOWN:
			# 		pos_y_change = 3
			# if event.type == pygame.KEYUP:
			# 	if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
			# 		pos_x_change = 0
			# 		pos_y_change = 0
		screen_display.fill(white)
		pygame.display.update()
		clock.tick(120)
        ####

def main():
	createSnake()
	pygame.quit()
	quit()
if __name__ == '__main__':
	main()
