class HBCemployee:
    raise_amount = .25

    def __init__(self, fName, lName, Pay):
        self.fName = fName
        self.lName = lName
        self.Pay = Pay

    @property
    def empEmail(self):
        return '{}.{}@email.com'.format(self.fName, self.lName)

    @property
    def empfullName(self):
        return '{} {}'.format(self.fName, self.lName)

    def raisePay(self):
        self.monthlyPay = int(self.Pay + (self.Pay * self.raise_amount))
        return self.monthlyPay
