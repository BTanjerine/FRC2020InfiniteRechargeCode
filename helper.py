from ctre import TalonSRX
from ctre import VictorSPX
from ctre import TalonFX
from ctre import StatorCurrentLimitConfiguration
from rev import SparkMax
from wpilib import VictorSP
from wpilib import Joystick
from wpilib import XboxController
from wpilib import DoubleSolenoid
from wpilib import Solenoid
import ctre


class Creator:
    def createMotor(self, MotorSpec):
        motr = None
        if MotorSpec['ContType'] == 'CAN':
            if MotorSpec['Type'] == 'TalonSRX':
                if MotorSpec['jobType'] == 'master':
                    motr = TalonSRX(MotorSpec['port'])
                elif MotorSpec['jobType'] == 'slave':
                    motr = TalonSRX(MotorSpec['port'])
                    motr.setInverted(MotorSpec['inverted'])
                    motr.set(ctre.ControlMode.Follower, MotorSpec['masterPort'])
            if MotorSpec['Type'] == 'TalonFX':
                if MotorSpec['jobType'] == 'master':
                    motr = TalonFX(MotorSpec['port'])
                elif MotorSpec['jobType'] == 'slave':
                    motr = TalonFX(MotorSpec['port'])
                    motr.setInverted(MotorSpec['inverted'])
                    motr.set(ctre.ControlMode.Follower, MotorSpec['masterPort'])
            if MotorSpec['Type'] == 'VictorSPX':
                if MotorSpec['jobType'] == 'master':
                    motr = VictorSPX(MotorSpec['port'])
                elif MotorSpec['jobType'] == 'slave':
                    motr = VictorSPX(MotorSpec['port'])
                    motr.setInverted(MotorSpec['inverted'])
                    motr.set(ctre.ControlMode.Follower, MotorSpec['masterPort'])
            if MotorSpec['Type'] == 'SparkMax':
                motr = SparkMax(MotorSpec['port'])
        else:
            print("IDK your motor")

        return motr

    def createPWMMotor(self, MotorSpec):
        if MotorSpec['Type'] == 'VictorSP':
            motr = VictorSP(MotorSpec['port'])
            motr.setInverted(MotorSpec['inverted'])
            return motr
        else:
            print("IDK your motor")

    def createCurrentConfig(self, configSpec):
        config = StatorCurrentLimitConfiguration(configSpec['state'], configSpec['currentLimit'],
                                                 configSpec['triggerThresh'], configSpec['time'])
        return config

    def createPistons(self, pistonSpec):
        piston = None
        if pistonSpec['Type'] == 'Double':
            piston = DoubleSolenoid(pistonSpec['portA'], pistonSpec['portB'])
        elif pistonSpec['Type'] == 'single':
            piston = Solenoid(pistonSpec['portA'])
        else:
            print("IDK your pistons")
        return piston

    def createControllers(self, ConSpec):
        con = None
        if ConSpec['jobType'] == 'main':
            if ConSpec['Type'] == 'xbox':
                con = XboxController(ConSpec['Id'])
            elif ConSpec['Type'] == 'xtreme':
                con = Joystick(ConSpec['Id'])
            elif ConSpec['Type'] == 'gameCube':
                con = Joystick(ConSpec['Id'])
            else:
                print("IDK your Controller")

        elif ConSpec['jobType'] == 'side':
            if ConSpec['Type'] == 'xbox':
                con = XboxController(ConSpec['Id'])
            elif ConSpec['Type'] == 'xtreme':
                con = Joystick(ConSpec['Id'])
            elif ConSpec['Type'] == 'custom':
                con = Joystick(ConSpec['Id'])
            else:
                print("IDK your Controller")

        else:
            print("IDK your Controller")

        return con
