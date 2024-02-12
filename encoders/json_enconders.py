import json

from models.moving_average import MovingAverage

class MovingAverageEncoder(json.JSONEncoder):
    def default(self, movingaverage):
        if isinstance(movingaverage, MovingAverage):
            return {'timestamp': movingaverage.timestamp.strftime('%Y-%m-%d %H:%M:%S'), 'average': movingaverage.average}
        
        return json.JSONEncoder.default(self, movingaverage)