import wpilib
from wpilib.command import Command


class Shooter(Command):
    def __init__(self, robot, dist):
        Command.__init__(self)

        self.robot = robot
        self.dist = dist
        self.s = 0
        self.i = 0

    def initialize(self):
        self.robot.Flywheel.flywheelPID.limitVal(self.speed)
        self.dist = self.robot.Limelight.getDistance() * 51.1
        self.s = self.robot.Flywheel.flywheelPID.setPoint(self.dist)

    def execute(self):
        self.Flywheel.set(self.s)

        if abs(self.Flywheel.flywheelPID.getError(self.dist)) < 10:
            self.i += 1

    def isFinished(self):
        return self.i == 10

    def end(self):
        self.Flywheel.flywheelPID.setPoint(0)
        self.Flywheel.set(0, 0)

