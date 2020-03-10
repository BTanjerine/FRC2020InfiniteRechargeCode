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

        for name in self.map.motorMap.motors:
            motors[name] = robot.Creator.createMotor(self.map.motorMap.motors[name])

        for name in self.map.PneumaticMap.pistons:
            pistons[name] = robot.Creator.createPistons(self.map.PneumaticMap.pistons[name])

        self.imotors = motors
        self.ipistons = pistons

        for name in self.imotors:
            self.imotors[name].setInverted(self.map.motorMap.motors[name]['inverted'])
            self.imotors[name].setNeutralMode(ctre.NeutralMode.Coast)

        self.iOut = wpilib.DoubleSolenoid.Value.kForward
        self.iIn = wpilib.DoubleSolenoid.Value.kReverse

    def setIntake(self, pow):
        self.imotors['intake'].set(ctre.ControlMode.PercentOutput, pow)

    def angleIntake(self, Mode):
        self.ipistons['intakeArm'].set(Mode)
