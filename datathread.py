import threading
from python_mindwave_mobile.MindwaveDataPointReader import MindwaveDataPointReader
from python_mindwave_mobile.MindwaveDataPoints import *

class GetData( threading.Thread ):

    def __init__(self, mdpr):
        super(GetData, self).__init__()
        self.mindwaveDataPointReader = mdpr
        
    def run ( self ):
        self.meditation = 50
        self.attention = 50
        self.poor_signal = 50
        self.running = True

        while self.running:
            dataPoint = self.mindwaveDataPointReader.readNextDataPoint()
            if (not dataPoint.__class__ is RawDataPoint):
                if dataPoint.__class__ is AttentionDataPoint:
                    self.attention = dataPoint.attentionValue
                if dataPoint.__class__ is MeditationDataPoint:
                    self.meditation = dataPoint.meditationValue
                if dataPoint.__class__ is PoorSignalLevelDataPoint:
                    self.poor_signal = dataPoint.amountOfNoise
                else:
                    pass
                    #print dataPoint
"""
#start the reader
if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start('74:E5:43:89:54:2E')


#start the data thread
data = GetData()
data.start()

#end the data thread
data.running = False
data.join()

"""
