#! /usr/bin/env python

import pygame
import sys
import time
import math
import os
import numpy as np
from random import uniform
from pygame.locals import *
import glob

image_cache = {}
def get_image(key):
	if not key in image_cache:
		image_cache[key] = pygame.image.load(key)
	return image_cache[key]

windowwidth = 256
windowheight = 240
music = 'music.mp3'
empty = (0,0,0,0)

lyrics = ["For a second", "I realize", "That I'm holding", "a hollow dice", "And what lies", "before me doesn't", "fright", "A first sense of", "a common place", "The only wind", "that illuminates", "Folding endlessly", "before my eyes"]

pygame.init()
font = pygame.font.Font(os.path.join("font.ttf"), 8)
run = 1

screen = pygame.display.set_mode((windowwidth, windowheight), pygame.NOFRAME|pygame.DOUBLEBUF, 32)
pygame.display.set_caption("demo")
pygame.mouse.set_visible(False)

images = glob.glob('*.png')

for image in images:
	get_image(image)

print images[0]

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

startdate = time.time()
while run:
	curtime = time.time() - startdate
	#print curtime
	keys=pygame.key.get_pressed()
	event=pygame.event.poll()
	if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
		run=0

	screen.blit(get_image('twinbee.png'), (0,-1856 + int(curtime * 25)))
	screen.blit(get_image('mockup.png'), (0, 0))
	#screen.blit(font.render("For a second", 0, (0, 0, 0)), (72, 192))
	#screen.blit(font.render("I realize", 0, (0, 0, 0)), (72, 200))
	print (int(curtime * 10) - 10)
	if curtime > 1:
		screen.blit(font.render(lyrics[0][:(int(curtime * 10) - 10)], 0, (0, 0, 0)), (72, 184))
	if curtime > (1 + float(len(lyrics[0])) / 10):
		screen.blit(font.render(lyrics[1][:(int(curtime * 10) - (len(lyrics[0]) + 10))], 0, (0, 0, 0)), (72, 192))

	pygame.display.flip()