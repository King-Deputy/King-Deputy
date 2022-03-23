class too:
    def __init__(self, measurement, uses):
        self.measurement = measurement
        self.uses = uses
Chisquare = too("counting data", "test association")
ttest = too("continuous data", "test difference")
correlation = too("continuous data", "test linear relationship")

