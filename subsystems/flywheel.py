import wpilib
from wpilib.command import Subsystem
from wpilib import Encoder
from utilities.PID import PID
import wpilib
import math
import ctre


class Flywheel(Subsystem):
    def __init__(self, robot):
        Subsystem.__init__(self, 'Flywheel')

        self.CurPos = 0
        self.PasPos = 0

        self.robot = robot
        self.Fenc = Encoder(6, 7, False, Encoder.EncodingType.k4X)
        self.map = self.robot.botMap
        motor = {}
        piston = {}

        for name in self.robot.botMap.motorMap.motors:
            motor[name] = self.robot.Creator.createMotor(self.robot.botMap.motorMap.motors[name])

        for name in self.robot.botMap.PneumaticMap.pistons:
            piston[name] = self.robot.Creator.createPistons(self.robot.botMap.PneumaticMap.pistons[name])

        self.fmotor = motor
        self.fpiston = piston

        for name in self.fmotor:
            self.fmotor[name].setInverted(self.robot.botMap.motorMap.motors[name]['inverted'])
            self.fmotor[name].setNeutralMode(ctre.NeutralMode.Coast)
            if self.map.motorMap.motors[name]['CurLimit'] is True:
                self.fmotor[name].configStatorCurrentLimit(self.robot.Creator.createCurrentConfig(
                    self.robot.botMap.currentConfig['Fly']), 40)

        self.kP = 0.008
        self.kI = 0.00002
        self.kD = 0.00018
        self.kF = 0.0   # tune me when testing

        self.flywheelPID = PID(self.kP, self.kI, self.kD, self.kF)

        self.flywheelPID.MaxIn(680)
        self.flywheelPID.MaxOut(1)
        self.flywheelPID.limitVal(0.95)  # Limit PID output power to 50%

        self.feetToRPS = 51.111

    def log(self):
        wpilib.SmartDashboard.putNumber('Flywheel Enc', self.Fenc.get())
        wpilib.SmartDashboard.putNumber('Flywheel Vel', self.getVelocity(self.Fenc.get()))

    def init(self):
        self.Fenc.reset()

    def set(self, pow):
        self.fmotor['RFly'].set(ctre.ControlMode.PercentOutput, pow)
        self.fmotor['LFly'].set(ctre.ControlMode.PercentOutput, pow)

    def setVelocityPID(self, rps):
        self.flywheelPID.setPoint(rps)
        if rps == 0:
            pow = 0
        else:
            pow = self.flywheelPID.outVel(self.getVelocity(self.get()))
        return pow

    def get(self):
        return self.Fenc.get()

    def getVelocity(self, input):
        self.CurPos = -(input / 1025) * (2 * math.pi)
        vel = (self.CurPos - self.PasPos) / 0.02
        self.PasPos = self.CurPos
        return vel








