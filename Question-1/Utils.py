import plotly.graph_objects as go

GRID_SIZE = 100

def plot_paths(agents):
    fig = go.Figure()

    colors = [
        "#FF6347", "#4682B4", "#32CD32", "#FFD700", "#8A2BE2", 
        "#FF4500", "#00FA9A", "#B22222", "#00BFFF", "#8A2BE2"
    ]
    
    for idx, agent in enumerate(agents):
        path = agent.path
        
        x = [p[0] for p in path]
        y = [p[1] for p in path]
        z = [p[2] for p in path]
        
        color = colors[idx % len(colors)] 
        
        fig.add_trace(go.Scatter3d(
            x = x, 
            y = y, 
            z = z,
            mode = 'lines',
            line = dict(color = color, width = 6),
            name = f'Agent {idx + 1}'
        ))

    fig.update_layout(
        scene = dict(
            xaxis = dict(title = 'X', showgrid = True, zeroline = True),
            yaxis = dict(title = 'Y', showgrid = True, zeroline = True),
            zaxis = dict(title = 'Z', showgrid = True, zeroline = True),
        ),
        title = 'Multi-Agent Paths with Conflict Detection',
        showlegend = True,
        margin = dict(l = 0, r = 0, b = 0, t = 0), 
        height = 800,  
        width = 800,  
        scene_camera = dict(
            eye=dict(x = 1.5, y = 1.5, z = 1.5) 
        )
    )
    
    fig.show()

