import wpilib


class RobotMap:
    def __init__(self, robot):
        self.robot = robot
        self.motorMap = MotorMap()
        self.PneumaticMap = PneumaticMap()
        self.ControlMap = ControlMap()

        self.currentConfig = {
            'Fly': {
                'state': True,
                'currentLimit': 25,
                'triggerThresh': 35,
                'time': 0.5
            },
            'Drive': {
                'state': True,
                'currentLimit': 35,
                'triggerThresh': 40,
                'time': 0.5
            }}


class MotorMap:
    def __init__(self):
        self.motors = {}
        self.PWMmotor = {}

        """
        Drive Motors
        """
        self.motors['RFDrive'] = {
            'port': 1,
            'inverted': True,
            'jobType': 'master',
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}

        self.motors['RMDrive'] = {
            'port': 4,
            'inverted': True,
            'jobType': 'slave',
            'masterPort': 1,
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}
        self.motors['RBDrive'] = {
            'port': 7,
            'inverted': True,
            'jobType': 'slave',
            'masterPort': 1,
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}

        self.motors['LFDrive'] = {
            'port': 9,
            'inverted': False,
            'jobType': 'master',
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}
        self.motors['LMDrive'] = {
            'port': 0,
            'inverted': False,
            'jobType': 'slave',
            'masterPort': 9,
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}
        self.motors['LBDrive'] = {
            'port': 2,
            'inverted': False,
            'jobType': 'slave',
            'masterPort': 9,
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}

        """
        Arm Motors
        
        self.motors['RLift'] = {
            'port': 3,
            'inverted': False,
            'jobType': 'master',
            'ContType': 'CAN',
            'Type': 'TalonSRX',
            'CurLimit': False}
        self.motors['LLift'] = {
            'port': 6,
            'inverted': True,
            'jobType': 'master',
            'ContType': 'CAN',
            'Type': 'TalonSRX',
            'CurLimit': False}"""

        """
        Shooter Motors
        
        self.motors['RFly'] = {
            'port': 10,
            'inverted': True,
            'jobType': 'master',
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}
        self.motors['LFly'] = {
            'port': 11,
            'inverted': False,
            'jobType': 'slave',
            'masterPort': 10,
            'ContType': 'CAN',
            'Type': 'TalonFX',
            'CurLimit': True}"""

        """
        Intake motors
        
        self.motors['intake'] = {'port': 12, 'inverted': False, 'jobType': 'master',
                                 'ContType': 'CAN', 'Type': 'TalonSRX', 'CurLimit': False}
        self.motors['transition'] = {'port': 13, 'inverted': False, 'jobType': 'master',
                                     'ContType': 'CAN', 'Type': 'TalonSRX', 'CurLimit': False}
        self.motors['conveyor'] = {'port': 14, 'inverted': False, 'jobType': 'master',
                                   'ContType': 'CAN', 'Type': 'TalonSRX', 'CurLimit': False}"""


class PneumaticMap:
    def __init__(self):
        self.pistons = {}

        self.OUT = wpilib.DoubleSolenoid.Value.kForward
        self.IN = wpilib.DoubleSolenoid.Value.kReverse
        self.CLOSE = wpilib.DoubleSolenoid.Value.kOff

        """
        Drive Pistons
        
        self.pistons['Shifter'] = {'portA': 0, 'portB': 1, 'Type': 'Double', 'masterPort': 0}
        self.pistons['flyShifter'] = {'portA': 2, 'Type': 'Single', 'masterPort': 0}"""

        """
        Intake Pistons
        
        self.pistons['intakeArm'] = {'portA': 3, 'portB': 4, 'Type': 'Double', 'masterPort': 0}
        self.pistons['ballStopper'] = {'portA': 5, 'portB': 6, 'Type': 'Double', 'masterPort': 0}
        self.pistons['liftRelease'] = {'portA': 0, 'portB': 1, 'Type': 'Double', 'masterPort': 1}"""


class ControlMap:
    def __init__(self):
        self.Controller = {}

        """
        drive controller
        """
        self.Controller['xbox'] = {'Id': 0, 'Type': 'xbox', 'jobType': 'main'}

        """
        Extra controller for controlling arm 
        """
        self.Controller['board'] = {'Id': 1, 'Type': 'custom', 'jobType': 'side'}
