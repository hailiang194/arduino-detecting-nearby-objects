import serial
import time
import pygame
import os
import list_audio
import information


pygame.mixer.init()
os.system("cls")
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

def setup():
	for i in range(0, 181, 2):
		rawData[i] = 0

def update():

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
	
	if((scanAngle == 0) or (scanAngle == 180)):
		minDis = min(rawData.values())
		if(start):
			start = False
			return;

		print('-' * 10)
		for angle in rawData.keys():
			if(rawData[angle] == minDis):
				print("MIN:\na = %d, d = %d" %(angle, minDis))
				play_notification(angle, minDis)
				break

def main():
	setup()

	while True:
		update()


if __name__ == '__main__':
	main()