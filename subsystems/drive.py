import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Subsystem
from wpilib import Encoder
from wpilib import ADXRS450_Gyro
from utilities.PID import PID
import wpilib
import ctre


class Drive(Subsystem):
    def __init__(self, robot):
        Subsystem.__init__(self, 'Drive')

        self.robot = robot

        motors = {}
        pistons = {}

        self.map = self.robot.botMap

        for name in self.map.motorMap.motors:
            motors[name] = robot.Creator.createMotor(self.map.motorMap.motors[name])

        for name in self.robot.botMap.PneumaticMap.pistons:
            if name == 'Shifter':
                pistons[name] = self.robot.Creator.createPistons(self.robot.botMap.PneumaticMap.pistons[name])

        self.dMotors = motors
        self.dPistons = pistons

        for name in self.dMotors:
            self.dMotors[name].setInverted(self.robot.botMap.motorMap.motors[name]['inverted'])
            self.dMotors[name].setNeutralMode(ctre.NeutralMode.Coast)
            if self.map.motorMap.motors[name]['CurLimit'] is True:
                self.dMotors[name].configStatorCurrentLimit(self.robot.Creator.createCurrentConfig(
                    self.robot.botMap.currentConfig['Drive']), 40)

    def set(self, lft, rgt):
        self.dMotors['RFDrive'].set(ctre.ControlMode.PercentOutput, rgt)
        self.dMotors['LFDrive'].set(ctre.ControlMode.PercentOutput, lft)




