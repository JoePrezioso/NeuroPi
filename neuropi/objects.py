import math

class Item:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.size = (image.get_height()+image.get_width())/2
    def collides(self, other):
        if math.sqrt((self.x-other.x)*(self.x-other.x)+ \
           (self.y-other.y)*(self.y-other.y))<(self.size+other.size)/2:
            return True
        return False
