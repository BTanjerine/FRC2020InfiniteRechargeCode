import wpilib
import ctre
import math
from wpilib.command import Subsystem
from utilities.PID import PID
from networktables import NetworkTables


class Limelight(Subsystem):
    def __init__(self, robot):
        Subsystem.__init__(self, 'Limelight')

        self.limelight = NetworkTables.getTable('limelight')
        self.limelight2 = NetworkTables.getTable('limelight2')

    def getX(self):
        px = self.limelight.getNumber("tx", 0)
        return px

    def getY(self):
        py = self.limelight.getNumber("ty", 0)
        return py

    def getDistance(self):
        h = 50.5
        ang = (20.262*(math.pi/180)) + self.getY() * (math.pi / 180)
        d = h / math.tan(ang)
        return d

