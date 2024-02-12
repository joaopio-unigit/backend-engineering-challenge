class MovingAverage:

    def __init__(self, timestamp, average):
        self._timestamp = timestamp
        self._average = average

    @property
    def timestamp(self):
        return self._timestamp
    
    @property
    def average(self):
        return self._average