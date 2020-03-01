import wpilib
from wpilib.command import Subsystem
from wpilib import Encoder
from utilities.PID import PID
from ctre import TalonSRX
import ctre


class Turret(Subsystem):
    def __init__(self, robot):
        Subsystem.__init__(self, 'Turret')

        self.robot = robot
        self.tEncoder = Encoder(1, 3, False, Encoder.EncodingType.k4X)
        motors = {}

        self.map = self.robot.botMap

        for name in self.map.MotorMap.motors:
            motors[name] = robot.Creator.createMotor(self.map.MotorMap.motors[name])

        self.tmotors = motors

        for name in self.tmotors:
            self.tmotors[name].setInverted(self.map.MotorMap.motors[name]['inverted'])
            self.tmotors[name].setNeutralMode(ctre.NeutralMode.Coast)
            if self.map.Motormap.motors[name]['CurLimit'] is True:
                self.tmotors[name].configStatorCurrentLimit(self.robot.Creator.createCurrentConfig(
                    self.robot.botMap.currentConfig['Turret']), 40)

    def set(self, pow):
        self.tmotors['turret'].set(ctre.ControlMode.PercentOutput, pow)


