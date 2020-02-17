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

        for name in self.robot.botMap.motorMap.motors:
            motors['name'] = self.robot.Creator.createMotor(self.robot.botMap.motorMap.motors['name'])

        for name in self.robot.botMap.PneumaticMap.pistons:
            if name == 'Shifter':
                pistons['name'] = self.robot.Creator.createPistons(self.robot.botMap.PneumaticMap.pistons['name'])

        self.dMotors = motors
        self.dPistons = pistons

        for name in self.dMotors:
            self.dMotors[name].setInverted(self.robot.botMap.motorMap.motors[name]['inverted'])
            self.dMotors[name].setNeutralMode(ctre.NeutralMode.Coast)
            self.dMotors[name].configStatorCurrentLimit(self.robot.Creator.createCurrentConfig(
                self.robot.botMap.currentConfig['Drive']), 40)




