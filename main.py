#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

encendido = False
# Write your program here
brick.sound.beep()

# Reproduce un pitido.
brick.sound.beep()
# Inicializa un motor en el puerto B.
test_motor = Motor(Port.B)
# Enciende el motor a una rapidez de 500 grados por segundo (º/s). Hasta girar un ángulo de 90 grados.
#test_motor.run_target(500, 90)
# Reproducir otro pitido.
while True:
    if Button.LEFT in brick.buttons():
        #encendido = True
        test_motor.run(500)
    if Button.RIGHT in brick.buttons():
        #encendido = False
        test_motor.stop(Stop.BRAKE)
    
    print (brick.buttons())

# Esta vez con un tono más alto (1000 Hz) y una duración más larga (500 ms).
brick.sound.beep(1000, 2000, 100)
