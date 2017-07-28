import pygame
import time
import random
pygame.init()

sound = pygame.mixer.Sound("sounds/crash.wav")
# giới hạn màn hình
display_width = 800
display_hieght = 600

car_width = 40
car_height = 45

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
car_img = pygame.image.load("image/racecar1.png")
pygame.display.set_icon(car_img)
clock = pygame.time.Clock()
# crashed = False

pause = True
## xử lý di chuyển

car_speed = 0
# vị trí mặc định của oto
def car(x,y):
	screen_display.blit(car_img,(x,y))
### score
def scoreNumThing(text,score,pos_x,pos_y,font_size = 25):
	font = pygame.font.SysFont("comicsansms",font_size)
	text = font.render(text + " ",True,block_color)
	screen_display.blit(text,(pos_x,pos_y))
	scoreNum = font.render(str(score),True,red_light)
	screen_display.blit(scoreNum,(pos_x + 80,pos_y))
### Thêm đồ vật
def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(screen_display,color,[thingx, thingy, thingw, thingh])

def textShow(text,font):
	textSurface = font.render(text,True,black)
	return textSurface,textSurface.get_rect()

# def showMessage(text):
# 	size_text = pygame.font.SysFont('comicsansms',115)
# 	text_surf, text_rect = textShow(text,size_text)
# 	text_rect.center = ((display_width/2),(display_hieght/2)) # vị trí hiển thị chữ
# 	screen_display.blit(text_surf,text_rect)
# 	pygame.display.update()

# 	time.sleep(1)
# 	for event in pygame.event.get():
# 		if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN :
# 			if event.button == 3:
# 				gameRun()
def addTextOnScreen(text,width,height,font_size = 20):
	size_text = pygame.font.SysFont('comicsansms',font_size)
	text_surf, text_rect = textShow(text,size_text)
	text_rect.center = ((width),(height))
	screen_display.blit(text_surf,text_rect)
	# pygame.display.flip()

def button(text,pos_x,pos_y,width,height,color,hover_color,action = None):
	muose = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if pos_x + width > muose[0] > pos_x and pos_y + height > muose[1] > pos_y:
		pygame.draw.rect(screen_display,hover_color,(pos_x,pos_y,width,height))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(screen_display, color, (pos_x, pos_y, width, height))
	addTextOnScreen(text,pos_x + (width / 2), pos_y + (height / 2))

def crash():

	pygame.mixer.Sound.play(sound)
	pygame.mixer.music.stop()
	addTextOnScreen("You Lose!", display_width / 2, display_hieght / 2 - 100, 115)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		button("Play again!",150,350,100,50,organge,bright_green,gameRun)
		button("Home",350,350,100,50,brown,light_brown,gameIntroduc)
		button("Quit",550,350,100,50,green_light,light_blue,quitGame)
		pygame.display.update()
		clock.tick(25)
def quitGame():
	pygame.quit()
	quit()
def gameUnpause():
	global pause
	pause = False
def gamePause():

	pygame.mixer.music.pause()

	addTextOnScreen("Pause",display_width/2,display_hieght/2 - 100,115)
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		button("Continue!",150,350,100,50,white,yellow,gameUnpause)
		button("Home",350,350,100,50,brown,light_brown,gameIntroduc)
		button("Quit",550,350,100,50,green_light,light_blue,quitGame)

		pygame.display.update()
		clock.tick(25)
## giới thiệu game
def gameIntroduc():
	introduc = True
	while introduc:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		screen_display.fill(white_gray)
		size_text = pygame.font.SysFont('comicsansms',105)
		text_surf, text_rect = textShow("Dogged color",size_text)
		text_rect.center = ((display_width/2),(display_hieght/2 - 100))
		screen_display.blit(text_surf,text_rect)

		addTextOnScreen("Click p stop game.",(display_width/2),(display_hieght/2 + 250),20)
		########### HOVER ANIMATION MUOSE
		button("Go!",150,350,100,50,green,bright_green,gameRun) # play
		button("Quit.",550,350,100,50,yellow,light_blue,quitGame) # quit

		pygame.display.update()
		clock.tick(25)

