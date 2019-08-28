import serial
import time
import pygame
import list_audio
import information
import sys
import radar

mode = ""

if(len(sys.argv) == 2):
	mode = sys.argv[1].upper()

displaySize = 0

if(mode == "SOUND"):
	displaySize = radar.SOUND_ONLY_DISPLAY
elif(mode == "RADAR"):
	displaySize = radar.RADAR_DISPLAY
else:
	print("WRONG ARGV")
	quit()

screenDisplay = pygame.display.set_mode(displaySize)
pygame.display.set_caption("RADAR PROJECT")

pygame.mixer.init()
time.sleep(3)

ser = serial.Serial('COM3',baudrate = 9600, timeout = 1)
rawData = {}

start = True;

def play_notification(minDistanceAngle, minDistance):
	for audioFile in list_audio.get_list_notification(minDistanceAngle, minDistance):
		pygame.mixer.music.load(audioFile)
		pygame.mixer.music.play()

		while pygame.mixer.music.get_busy():
			continue

def notify(angle):

	global rawData
	global start

	if((angle == 0) or (angle == 180)):
		minDis = min(rawData.values())
		if(start):
			start = False
			return;

		print('-' * 10)
		for angleRead in rawData.keys():
			if(rawData[angleRead] == minDis):
				print("MIN:\na = %d, d = %d" %(angleRead, minDis))
				play_notification(angleRead, minDis)
				break

def setup():
	for i in range(0, 181, 2):
		rawData[i] = 0

def update():

	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			pygame.quit()
			quit()

	data = ser.readline()
	dataStr = data.decode('utf-8')[:-2] #remove '\r\n'

	global start

	if(dataStr == ''):
		return

	inData = dataStr.split(':')

	scanAngle = int(inData[0])
	scanDistance = int(inData[1])

	print("a = %d, d = %d" %(scanAngle, scanDistance))

	rawData[scanAngle] = scanDistance

	if(mode == "SOUND"):
		notify(scanAngle)
		soundOnly = pygame.image.load("img\\sound-only.jpg")
		screenDisplay.blit(soundOnly, (0,0))
	if(mode == "RADAR"):
		radar.draw_radar(screenDisplay,scanAngle, rawData)

	pygame.display.flip()
	


def main():
	setup()

	while True:
		update()


if __name__ == '__main__':
	main()