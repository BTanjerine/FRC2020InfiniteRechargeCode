import wpilib
import ctre
from wpilib.command import Subsystem
from wpilib import DigitalInput


class Conveyor(Subsystem):
    def __init__(self, robot):
        Subsystem.__init__(self, 'Conveyor')

        self.robot = robot
        self.blaser = DigitalInput(3)

        motors = {}

        self.map = self.robot.botMap

        for name in self.map.motorMap.motors:
            motors[name] = self.robot.Creator.createMotor(self.map.motorMap.motors[name])

        self.cMotors = motors

        for name in self.cMotors:
            self.cMotors[name].setInverted(self.map.motorMap.motors[name]['inverted'])
            self.cMotors[name].setNeutralMode(ctre.NeutralMode.Coast)

    def log(self):
        wpilib.SmartDashboard.putNumber('Infared Value', self.blaser.get())

    def set(self, pw):
        self.cMotors['conveyor1'].set(ctre.ControlMode.PercentOutput, pw)
        self.cMotors['conveyor2'].set(ctre.ControlMode.PercentOutput, pw)

    def stay(self, pw):
        self.cMotors['conveyor1'].set(ctre.ControlMode.PercentOutput, pw)
        self.cMotors['conveyor2'].set(ctre.ControlMode.PercentOutput, -pw)

    def getblaser(self):
        y = self.blaser.get()
        return y

