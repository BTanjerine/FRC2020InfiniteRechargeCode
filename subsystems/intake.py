import wpilib
import ctre
from wpilib.command import Subsystem
from wpilib import Encoder
from wpilib import DoubleSolenoid

class Intake(Subsystem):
    def __init__(self, robot):
        Subsystem.__init__(self, 'Intake')

        self.robot = robot

        motors = {}
        pistons = {}

        self.map = self.robot.botMap

        for name in self.map.MotorMap.motors:
            motors[name] = robot.Creator.createMotor(self.map.MotorMap.motors[name])

        for name in self.map.PneumaticMap.pistons:
            pistons[name] = robot.Creator.createPistons(self.map.PneumaticMap.pistons[name])

        self.imotors = motors
        self.ipistons = pistons

        for name in self.imotors:
            self.imotors[name].setInverted(self.map.motors[name]['inverted'])
            self.imotors[name].setNeutralMode(ctre.NeutralMode.Coast)
            if self.map.MotorMap.motors[name]['CurLimit'] is True:
                self.dMotors[name].configStatorCurrentLimit(self.robot.Creator.createCurrentConfig(
                    self.robot.botMap.currentConfig['Intake']), 40)

    def setIntake(self, pow):
        self.imotor['intake'].set(ctre.ControlMode.PercentOutput, pow)

    def angleIntake(self, Mode):
        self.ipistons['intakeArm'].set(Mode)
