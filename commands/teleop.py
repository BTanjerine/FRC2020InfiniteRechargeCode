import wpilib
from wpilib.command import Command
from wpilib.command import Command


class TeleOp(Command):
    def __init__(self, robot):
        Command.__init__(self)
        self.robot = robot  # access robot values

        self.controller = robot.oi.getMainController()  # get controller class
        self.sideCon = robot.oi.getSideController()     # get side controller class

    def execute(self):
        y = -self.controller.getY(self.controller.Hand.kLeftHand)  # drive y axis percent output
        x = self.controller.getX(self.controller.Hand.kRightHand)  # drive x axis percent output

        rgtArc = y - x
        lftArc = y + x

        if abs(rgtArc) < 0.05:
            rgtArc = 0
        if abs(lftArc) < 0.05:
            lftArc = 0

        self.robot.Drive.set(lftArc, rgtArc)

    def isFinished(self):
        return False


