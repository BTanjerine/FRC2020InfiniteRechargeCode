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
        self.tEncoder = Encoder(4, 5, False, Encoder.EncodingType.k4X)
        motors = {}

        self.map = self.robot.botMap
        self.tmotors = motors

        for name in self.map.MotorMap.motors:
            motors[name] = robot.Creator.createMotor(self.map.MotorMap.motors[name])

        for name in self.tmotors:
            self.tmotors[name].setInverted(self.map.MotorMap.motors[name]['inverted'])
            self.tmotors[name].setNeutralMode(ctre.NeutralMode.Coast)
            if self.map.Motormap.motors[name]['CurLimit'] is True:
                self.tmotors[name].configStatorCurrentLimit(self.robot.Creator.createCurrentConfig(
                    self.robot.botMap.currentConfig['Turret']), 40)

        self.kP = 0.0
        self.kI = 0.0
        self.kD = 0.0

        self.turretPID = PID(self.kP, self.kI, self.kD)

    def set(self, pw):
        self.tmotors['turret'].set(ctre.ControlMode.PercentOutput, pw)

    def getEnc(self):
        return self.tEncoder.get()

