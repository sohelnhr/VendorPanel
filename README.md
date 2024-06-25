Toy Robot Challenge
Introduction
The Toy Robot Challenge is a simulation of a toy robot moving on a square tabletop of dimensions 5x5 units. The challenge is to read commands of the following form and execute them accordingly:

PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
The aim is to develop a system that can take these commands, either through a command line interface, a graphical user interface, or a web API, and execute them to control the robot's actions on the tabletop.

Features
Command-Line Interface: Interact with the robot through command line inputs.
Error Handling: Robust error handling to prevent the robot from falling off the table.
Flexible Input: Supports multiple input methods including direct CLI commands and input files.
Logging: Detailed logs of robot movements and errors.
GUI (Optional): A simple graphical user interface to visualize the robot's movements on the tabletop.

Commands
PLACE X,Y,F: Place the robot on the table in position X,Y and facing NORTH, SOUTH, EAST, or WEST.
MOVE: Move the robot one unit forward in the direction it is currently facing.
LEFT: Rotate the robot 90 degrees to the left without changing its position.
RIGHT: Rotate the robot 90 degrees to the right without changing its position.
REPORT: Announce the X,Y and F of the robot.