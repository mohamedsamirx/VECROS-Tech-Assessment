from Grid import Grid
from Agent import Agent
from PathFinder import PathFinder
from Utils import GRID_SIZE, plot_paths

# Main function
def main():
    grid = Grid(GRID_SIZE)
    path_finder = PathFinder(grid)
    agents = [
        Agent(start = (0, 0, 0), end = (50, 51, 52)),        
        Agent(start = (50, 50, 50), end = (100, 100, 100)),  
        Agent(start = (0, 50, 53), end = (52, 100, 50)),     
        Agent(start = (56, 3, 50), end = (3, 53, 50)),       
        Agent(start = (25, 25, 25), end = (75, 75, 75)),     
        Agent(start = (24, 24, 24), end = (76, 76, 76)),  
        Agent(start = (1, 1, 1), end = (1, 3, 0)),           
        Agent(start = (1, 70, 10), end = (10, 20, 30)),      
        Agent(start = (42, 62, 82), end = (45, 46, 47)),     
        Agent(start = (60, 44, 20), end = (90, 63, 84))      
    ]

    agents = path_finder.ecbs(agents)
    
    if agents:
        for idx, agent in enumerate(agents):
            print(f"Agent {idx+1} path: {agent.path}")
            
        print()
        plot_paths(agents)

   

if __name__ == "__main__":
    main()
