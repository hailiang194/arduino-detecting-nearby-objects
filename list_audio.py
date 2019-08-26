import information
	
def get_digit_audio_file(digit):
	
	digitFile = ("","one.mp3","two.mp3", "three.mp3", "four.mp3","five.mp3",
				"six.mp3","seven.mp3","eight.mp3", "nine.mp3"
		)

	if(digit == 0 or digit >= 10):
		return ""

	return information.AUDIO_DIGITS_FOLDER + digitFile[digit]

def get_list_audio_number(number):
	
	lstAudio = []

	if(number == 0):
		lstAudio.append(information.AUDIO_DIGITS_FOLDER + "zero.mp3")

	hundred = number // 100
	ten = (number % 100) // 10
	unit = number % 10

	#process hundred
	if(hundred > 0):
		lstAudio.append(get_digit_audio_file(hundred))
		lstAudio.append(information.AUDIO_SUFFIXES_FOLDER + "hundred.mp3")

	#process ten
	if(ten == 0):
		if(unit == 0):
			return lstAudio
		if(hundred > 0):
			lstAudio.append(information.AUDIO_SUFFIXES_FOLDER + "and.mp3")
		
		lstAudio.append(get_digit_audio_file(unit));

		return lstAudio

	#if ten != 0
	if(ten == 1):
		lstAudio.append(information.AUDIO_DIGITS_FOLDER + "ten.mp3")
	else:
		lstAudio.append(get_digit_audio_file(ten))
		lstAudio.append(information.AUDIO_SUFFIXES_FOLDER + "_ty.mp3")


	if(unit > 0):
		lstAudio.append(get_digit_audio_file(unit))

	return lstAudio

def get_list_detected_object(minDistanceAngle, minDistance):
	lstNofiti = []

	#lstNofiti.append(information.AUDIO_DETECTED_FOLDER + "notify-header.mp3")
	#lstNofiti.append(get_list_audio_number(minDistance))
	for audioFile in get_list_audio_number(minDistance):
		lstNofiti.append(audioFile)
	lstNofiti.append(information.AUDIO_UNIT_FOLDER + "centimeter.mp3")	

	lstNofiti.append(information.AUDIO_DETECTED_FOLDER + "at-the-corner.mp3")
	
	#lstNofiti.append(get_list_audio_number(minDistanceAngle))
	for audioFile in get_list_audio_number(minDistanceAngle):
		lstNofiti.append(audioFile)

	lstNofiti.append(information.AUDIO_UNIT_FOLDER + "degree.mp3")

	return lstNofiti

def get_list_undetected_object():
	lstNofiti = []
	lstNofiti.append(information.AUDIO_UNDETECTED_FOLDER + "no-object.mp3")

	return lstNofiti

def get_list_notification(minDistanceAngle, minDistance):
	if(minDistance >= information.INFINITY):
		return get_list_undetected_object() 
	else:
		return get_list_detected_object(minDistanceAngle, minDistance)