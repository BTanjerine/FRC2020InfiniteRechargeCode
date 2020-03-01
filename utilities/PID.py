from time import sleep


class PID(object):
    def __init__(self, kp, ki, kd, kf=0):
        super().__init__()

        self.kp = kp
        self.ki = ki        # PID tuning variables
        self.kd = kd
        self.kf = kf

        self.pastError = 0  # Reset Past error

        self.p = 0
        self.i = 0
        self.d = 0

        self.output = 0     # output value is 0
        self.outputVel = 0
        self.Dest = 0
        self.Error = 0
        self.aError = 0
        self.limit = 0
        self.MaxInput = 0
        self.MaxOutput = 0

    def setPoint(self, setpoint):
        """
        :param setpoint: destination
        :return: setpoint or destination
        """
        self.Dest = setpoint
        return self.Dest

    def MaxIn(self, MaxInput):
        self.MaxInput = MaxInput

    def MaxOut(self, MaxOutput):
        self.MaxOutput = MaxOutput

    def getError(self, inval):
        """

        :param inval: sensor input
        :return: Error, or current position of robot
        Error is where you want to be minus where you are
        """
        self.Error = self.Dest - inval    # destination minus current pos
        return self.Error

    def getp(self, inval):
        """
        :param inval: sensor input
        :return get proportional, which is
        error multiplied by tuning variable kP
        """
        self.p = self.getError(inval) * self.kp
        return self.p

    def getI(self, inval):
        """
        :param inval: sensor input
        :return get integral, which is
        accumulated error * kI
        accumulated error is total error
        """
        if self.Error == 0:
            self.i = 0
        else:
            self.i = ((self.Error)+self.i) * self.ki

        return self.i

    def getd(self, inval):
        """

        :param inval: sensor input
        :return: derivative, deltaError * kD,
        derivative is rate of change
        deltaError is your error - past error

        """
        self.d = (self.getError(inval) - self.pastError) * self.kd
        return self.d

    def EstF(self):
        """
        :return: Feed forward value using ratio maximum output over maximum input
        multiplied by the set point, will change motor power based on the ratio
        """
        self.F = ((self.MaxOutput / self.MaxInput) * self.Dest) * self.kf
        return self.F

    def limitVal(self, limitval):
        """
        :param limitval: set limit for the pid
        :return: limitval
        limitvalue limits output value for the pid
        either 1 or -1
        """
        self.limit = limitval
        return self.limit

    def outVel(self, inval):
        """

        :param inval: sensor input
        :return: output value for the motor,
        outVel is the sum of p i d plus the feed forward
        """
        self.outputVel = self.getp(inval) + self.getI(inval) + self.getd(inval)
        if self.outputVel > self.limit:
            self.outputVel = self.limit

        elif self.outputVel < 0:
            self.outputVel = 0

        self.pastError = self.getError(inval)

        return self.EstF() + self.outputVel

    def outVal(self, inval):
        """
        :param inval: sensor input
        :return: output value for the motor,
        outVal is the sum of the p i and d
        """
        self.output = self.getp(inval) + self.getI(inval) + self.getd(inval)

        if self.output > self.limit:
            self.output = self.limit
        elif self.output < -self.limit:
            self.output = -self.limit
        return self.output

    def UpCon(self, kP, kI , kD):
        """

        :param kP: Tuning constant for P from smart Dashboard
        :param kI: Tuning constant for I from Smart Dashboard
        :param kD: Tuning constant for D from Smart Dashboard
        :return: Updated values for pid
        """
        self.kp = kP
        self.kI = kI
        self.kD = kD

        return self.kp, self.kI, self.kD
