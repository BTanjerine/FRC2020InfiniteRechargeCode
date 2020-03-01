import wpilib
import ctre
from wpilib.command import Subsystem


class testElectronics(Subsystem):
    def __init__(self, robot):
        Subsystem.__init__(self, 'testElectronics')

        self.robot = robot

        self.map = self.robot.botMap.motorMap

        tMotors = {}

        for name in self.map.motors:
            tMotors[name] = self.robot.Creator.createMotor(self.map.motors[name])

        self.tMotors = tMotors

    def set(self, motorNum, pow):
        if motorNum == 0:
            self.tMotors['LLift'].set(ctre.ControlMode.PercentOutput, pow)
        elif motorNum == 1:
            self.tMotors['RLift'].set(ctre.ControlMode.PercentOutput, pow)
        elif motorNum == 2:
            self.tMotors['intake'].set(ctre.ControlMode.PercentOutput, pow)
        elif motorNum == 3:
            self.tMotors['WOF'].set(ctre.ControlMode.PercentOutput, pow)
        elif motorNum == 4:
            self.tMotors['conveyor1'].set(ctre.ControlMode.PercentOutput, pow)
        elif motorNum == 5:
            self.tMotors['conveyor2'].set(ctre.ControlMode.PercentOutput, pow)
        elif motorNum == 6:
            self.tMotors['turret'].set(ctre.ControlMode.PercentOutput, pow)