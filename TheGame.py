import pygame
from random import randint

#initialisation##############
gameDisplay = pygame.display.set_mode([800, 600])
cursor_green = [51,204,51]
white = [255,255,255]
pointer_red = [232, 72, 72, 25]
background = [255, 193, 151]
black = [0,0,0]
text_green = [7,165,28]
pygame.display.set_caption('The Game')
clock = pygame.time.Clock()
pygame.font.init()
#############################


#Loop_variables##############
gameExit = False
gameintro = True
gameOver = False
#############################

#functions###################
def msg(text, color, size, font_style, where):
	font = pygame.font.SysFont(font_style, size)
	to_be = font.render(text, True, color)
	gameDisplay.blit(to_be, where)

def game_intro():
	gameExit = False
	gameintro = True
	gameOver = False
	while gameintro:
		gameDisplay.fill(white)
		msg('The Game', text_green, 100, None, [235,100] )
		msg('Right-Click to continue', black, 50, None, [215, 180])

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				gameintro = False

		pygame.display.flip()


def gameover():
	gameOver = True
	while gameOver:
		gameDisplay.fill(white)
		msg('Well Done', text_green, 100, None, [235,100])
		msg('Right-Click to play again', black, 50, None, [200,180])
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				gameOver = False
				difficulty()
			elif event.type == pygame.QUIT:
				pygame.quit()
				quit()

def difficulty():
	Onthepage = True

	while Onthepage:
		pos = pygame.mouse.get_pos()
		gameDisplay.fill(white)
		msg('Choose the difficulty level',black, 50, None, [200, 100])
		
		#Boxes######
		pygame.draw.rect(gameDisplay, black, (50, 200, 170, 100), 2)
		msg('EASY',text_green, 30, None, [110, 240])

		pygame.draw.rect(gameDisplay, black, (300, 200, 170, 100), 2)
		msg('MEDIUM', text_green, 30, None, [345, 240])

		pygame.draw.rect(gameDisplay, black, (550, 200, 170, 100), 2)
		msg('HARD', text_green, 30, None, [605, 240])
		############

		#Click_logic#
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if 50<pos[0]<220 and 200<pos[1]<300:
					game('easy')

				elif 300<pos[0]<470 and 200<pos[1]<300:
					game('medium')

				elif 550<pos[0]<720 and 200<pos[1]<300:
					game('hard')


		#############
		

		#update#####
		pygame.display.flip()
		
		





def game(diffi):
	gameExit = False
	gameintro = True
	gameOver = False
	lead_x = 400
	lead_y = 300
	change = 1
	var = 40
	counter_width = 0
	pace = 10
	#Setting_difficulty####

	# if diffi == 'easy':
	# 	redu = 0
	# elif diffi == 'medium':
	# 	red = 5
	# elif diffi == 'hard':
	# 	red = 4


	#######################

	while not gameExit:
		while not gameOver:
			#initials###############
			gameDisplay.fill(background)
			cursor = pygame.draw.circle(gameDisplay, cursor_green, [lead_x,lead_y], 15, 0)
			msg('Keep the green dot inside the ring to score!', black, 20, None, [10,5])
			#pygame.display.update()
			########################

			#cursor###########
			rand1 = randint(1,101)
			if rand1 <= 50:
				for i in range(var):
					lead_x += change
			else:
				for i in range(var):
					lead_x -= change
			rand2 = randint(1,101)
			if rand2 <= 50:
				for i in range(var):
					lead_y -= change
			else:
				for i in range(var):
					lead_y += change

			#boundaries##############

			if lead_x < 15:
				for i in range(var+10):
					lead_x += change

			elif lead_x >= 784:
				for i in range(var+10):
					lead_x -= change

			elif lead_y < 15:
				for i in range(var+10):
					lead_y += change

			elif lead_y >= 540:
				for i in range(var+10):
					lead_y -= change

			clock.tick(20)

			#pointer#################

			pos = pygame.mouse.get_pos()
			
			pointer = pygame.draw.circle(gameDisplay, pointer_red, pos, 100, 10)	

			#logic###################

			
			if pos[0]-100<lead_x<pos[0]+100 and pos[1]-100<lead_y<pos[1]+100:
				if counter_width >=0:
					counter_width += pace
				elif counter_width <0:
					counter_width = 0

				if diffi == 'hard': 

					rand3 = randint(1,101)
					if rand3 <= 50:
						for i in range(var-10):
							lead_x += change
					else:
						for i in range(var-10):
							lead_x -= change
					rand4 = randint(1,101)
					if rand4 <= 50:
						for i in range(var-10):
							lead_y -= change
					else:
						for i in range(var-10):
							lead_y += change



			
			else:
				if counter_width >0:
					if diffi == 'medium':
						counter_width -= 5
					elif diffi == 'hard':
						counter_width -= 6

				

			#progress_logic################

			pygame.draw.rect(gameDisplay, black, [10, 550,counter_width, 30],0 )
			if counter_width >= 770:
				gameover()
				counter_width = 0


			#exit button###############
			for event in pygame.event.get():    
				if event.type == pygame.QUIT:
					gameOver = True
					gameExit = True
					pygame.quit()
					quit()
					
			###########################

			pygame.display.flip()



##############################




#calling######################
game_intro()
difficulty()
#game()

##############################




