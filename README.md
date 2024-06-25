Toy Robot Simulator

Description
The Toy Robot Simulator is a Python application that simulates a toy robot moving on a 5x5 square tabletop. The application reads commands from the user to place, move, rotate, and report the position of the robot ensuring the robot does not fall off the table.

Features
Place the robot on the table at a specific position facing North, South, East, or West.
Move the robot one unit forward in the direction it is facing.
Rotate the robot left or right without changing its position.
Report the position of the robot, including its location and the direction it is facing.

Prerequisites
Before you begin, ensure you have met the following requirements:

Docker installed on your machine
Python 3.8 or higher
Access to a Kubernetes cluster for deployment (optional)

Commands
PLACE X Y F: Places the robot at coordinates (X,Y) facing direction F.
MOVE: Moves the robot one unit in the direction it is currently facing.
LEFT: Rotates the robot 90 degrees to the left.
RIGHT: Rotates the robot 90 degrees to the right.
REPORT: Outputs the current position and facing of the robot.
