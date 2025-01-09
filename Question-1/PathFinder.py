import heapq
from Utils import GRID_SIZE

# ECBS PathFinder
class PathFinder:
    def __init__(self, grid):
        self.grid = grid

    # A* algorithm for single agent
    def a_star(self, start, end, constraints):
        open_set = []
        heapq.heappush(open_set, (0, 0, start, []))
        came_from = {}
        g_score = {start: 0}
        constraints_set = set(constraints)

        while open_set:
            f, g, current, path = heapq.heappop(open_set)
            if current == end:
                return path + [current]
            
            if current in came_from:
                continue
            
            came_from[current] = path
            x, y, z = current
            neighbors = [
                (x + 1, y, z),
                (x - 1, y, z),
                (x, y + 1, z),
                (x, y - 1, z),
                (x, y, z + 1),
                (x, y, z - 1)
            ]
            
            for neighbor in neighbors:
                if 0 <= neighbor[0] <= GRID_SIZE and 0 <= neighbor[1] <= GRID_SIZE and 0 <= neighbor[2] <= GRID_SIZE:
                    if (neighbor, g + 1) in constraints_set:
                        continue
                    
                    weight = self.grid.get_weight(neighbor)
                    cost = weight
                    tentative_g = g + cost
                    
                    if neighbor not in g_score or tentative_g < g_score[neighbor]:
                        g_score[neighbor] = tentative_g
                        h = abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1]) + abs(neighbor[2] - end[2])
                        f_score = tentative_g + h
                        
                        heapq.heappush(open_set, (f_score, tentative_g, neighbor, path + [current]))
       
        return None

    # ECBS algorithm
    def ecbs(self, agents):
        for agent in agents:
            path = self.a_star(agent.start, agent.end, [])
            if path:
                agent.path = path
                
            else:
                print("No path found for an agent.")
                return None

        while True:
            conflicts = self.detect_conflicts(agents)
            if not conflicts:
                break
            
            for conflict in conflicts:
                agent_idx, other_agent_idx, conflict_pos, conflict_step = conflict
                agents[agent_idx].constraints.append((conflict_pos, conflict_step))
                new_path = self.a_star(agents[agent_idx].start, agents[agent_idx].end, agents[agent_idx].constraints)
                if new_path:
                    agents[agent_idx].path = new_path
                    
                else:
                    print("Cannot resolve conflict for agent", agent_idx)
                    return None
                
        return agents

    # Conflict detection
    def detect_conflicts(self, agents):
        conflicts = []
        
        for i in range(len(agents)):
            for j in range(i + 1, len(agents)):
                path_i = agents[i].path
                path_j = agents[j].path
                max_step = max(len(path_i), len(path_j))
                
                for step in range(max_step):
                    pos_i = path_i[step] if step < len(path_i) else path_i[-1]
                    pos_j = path_j[step] if step < len(path_j) else path_j[-1]

                    if pos_i == pos_j:
                        conflicts.append((i, j, pos_i, step))

        return conflicts