def gameRun():

	global pause

	pygame.mixer.music.load('sounds/jazz.wav')
	pygame.mixer.music.play(-1)

	pos_x = (display_width * 0.45)
	pos_y = (display_hieght * 0.8)
	pos_x_change = 0
	pos_y_change = 0
	### xử lý đồ vật.
	thing_height = 50
	thing_width = 30
	thing_start_x11 = random.randrange(0,(display_width - 30))
	thing_start_x12 = random.randrange(0,(display_width - 30))
	thing_start_x13 = random.randrange(0,(display_width - 30))
	thing_start_y1 = -600
	thing_start_x2 = -800
	thing_start_y2 = random.randrange(0,display_hieght - 50)
	thing_speed = 5

	### score
	score = 0
	thing_count = 1
	#####
	game_exit = False
	while not game_exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			## event key----
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					pos_x_change = -3
				if event.key == pygame.K_RIGHT:
					pos_x_change = 3
				if event.key == pygame.K_UP:
					pos_y_change = -3
				if event.key == pygame.K_DOWN:
					pos_y_change = 3
				if event.key == pygame.K_p:
					pause = True
					gamePause()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					pos_x_change = 0
					pos_y_change = 0
			#######
		## move
		pos_x += pos_x_change
		pos_y += pos_y_change
		screen_display.fill(white_gray)

		## khoi dong do vat
		if int(thing_count) == 2:
			things(thing_start_x12,thing_start_y1,thing_width,thing_height,red)
		elif int(thing_count) == 3:
			things(thing_start_x12,thing_start_y1,thing_width,thing_height,red)
			things(thing_start_x13,thing_start_y1,thing_width,thing_height,yellow)
		things(thing_start_x11,thing_start_y1,thing_width,thing_height,blue)
		thing_start_y1 += (thing_speed - 3)
		things(thing_start_x2,thing_start_y2,thing_width,thing_height,green)
		thing_start_x2 += (thing_speed - 3)
		car(pos_x,pos_y)
		scoreNumThing("Score:",score,0,0)
		scoreNumThing("Level:",int(thing_count),3,40)
		### xu va cham voi man hinh
		if pos_y >= display_hieght - (car_height + 1):
			pos_y = (display_hieght * 0.92)
		if pos_x > display_width - car_width or pos_x < 0 or pos_y < 0:
			crash()

		if thing_start_y1 > display_hieght :
			thing_start_y1 = 0 - display_hieght
			thing_start_x11 = random.randrange(0,(display_width - 30))
			thing_start_x12 = random.randrange(0,(display_width - 30))
			thing_start_x13 = random.randrange(0,(display_width - 30))
			score += 1
			thing_count += 0.1
			thing_speed += 0.2
			thing_width += (score * 0.2)
		if thing_start_x2 > display_width :
			thing_start_x2 = 0 - display_width
			thing_start_y2 = random.randrange(0,display_hieght - 50)
			score += 1
			thing_count += 0.1
			thing_speed += 0.3
			thing_height += (score * 0.2)
		#######

		##### SCORE
		if (pos_y < thing_start_y1 and pos_y + car_height > thing_start_y1) or (pos_y < thing_start_y1 + thing_height and pos_y > thing_start_y1):
			# print("X------")
			if (pos_x < thing_start_x11 and pos_x + car_width > thing_start_x11) or (pos_x < thing_start_x11 + thing_width and pos_x > thing_start_x11):
				 crash()
			if int(thing_count) == 2:
				if (pos_x < thing_start_x12 and pos_x + car_width > thing_start_x12) or (pos_x < thing_start_x12 + thing_width and pos_x > thing_start_x12):
					 crash()
			elif int(thing_count) == 3:
				if (pos_x < thing_start_x12 and pos_x + car_width > thing_start_x12) or (pos_x < thing_start_x12 + thing_width and pos_x > thing_start_x12):
					 crash()
				if (pos_x < thing_start_x13 and pos_x + car_width > thing_start_x13) or (pos_x < thing_start_x13 + thing_width and pos_x > thing_start_x13):
					 crash()
		if (pos_x < thing_start_x2 and pos_x + car_width > thing_start_x2) or (pos_x < thing_start_x2 + thing_width and pos_x > thing_start_x2):
			# print("X2")
			if (pos_y < thing_start_y2 and pos_y + car_height > thing_start_y2) or (pos_y < thing_start_y2 + thing_height and pos_y > thing_start_y2):
				# print("y y 2")
				crash()
		pygame.display.update()
		clock.tick(120)
        ####

def main():
	gameIntroduc()
	gameRun()
	pygame.quit()
	quit()
if __name__ == '__main__':
	main()
