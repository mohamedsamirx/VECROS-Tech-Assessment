## Problem 1: Multi-Agent Pathfinding in 3D Grid

### Problem Overview and Description

This problem is a common challenge in fields such as robotics, logistics, and game development. It involves finding the shortest paths for multiple agents (represented by the user-input sets of `{start, end}` points) in a 3D grid environment. 

#### Key Challenges:

1. **Multiple Agents**: The problem involves two or more sets of `{start, end}` points, making it a multi-agent pathfinding problem.
2. **Conflict Avoidance**: Paths must be conflict-free, meaning no two agents can occupy the same grid point at the same time.
3. **Obstacles**: Randomly assigned higher weights on certain grid points act as obstacles. The goal is to find the shortest path (i.e., with the smallest cumulative weight) while avoiding these obstacles.
4. **Time and Velocity**: All agents share the same velocity, simplifying the problem. The focus is on ensuring no conflicts at any time step.

---

### Key Considerations

- **Conflict-Free Paths**: Ensuring computed paths for all agents do not intersect at any time step.
- **Shortest Path**: Paths must minimize the cumulative weight (cost).
- **Visualization**: The output includes a 3D plot of computed paths with unique colors.

---


### Final Output

1. **Conflict-Free Paths**: Compute shortest, conflict-free paths for all agents.
2. **Visualization**: 3D plot of computed paths with unique colors.

---

## Algorithm Overview

The solution employs the **Enhanced Conflict-Based Search (ECBS)** algorithm, extending the A* algorithm for multi-agent pathfinding.

1. **Grid Initialization**: Random weights simulate obstacles.
2. **Pathfinding**: A* for individual agents; ECBS resolves conflicts iteratively.
3. **Visualization**: Intuitive 3D path representation using Plotly.

---

## File Descriptions

### `Agent.py`

**Purpose**: Represents an agent with start and end positions.

**Attributes**:

- `start`: Starting position in the 3D grid.
- `end`: Goal position in the 3D grid.
- `path`: Computed path.
- `constraints`: Prevents conflicts by avoiding specific positions at specific times.

---

### `Grid.py`

**Purpose**: Represents a 3D grid environment with random weights.

**Attributes**:

- **`size`**: Grid size (e.g., 100 for 100x100x100 grid).
- **`grid`**: 3D NumPy array storing weights.

**Methods**:

- `__init__`: Initializes grid with random weights.
- `get_weight`: Returns the weight of a grid point.

---

### `Utils.py`

**Purpose**: Visualizes multi-agent paths in a 3D plot using Plotly.

**Features**:

- **Color-Coded Paths**: Unique color for each agent.
- **Interactive 3D Visualization**: Zoom, rotate, and pan capabilities.

---

### `PathFinder.py`

#### 1. A* Algorithm

**Purpose**: Finds shortest paths for single agents.

**Steps**:

1. **Initialization**: Sets up open set, path tracking, and costs.
2. **Exploration**: Expands nodes, avoiding constraints.
3. **Heuristic**: Uses Manhattan distance.
4. **Output**: Returns shortest path or `None` if no path exists.

---

#### 2. Enhanced Conflict-Based Search (ECBS)

**Purpose**: Resolves conflicts iteratively for multi-agent pathfinding.

**Steps**:

1. **Initial Planning**: Computes paths using A*.
2. **Conflict Detection**: Identifies conflicts between agents.
3. **Resolution**: Adds constraints and re-plans paths iteratively.

---

#### 3. Conflict Detection

**Purpose**: Detects conflicts between agent paths.

**Steps**:

1. **Comparison**: Checks agents' positions at each time step.
2. **Output**: Returns list of conflicts.

---

### `Multiple-Agent-path.py`

**Purpose**: Entry point of the program.

- **Initializes**: Grid, agents, and pathfinder.
- **Computes**: Conflict-free paths using ECBS.
- **Visualizes**: Results in a 3D plot.

## How to Run the Program

To run the program, first clone the repository using `git clone <repository-link>`, then navigate to the cloned directory using `cd <repository-name>`. Finally, execute the program by running the command `python3 Question-1/Multiple-Agent-path.py`. Replace `<repository-link>` with the repository URL and `<repository-name>` with the name of the cloned repository.

## Output

The program generates the following outputs:

1. **Grid Information**: Displays the size of the grid, the total number of grid points, and the number of high-weight points acting as obstacles.
2. **Agent Paths**: Prints each agent's path as a sequence of grid points from the start to the end position.
3. **Visualization**: Creates an interactive 3D plot showing the conflict-free paths for all agents.


![Alt text](/Question-1/Images/image1.png)
![Alt text](/Question-1/Images/image2.png)
![Alt text](/Question-1/Images/image3.png)
![Alt text](/Question-1/Images/image4.png)
![Alt text](/Question-1/Images/image5.png)
![Alt text](/Question-1/Images/image6.png)
