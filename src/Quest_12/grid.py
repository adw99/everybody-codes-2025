import copy
import pickle

# A grid class where the upper left hand corner of the grid is (0,0)
# x goes up to the right, y goes up as you go down

class Grid:
    def __init__(self,max_x=None,max_y=None,_grid=None):
        if max_x != None and max_y!= None:
            self.grid = [[' ' for _ in range(max_x)] for _ in range(max_y)]
        elif _grid != None:
            self.grid = _grid
        else:
            raise ValueError(f"Inputs missing: {max_x} / {max_y} or {_grid}")

    def __eq__(self,other):
        ym = len(self.grid)
        xm = len(self.grid[0])
        for y in range(ym):
            for x in range(xm):
                if self.grid[y][x] != other.grid[y][x]:
                    return False
        return True

    def __hash__(self):
        immut = tuple( tuple(inner) for inner in self.grid)
        return hash(immut)

    def get(self,x,y):
        return self.grid[y][x]
    
    def set(self,x,y,pt):
        self.grid[y][x] = pt

    def x(self):
        return(len(self.grid[0]))
    
    def y(self):
        return(len(self.grid))

    def copy(self):
        return self.pickle_copy()

    def deep_copy(self):
        _ng = copy.deepcopy(self.grid)
        return Grid(_grid=_ng)
    
    def manual_copy(self):
        _ng = [[' ' for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]
        sample = self.grid[0][0]
        use_copy = type(sample) is dict or type(sample) is list
        for y in range(len(_ng)):
            for x in range(len(_ng[0])):
                if use_copy:
                    _ng[y][x] = self.grid[y][x].copy()
                else:
                    _ng[y][x] = self.grid[y][x]
        return Grid(_grid=_ng)
    
    def pickle_copy(self):
        _ng = pickle.loads(pickle.dumps(self.grid))
        return Grid(_grid=_ng)
