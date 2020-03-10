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
        joyFly = self.sideCon.getRawButton(3)
        joyTur = self.sideCon.getRawAxis(1)
        joyIn = self.controller.getAButton()
        joyUp = self.sideCon.getRawButton(7)
        joyStay = self.sideCon.getRawButton(8)
        joyDown = self.sideCon.getRawButton(9)

        rgtArc = 0 # y - x
        lftArc = 0 # y + x

        if abs(rgtArc) < 0.05:
            rgtArc = 0
        if abs(lftArc) < 0.05:
            lftArc = 0

        if abs(x) < 0.9:
            x = 0

        self.robot.Drive.set(lftArc, rgtArc)

        if joyIn:
            self.robot.Intake.setIntake(0.9)
        else:
            self.robot.Intake.setIntake(0)

        if joyFly:
            self.robot.Flywheel.set(self.robot.Flywheel.setVelocityPID(460))
        elif self.sideCon.getRawButton(2):
            self.robot.Flywheel.set(0.6)
        else:
            self.robot.Flywheel.set(0)

        if joyUp:
            self.robot.Conveyor.set(0.9)
        elif joyDown:
            self.robot.Conveyor.set(-0.8)
        elif joyStay:
            self.robot.Conveyor.stay(0.3)
        else:
            self.robot.Conveyor.set(0)

        if joyTur:
            self.robot.Turret.setPower(0.6)
        else:
            self.robot.Turret.setPower(0)

    def isFinished(self):
        return False
