#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import random

ev3 = EV3Brick()

while True:
    ult = UltrasonicSensor(Port.S2) #O sensor ultrasônico se encontrada no Port 1
    chance = random.randint(1, 20) # Gerar numeros aleatórios para trazer as chances

    print("Distancia -", ult.distance()) # Imprime a distancia do sensor
    print("Chance -", chance)

    #time.sleep(0.1)

    if ult.distance() <= 60: #Se a distancia do sensor for menor que 60.
        if chance == 1: # Se a chance gerar um numero igual a 1, então
            ev3.speaker.play_file("audio.wav") # solta o som estourado no EV3
        else:
            ev3.speaker.beep() #Apenas dará um beep se a chance não for igual a 1
    else:
        pass
