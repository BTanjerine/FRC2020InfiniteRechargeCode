import wpilib
from wpilib import SmartDashboard
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler

from robotMap import RobotMap
from helper import Creator
from oi import OI

from subsystems.drive import Drive

from commands.teleop import TeleOp


class Robot(CommandBasedRobot):

    def robotInit(self):
        super().__init__(self)
        # init robot subs and commands

        self.Creator = Creator()  # program to create robot parts for subs
        self.botMap = RobotMap(self)
        self.oi = OI(self)

        self.drive = Drive(self)

        self.teleop = TeleOp(self)

        self.Drive = Drive(self)

        self.selectedAuto = None

        self.s = Scheduler

    def robotPeriodic(self):
        self.s.getInstance().run()  # run auto

    def log(self):
        pass

    def autonomousInit(self):
        # choose auto program
        """self.selectedAuto.cancel()
        self.selectedAuto = self.chooser.getSelected()  # find what auto was selected
        self.selectedAuto.start()   # start chosen auto"""
        pass

    def autonomousPeriodic(self):
        # cut auto if fail and go to driver
        """if self.OI.getMainController().getStartButton():
            self.selectedAuto.cancel()
            self.selectedAuto = self.teleOp
            self.selectedAuto.start()

        # self.s.getInstance().run()   # run auto
        self.log()  # log important data on to smartdashboard"""
        pass

    def teleopInit(self):
        # stops old auto and goes to teleop
        # self.selectedAuto.cancel()
        self.teleop.start()     # start teleop"""

    def teleopPeriodic(self):
        # self.log()  # log important data on to smartdashboard
        self.log()

    def disabledInit(self):
        pass  # nothing

    def disabledPeriodic(self):
        # self.log()  # log important data on to smartdashboard
        pass


if __name__ == '__main__':
    wpilib.run(Robot)