import wpilib
from wpilib.command import Command


class Movement(Command):
    def __init__(self, robot, dist, speed, angle):
        Command.__init__(self)
        self.robot = robot
        self.dist = dist
        self.speed = speed
        self.angle = angle
        self.i = 0
        self.s = 0

    def initialize(self):
        self.robot.Drive.resetGryo()
        self.robot.Drive.resetEnc()
        self.robot.Drive.DrivePID.setPoint(5)
        self.robot.Drive.DrivePID.limitVal(self.speed)
        self.robot.Drive.setSpeed(self.OUT)

    def execute(self):
        turn = self.Drive.DrivePID.outVal(self.Drive.getAngle())
        move = self.Drive.DrivePID.outVal(self.Drive.getEnc())
        rgt = move - turn
        lft = move + turn
        self.robot.Drive.set(rgt, lft)

        if abs(rgt) < 0.1:
            self.i += 1

    def isFinished(self):
        return self.i == 10

    def end(self):
        self.i = 0
        self.robot.Drive.stop()
        self.robot.Drive.resetEnc()
