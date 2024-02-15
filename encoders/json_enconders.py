import json

from models.moving_average import MovingAverage

class MovingAverageEncoder(json.JSONEncoder):
    """
    This class is a JSON Encoder for MovingAverage instances.

    The encoder provides a serialization method for MovingAverage instances
    that can be used to convert these into the JSON format.

    Methods:
    default(self, movingaverage): Serializes a MovingAverage object into the JSON format.
    """

    def default(self, movingaverage):
        """
        Serializes a MovingAverage instance into the JSON format.

        Parameters:
        movingaverage (MovingAverage): The MovingAverage instance to be serialized.

        Returns:
        dict: A JSON representation of the MovingAverage instance.
        """
        
        if isinstance(movingaverage, MovingAverage):
            return {'date': movingaverage.timestamp.strftime('%Y-%m-%d %H:%M:%S'), 'average_delivery_time': movingaverage.average}
        
        return json.JSONEncoder.default(self, movingaverage)