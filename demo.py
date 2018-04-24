#! /usr/bin/env python

import pygame
import time
import math
import os
import numpy as np
from random import uniform
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

	pygame.display.flip()
