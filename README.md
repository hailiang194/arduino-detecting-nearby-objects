# ARDUINO - DETECTING NEARBY OBJECTS USING ULTRASONIC SENSOR
Using ultrasonic to detect objects that are near us

## COMPONENTS AND SUPPLIES
1. Arduino Uno
![Arduino Uno](https://giadungnhaviet.com/wp-content/uploads/2018/09/bo-mach-dieu-khien-arduino-r3-2.jpg)
2. Servo SG90
![Servo SG90](https://product.hstatic.net/1000292825/product/o-barco-acessorios-para-arduino-d_nq_np_687287-mlb25991415732_092017-f_master.jpg)
3. Ultrasonic sensor
![Ultrasonic sensor](https://www.makerlab-electronics.com/my_uploads/2016/05/ultrasonic-sensor-HCSR04-1.jpg)

## Schematics
[!board-design](ttps://user-images.githubusercontent.com/30114830/63929569-dbdd1c80-ca7b-11e9-82ce-d1fc055852f9.jpg)

## Install
1. clone this repository
```
git clone https://github.com/53k41iga/arduino-detecting-nearby-objects.git
```
2. second, vetify get-data/get-data.ino then upload it into Arduino
#### NOTE: 
make sure you have installed ```pyserial``` and ```pygame``` using COM3 port in this project
## Implementation
after installing into arduino, connect it to computer by USB and run main.py on terminal, cmd or Powershell. We have 2 mode in this project
#### SOUND
This mode will talk to you distance and angle from the nearest object that it detect.
```
python main.py SOUND
```
#### RADAR
This mode will draw a radar for you
```
python main.py RADAR
```
