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
        self.FVelocity = 0

        self.robot = robot
        self.Fenc = Encoder(0, 1, False, Encoder.EncodingType.k4X)

        motor = {}
        piston = {}

        for name in self.robot.botMap.motorMap.motors:
            motor[name] = self.robot.Creator.createMotor(self.robot.botMap.motorMap.motors[name])

        for name in self.robot.botMap.PneumaticMap.pistons:
            piston[name] = self.robot.Creator.createPistons(self.robot.botMap.PneumaticMap.pistons[name])

        self.fmotor = motor
        self.fpiston = piston

        for name in self.fmotor:
            self.fMotors[name].setInverted(self.robot.botMap.motorMap.motors[name]['inverted'])
            self.fMotors[name].setNeutralMode(ctre.NeutralMode.Coast)
            self.fMotors[name].configStatorCurrentLimit(self.robot.Creator.createCurrentConfig(
                self.robot.botMap.currentConfig['Flywheel']), 40)

    def periodic(self):
        pass

    def set(self, pow):
        self.fmotor['RFLy'].set(ctre.ControlMode.PercentOutput, pow)
        self.fmotor['LFLy'].set(ctre.ControlMode.PercentOutput, pow)

    def get(self):
        return self.Fenc.get()

    def getVelocity(self):
        self.FVelocity = (self.CurPos - self.PasPos) / 0.02
        self.CurPos = -(self.fly.get() / 1025) * (2 * math.pi)
        self.PasPos = self.CurPos
        return self.FVelocity







