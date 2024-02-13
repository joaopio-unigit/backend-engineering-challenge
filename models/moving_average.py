class MovingAverage:
    """
    MovingAverage is a class that stores the average of translation events
    for each corresponding timestamp. With this class it becomes easier to
    create relations between a given time and its corresponding average.

    Attributes:
    timestamp (datetime): The atribute that stores the time of the corresponding MovingAverage.
    average (int): The atribute that store the average of the corresponding MovingAverage.
    """

    def __init__(self, timestamp, average):
        """
        Initialize a new instance of MovingAverage.

        Parameters:
        timestamp (datetime): The MovingAverage instance timestamp representing its time.
        average (int): The MovingAverage instance average.
        """
        self._timestamp = timestamp
        self._average = average

    @property
    def timestamp(self):
        """
        The timestamp of the MovingAverage instance.

        Returns:
        timestamp: The MovingAverage instance timestamp.
        """
        return self._timestamp
    
    @property
    def average(self):
        """
        The average of the MovingAverage instance.

        Returns:
        average: The MovingAverage instance average.
        """
        return self._average