class ToyRobot:
    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None
        self.directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
        
    def place(self, x, y, f):
        if 0 <= x < 5 and 0 <= y < 5 and f in self.directions:
            self.x = x
            self.y = y
            self.facing = f

    def move(self):
        if self.x is None or self.y is None:
            return
        if self.facing == 'NORTH' and self.y < 4:
            self.y += 1
        elif self.facing == 'SOUTH' and self.y > 0:
            self.y -= 1
        elif self.facing == 'EAST' and self.x < 4:
            self.x += 1
        elif self.facing == 'WEST' and self.x > 0:
            self.x -= 1

    def left(self):
        if self.facing:
            self.facing = self.directions[(self.directions.index(self.facing) - 1) % 4]

    def right(self):
        if self.facing:
            self.facing = self.directions[(self.directions.index(self.facing) + 1) % 4]

    def report(self):
        if self.x is not None and self.y is not None:
            return f"{self.x},{self.y},{self.facing}"
        return "Not placed on the board."

if __name__ == "__main__":
    robot = ToyRobot()
    print("Toy Robot Simulator. Type 'QUIT' to exit.")
    
    while True:
        command = input("Enter command: ")
        if command == "QUIT":
            print("Exiting Toy Robot Simulator.")
            break
        if command.startswith("PLACE"):
            _, x, y, f = command.split()
            robot.place(int(x), int(y), f)
        elif command == "MOVE":
            robot.move()
        elif command == "LEFT":
            robot.left()
        elif command == "RIGHT":
            robot.right()
        elif command == "REPORT":
            print(robot.report())
