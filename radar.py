import pygame
import math
import information

SOUND_ONLY_DISPLAY = (480, 360)

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)

RED = (225, 0, 0)
BLUE = (0, 0, 225)
GREEN = (0, 255, 0)

DIPLAY_WIDTH = 600
DIPLAY_HEIGHT = DIPLAY_WIDTH // 2


THICKNESS = DIPLAY_WIDTH // 100 * 2
DIV = 3

RADAR_DISPLAY = (DIPLAY_WIDTH, DIPLAY_HEIGHT)

CENTER = (DIPLAY_WIDTH // 2, DIPLAY_HEIGHT)

RAD = DIPLAY_HEIGHT

def convert(distance):
	return (distance * DIPLAY_HEIGHT // 100)

def get_point(angle, rad = RAD):
	return (rad * math.cos(get_angle_display(angle)) + CENTER[0], rad * math.sin(get_angle_display(angle)) + CENTER[1])


def get_angle_display(angle):
	return (- math.radians(angle))

def draw_full_line(radarSurface,color, angle, startPoint = CENTER, width = THICKNESS):
	pygame.draw.line(radarSurface, color, startPoint, get_point(angle), width)

def draw_object(radarSurface, angle, rawData):
	if(rawData[angle] == information.INFINITY or rawData[angle] == 0):
		return

	distance = rawData[angle]

	startPoint = get_point(angle, convert(distance))
	
	draw_full_line(radarSurface, RED, angle, startPoint)



def draw_radar_background(radarSurface):
	radarSurface.fill(BLACK)

	for i in range(DIV):
		rect = (DIPLAY_HEIGHT * i // DIV, DIPLAY_HEIGHT * i // DIV, DIPLAY_WIDTH * (DIV - i) // DIV, DIPLAY_WIDTH * (DIV - i) // DIV)
		pygame.draw.arc(radarSurface, GREEN, rect, 0, math.pi)

	draw_full_line(radarSurface, GREEN, 45, width = 1)
	draw_full_line(radarSurface, GREEN, 90, width = 1)
	draw_full_line(radarSurface, GREEN, 135, width = 1)

def draw_radar(radarSurface, currentAngle, rawData):
	draw_radar_background(radarSurface)

	for angle in rawData.keys():
		draw_object(radarSurface, angle, rawData)

	draw_full_line(radarSurface, WHITE, currentAngle)