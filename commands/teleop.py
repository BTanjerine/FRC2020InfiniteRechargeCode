import wpilib
from wpilib.command import Command
from wpilib.command import Command
from subsystems.testelectronics import testElectronics


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

        if abs(x) < 0.9:
            x = 0

        self.robot.Drive.set(lftArc, rgtArc)

        if self.sideCon.getRawButton(1):
            self.robot.testMot.set(0, 0.7)
        else:
            self.robot.testMot.set(0, 0)

        if self.sideCon.getRawButton(2):
            self.robot.testMot.set(1, 0.7)
        else:
            self.robot.testMot.set(1, 0)

        if self.sideCon.getRawButton(3):
            self.robot.testMot.set(2, 0.75)
        else:
            self.robot.testMot.set(2, 0)

        if self.sideCon.getRawButton(4):
            self.robot.testMot.set(3, 0.7)
        else:
            self.robot.testMot.set(3, 0)

        if self.sideCon.getRawButton(5):
            self.robot.testMot.set(4, 0.7)
        else:
            self.robot.testMot.set(4, 0)

        if self.sideCon.getRawButton(6):
            self.robot.testMot.set(5, 0.7)
        else:
            self.robot.testMot.set(5, 0)

        if self.sideCon.getRawButton(7):
            self.robot.testMot.set(6, 0.7)
        else:
            self.robot.testMot.set(6, 0)

    def isFinished(self):
        return False
