class Point:
    ''' Represents a point in two-dimensional geometric coordinates '''
    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point.
        The x and y coordinates can be specified.
        If they are not, the point defaults to the origin.'''
        self.x = x
        self.y = y
