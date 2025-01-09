import numpy as np

# Grid class
class Grid:
    def __init__(self, 
                 size,
                 weight_prob = 0.1,
                 Min_high_weight = 1,
                 Max_high_weight = 10):
        self.size = size
        self.grid = np.zeros((size + 1, size + 1, size + 1), dtype = int)
        print(f"Grid size: {self.grid.shape}")

        total_points = (size + 1) ** 3
        print(f"Total grid points: {total_points}")

        num_high_weight = int((size + 1) ** 3 * weight_prob)
        print(f"Number of high-weight points: {num_high_weight}")
        
        coords = np.array(np.unravel_index(np.random.choice((size + 1) ** 3, num_high_weight, replace = False),
                                           (size + 1, size + 1, size + 1))).T
        for x, y, z in coords:
                self.grid[x, y, z] = np.random.randint(Min_high_weight, Max_high_weight + 1)

    def get_weight(self, pos):
        x, y, z = pos
        return self.grid[x, y, z]