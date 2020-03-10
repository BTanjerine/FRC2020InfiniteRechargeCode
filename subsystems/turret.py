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

        for name in self.map.motorMap.motors:
            motors[name] = robot.Creator.createMotor(self.map.motorMap.motors[name])

        for name in self.tmotors:
            self.tmotors[name].setInverted(self.map.motorMap.motors[name]['inverted'])
            self.tmotors[name].setNeutralMode(ctre.NeutralMode.Coast)

        self.kP = 0.05
        self.kI = 0.000
        self.kD = 0.002

        self.turretPID = PID(self.kP, self.kI, self.kD)

        self.turretPID.limitVal(0.3)

        self.setPow = 0

    def set(self, pw):
        self.tmotors['turret'].set(ctre.ControlMode.PercentOutput, pw)

    def setPower(self, pow):
        self.setPow = pow

    def getEnc(self):
        return self.tEncoder.get()

    def periodic(self):
        if self.robot.Limelight.isExisting():
            self.set(0) # self.turretPID.outVal(self.robot.Limelight.getX()))
        else:
            self.set(self.setPow)