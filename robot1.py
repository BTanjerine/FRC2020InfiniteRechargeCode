import ctre
from ctre import WPI_TalonFX
from ctre import StatorCurrentLimitConfiguration
from ctre import SupplyCurrentLimitConfiguration
from wpilib import Joystick
import wpilib
from wpilib import SmartDashboard
import math
from PID import PID


class KodyBot(wpilib.TimedRobot):

    def robotInit(self):
        self.kP = 0.003
        self.kI = 0.00001
        self.kD = 0.4
        self.kF = 16

        self.lft = WPI_TalonFX(1)          # Motor and Controller see
        self.rgt = WPI_TalonFX(0)

        self.joy = wpilib.XboxController(0)
        self.Pan = Joystick(1)

        self.FlywheelPID = PID(self.kP, self.kI, self.kD, self.kF)   # Create Flywheel PID using PID template
        self.tickperRevMotor = 2048           # 3000 ticks equals one rotation for motor
        self.tickperRevShaft = (self.tickperRevMotor * 1.5) / 2
        self.PidVel = 0

        self.rgt.setInverted(False)     # Reversing motors
        self.lft.setInverted(True)

        self.rgt.setNeutralMode(ctre.NeutralMode.Coast)     # setting motors to coast
        self.lft.setNeutralMode(ctre.NeutralMode.Coast)

        self.rgt.configStatorCurrentLimit(StatorCurrentLimitConfiguration(True, 25, 35, 1.0), 40)    # limit motor current to 35 amps
        self.lft.configStatorCurrentLimit(StatorCurrentLimitConfiguration(True, 25, 35, 1.0), 40)

    def RPMVel(self, vel1, vel2):
        AvgVel = (vel2 + vel1) / 2    # Taking avg sensor inputs and accounting for gear ratio
        AvgRPM = AvgVel*600 / 2050  # Mult AvgVel by 600 then dividing by ticks per revolution get RPM
        return AvgRPM       # Return RPM Calculated

    def RPMConv(self, AvgRPM):
        AvgRPS = AvgRPM / 60            # Covert RPM into sec
        AvgFPS = AvgRPS * 0.5 * math.pi     # use RPS to get distance traveled in feet per sec
        return AvgFPS


    def getkP(self):
        self.kP = wpilib.SmartDashboard.getNumber("kP", 0.03)    # Use SD input to tune P constant

    def getkI(self):
        self.kI = wpilib.SmartDashboard.getNumber("kI", 0.00001)    # Use SD input to tune I constant

    def getkD(self):
        self.kD = wpilib.SmartDashboard.getNumber("kD", 10)    # use SD input to tune D constant

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        self.rgt.setSelectedSensorPosition(0)       # Reset encoders in flywheel
        self.lft.setSelectedSensorPosition(0)
        self.FlywheelPID.MaxIn(6400)
        self.FlywheelPID.MaxOut(1)
        self.FlywheelPID.limitVal(0.5)              # Limit PID output power to 50%
        self.FlywheelPID.setPoint(2000)              # Flywheel setpoint

    def teleopPeriodic(self):
        self.rgtV = self.rgt.getSelectedSensorVelocity() * 1.5
        self.lftV = self.lft.getSelectedSensorVelocity()
        self.rgtPos = self.rgt.getSelectedSensorPosition() * 1.5
        self.lftPos = self.lft.getSelectedSensorPosition()  # get sensor values from flywheel encoders

        self.getkP()           # Get tuning values from smart Dashboard
        self.getkI()
        self.getkD()

        joyS = self.joy.getTriggerAxis(self.joy.Hand.kRightHand)        # Joystick input values
        joyA = self.joy.getAButton()
        self.PidVel = self.FlywheelPID.outVel(self.RPMVel(self.rgtV, self.rgtV))

        if self.PidVel < 0:
            self.PidVel = 0

        if joyA == 1:
            if self.Pan.getRawButton(9) == 1:
                self.rgt.set(ctre.ControlMode.PercentOutput, 0.6)      # 60% power
                self.lft.set(ctre.ControlMode.PercentOutput, 0.6)

            elif self.Pan.getRawButton(8) == 1:
                self.rgt.set(ctre.ControlMode.PercentOutput, 0.65)     # 65% power
                self.lft.set(ctre.ControlMode.PercentOutput, 0.65)

            elif self.Pan.getRawButton(7) == 1:
                self.rgt.set(ctre.ControlMode.PercentOutput, 0.7)      # 70% power
                self.lft.set(ctre.ControlMode.PercentOutput, 0.7)

            elif self.Pan.getRawButton(6) == 1:
                self.rgt.set(ctre.ControlMode.PercentOutput, 0.75)     # 75% power
                self.lft.set(ctre.ControlMode.PercentOutput, 0.75)

            elif self.Pan.getRawButton(5) == 1:
                self.rgt.set(ctre.ControlMode.PercentOutput, 0.8)      # 80% power
                self.lft.set(ctre.ControlMode.PercentOutput, 0.8)

            elif self.Pan.getRawButton(4) == 1:

                self.rgt.set(ctre.ControlMode.PercentOutput, 1.0)         # 100% power
                self.lft.set(ctre.ControlMode.PercentOutput, 1.0)

            elif self.Pan.getRawButton(3) == 1:
                self.rgt.set(ctre.ControlMode.PercentOutput, self.PidVel)
                self.lft.set(ctre.ControlMode.PercentOutput, self.PidVel)

            else:
                self.rgt.set(ctre.ControlMode.PercentOutput, 0)         # stop
                self.lft.set(ctre.ControlMode.PercentOutput, 0)
        else:
            self.rgt.set(ctre.ControlMode.PercentOutput, 0)     # Stop motors
            self.lft.set(ctre.ControlMode.PercentOutput, 0)

        wpilib.SmartDashboard.putNumber("PID Err", self.FlywheelPID.getError(self.RPMVel(self.rgtV, self.rgtV)))  # Print error on Smart Dash
        wpilib.SmartDashboard.putNumber("PID OutP", self.PidVel)   # Print Output vals on SD
        wpilib.SmartDashboard.putNumber("Fly Val", self.rgtPos/2050)
        wpilib.SmartDashboard.putNumber("Fly RPM", self.RPMVel(self.rgtV, self.rgtV))
        wpilib.SmartDashboard.putNumber("Fly Vel", self.rgtV)

        wpilib.SmartDashboard.putNumber("kP", self.kP)
        wpilib.SmartDashboard.putNumber("kI", self.kI)
        wpilib.SmartDashboard.putNumber("kD", self.kD)
        wpilib.SmartDashboard.putNumber("Flywheel P", self.FlywheelPID.getp(self.RPMVel(self.rgtV, self.rgtV)))
        wpilib.SmartDashboard.putNumber("flywheel I", self.FlywheelPID.getI(self.RPMVel(self.rgtV, self.rgtV)))
        wpilib.SmartDashboard.putNumber("flywheel D", self.FlywheelPID.getd(self.RPMVel(self.rgtV, self.rgtV)))
        wpilib.SmartDashboard.putNumber("Rgt %", self.rgt.getMotorOutputPercent())
        wpilib.SmartDashboard.putNumber("Lft %", self.lft.getMotorOutputPercent())
        wpilib.SmartDashboard.putNumber("Flywheel Volts", self.rgt.getStatorCurrent())

        self.FlywheelPID.UpCon(self.kP, self.kI, self.kD)
        print(self.kD)

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def testPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(KodyBot)

