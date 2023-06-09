# Raspberry Pi Robot Control

This Python code allows you to control a robot using a Raspberry Pi and various components such as motors, LEDs, and an ultrasonic sensor. The code utilizes the RPi.GPIO library for GPIO control.

## Note

 This code is still a work in progress and is being updated. Additional features and improvements are planned for future updates.

## Features

- Autonomous Mode: The robot can operate autonomously using the ultrasonic sensor to detect obstacles and adjust its movement accordingly.
- Manual Mode: You can manually control the robot's movement by selecting the desired direction from the menu.

## Components Used

- Ultrasonic Sensor: Connected to GPIO pins Echo (pin 23) and Trig (pin 24). It measures the distance to obstacles using sound waves.
- LEDs: A red LED connected to GPIO pin 18. It indicates the presence of obstacles when the distance measured by the ultrasonic sensor is below a certain threshold.
- Motors: Four motors connected to GPIO pins MotorLF (pin 26), MotorRF (pin 20), MotorLB (pin 19), and MotorRB (pin 21). They control the robot's movement in different directions.

## Usage

1. Connect the required components (ultrasonic sensor, LEDs, and motors) to the appropriate GPIO pins on the Raspberry Pi.
2. Run the Python code on the Raspberry Pi.
3. Select the desired driving mode (autonomous or manual) from the menu.
4. If in manual mode, choose the direction (forward, backward, left, right) for the robot to move.
5. In autonomous mode, the robot will move and adjust its direction based on the obstacle detection by the ultrasonic sensor.
6. The distance measured by the ultrasonic sensor and the status of the LED indicator will be displayed.

Feel free to modify and adapt the code according to your specific robot configuration and requirements.

## Requirements

- Raspberry Pi board
- RPi.GPIO library
- Ultrasonic sensor
- LEDs
- Motors

