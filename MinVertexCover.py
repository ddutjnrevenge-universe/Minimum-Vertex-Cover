import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, colorchooser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def isCover(V, k, E):
    global gr
    Set = (1 << k) - 1
    limit = (1 << V)
    vis = [[0] * maxn for i in range(maxn)]
    cover_vertices = []
    
    while (Set < limit):
        vis = [[0] * maxn for i in range(maxn)]
        cnt = 0
        j = 1
        v = 1
        
        while(j < limit):
            if (Set & j):
                cover_vertices.append(v)
                for k in range(1, V + 1):
                    if (gr[v][k] and not vis[v][k]):
                        vis[v][k] = 1
                        vis[k][v] = 1
                        cnt += 1
            j = j << 1
            v += 1
        
        if (cnt == E): 
            return cover_vertices
        
        cover_vertices = []
        c = Set & -Set
        r = Set + c 
        Set = (((r ^ Set) >> 2) // c) | r
    
    return []

def findMinCover(n, m):
    global gr
    left = 1
    right = n 
    
    while (right > left):
        mid = (left + right) >> 1
        cover_vertices = isCover(n, mid, m)
        
        if cover_vertices:
            right = mid
            vertex_cover = cover_vertices
        else:
            left = mid + 1
    
    return vertex_cover

def insertEdge(u, v):
    global gr
    gr[u][v] = 1
    gr[v][u] = 1 

maxn = 25
gr = [[0] * maxn for i in range(maxn)]

def draw_graph():
    global objects, constraints, V, E, vertex_cover, gr
    objects = entry_objects.get().split()
    node_map = {node: index + 1 for index, node in enumerate(objects)}

    constraints_input = entry_constraints.get()
    constraints = [tuple(pair.split(',')) for pair in constraints_input.split()]
    
    gr = [[0] * maxn for i in range(maxn)] 
    
    for u, v in constraints:
        insertEdge(node_map[u], node_map[v])

    V = len(objects)
    E = len(constraints)

    vertex_cover = findMinCover(V, E)
    vertex_cover_names = [objects[vertex - 1] for vertex in vertex_cover]

    global graph_canvas
    plt.clf()  # Clear previous plot

    # Create a graph
    G = nx.Graph()
    # background color
    

    # Add nodes and edges to the graph
    G.add_nodes_from(objects)
    G.add_edges_from(constraints)

    # Draw the graph with circular layout
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=node_color, node_size=2000, font_size=15, font_color='white', font_weight='bold', width=2, edge_color='black', style='dotted')

    # Draw canvas
    graph_canvas.draw()

# function to highlight the vertex cover in red
def highlight_vertex_cover():
    global objects, constraints, V, E, vertex_cover, gr
    objects = entry_objects.get().split()
    node_map = {node: index + 1 for index, node in enumerate(objects)}

    constraints_input = entry_constraints.get()
    constraints = [tuple(pair.split(',')) for pair in constraints_input.split()]
    
    gr = [[0] * maxn for i in range(maxn)] 
    
    for u, v in constraints:
        insertEdge(node_map[u], node_map[v])

    V = len(objects)
    E = len(constraints)

    vertex_cover = findMinCover(V, E)
    vertex_cover_names = [objects[vertex - 1] for vertex in vertex_cover]

    global graph_canvas
    plt.clf()  # Clear previous plot

    # Create a graph
    G = nx.Graph()

    # Add nodes and edges to the graph
    G.add_nodes_from(objects)
    G.add_edges_from(constraints)

    # Draw the graph with circular layout
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=node_color, node_size=2000, font_size=15, font_color='white', font_weight='bold', width=2, edge_color='black', style='dotted')

    # Highlight the vertices in the vertex cover
    nx.draw_networkx_nodes(G, pos, nodelist=vertex_cover_names, node_color='red', node_size=2500)

    # Draw canvas
    graph_canvas.draw()

#function to delete the vertex cover from the graph
def remove_vertex_cover():
    global objects, constraints, V, E, vertex_cover, gr
    objects = entry_objects.get().split()
    node_map = {node: index + 1 for index, node in enumerate(objects)}

    constraints_input = entry_constraints.get()
    constraints = [tuple(pair.split(',')) for pair in constraints_input.split()]
    
    gr = [[0] * maxn for i in range(maxn)] 
    
    for u, v in constraints:
        insertEdge(node_map[u], node_map[v])

    V = len(objects)
    E = len(constraints)

    vertex_cover = findMinCover(V, E)
    vertex_cover_names = [objects[vertex - 1] for vertex in vertex_cover]

    global graph_canvas
    plt.clf()  # Clear previous plot

    # Create a graph
    G = nx.Graph()

    # Add nodes to the graph excluding the vertex cover
    non_cover_nodes = set(objects) - set(vertex_cover_names)
    G.add_nodes_from(non_cover_nodes)

    # Add edges to the graph excluding the edges connected to the vertex cover
    non_cover_edges = [(u, v) for u, v in constraints if u not in vertex_cover_names and v not in vertex_cover_names]
    G.add_edges_from(non_cover_edges)

    # Draw the graph with circular layout
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=node_color, node_size=2000, font_size=15, font_color='white', font_weight='bold', width=2, edge_color='black', style='dotted')

    # Draw canvas
    graph_canvas.draw()

# Function to change node color
def change_node_color():
    global node_color
    color = colorchooser.askcolor(title="Choose Node Color")[1]
    node_color = color

# Function to clear the canvas
def clear_canvas():
    global graph_canvas
    plt.clf()
    graph_canvas.draw()
    #empty the entry widgets
    entry_objects.delete(0, tk.END)
    entry_constraints.delete(0, tk.END)
    
# Function to reset the global variables
def reset():
    global objects, constraints, V, E, vertex_cover, gr
    objects = []
    constraints = []
    V = 0
    E = 0
    vertex_cover = []
    gr = [[0] * maxn for i in range(maxn)] 

def quit():
    root.quit()
    root.destroy()
# Create the main window
root = tk.Tk()
root.title("Minimum Vertex Cover")
root.geometry("1200x800")
#make it pop up in the center of the screen
# root.eval('tk::PlaceWindow . center')

# Define colors
bg_color = "white"  # Light gray background
button_color = "#741A1F"  # Blue-gray button color
text_color = "white"  # Black text color
node_color = 'black'  # Default node color

# Set window background color
root.config(bg=bg_color)

# Create a frame for objects and constraints input
input_frame = tk.Frame(root, bg=bg_color)
input_frame.pack(side=tk.LEFT, padx=50, pady=50)

# Create labels and entry widgets for objects and constraints
label_objects = tk.Label(input_frame, text="Objects:", bg=bg_color, fg="#9B522A", font=('Calibri', 30, 'bold'))
label_objects.grid(row=0, column=0, sticky="", padx=5)
label_example = tk.Label(input_frame, text="e.g. cat dog chicken mouse bird", bg=bg_color, fg="gray", font=('Calibri', 15))
label_example.grid(row=1, column=0, sticky="", padx=5)
entry_objects_text = tk.StringVar()
entry_objects = tk.Entry(input_frame, textvariable=entry_objects_text, width=30)
entry_objects.grid(row=2, column=0, padx=5, pady=(0, 10))
entry_objects.config(fg='#741A1F', font=('Calibri', 20), relief=tk.RIDGE, bd=2, insertbackground='#741A1F', highlightthickness=2,  highlightcolor='#741A1F', selectbackground='gray')

label_constraints = tk.Label(input_frame, text="Constraints:", bg=bg_color, fg="#9B522A", font=('Calibri', 30, 'bold'))
label_constraints.grid(row=3, column=0, sticky="", padx=5)
label_example = tk.Label(input_frame, text="e.g. cat,dog cat,mouse chicken,bird", bg=bg_color, fg="gray", font=('Calibri', 15))
label_example.grid(row=4, column=0, sticky="", padx=5)
entry_constraints_text = tk.StringVar()
entry_constraints = tk.Entry(input_frame, textvariable=entry_constraints_text, width=30)
entry_constraints.grid(row=5, column=0, padx=5, pady=(0, 30))
entry_constraints.config(fg='#741A1F', font=('Calibri', 20), relief=tk.RIDGE, bd=2, insertbackground='#741A1F', highlightthickness=2,  highlightcolor='#741A1F', selectbackground='gray')

# Create buttons with improved appearance
button_draw = tk.Button(input_frame, text="Draw Graph", command=draw_graph, bg=button_color, fg=text_color, width=20, font=('Calibri', 20, 'bold'))
button_draw.grid(row=6, column=0, pady=(0, 5))

button_find_vertex_cover = tk.Button(input_frame, text="Find Vertex Cover", command=highlight_vertex_cover, bg=button_color, fg=text_color, width=20, font=('Calibri', 20, 'bold'))
button_find_vertex_cover.grid(row=7, column=0, pady=(0, 5))

button_change_color = tk.Button(input_frame, text="Change Node Color", command=change_node_color, bg=button_color, fg=text_color, width=20, font=('Calibri', 20, 'bold'))
button_change_color.grid(row=8, column=0, pady=(0, 5))

button_remove_vertex_cover = tk.Button(input_frame, text="Remove Vertex Cover", command=remove_vertex_cover, bg=button_color, fg=text_color, width=20, font=('Calibri', 20, 'bold'))
button_remove_vertex_cover.grid(row=9, column=0, pady=(0, 5))

button_clear_canvas = tk.Button(input_frame, text="Clear Canvas", command=clear_canvas, bg=button_color, fg=text_color, width=20, font=('Calibri', 20, 'bold'))
button_clear_canvas.grid(row=10, column=0, pady=(0, 5))

button_quit = tk.Button(input_frame, text="Quit", command=quit, bg=button_color, fg=text_color, width=20, font=('Calibri', 20, 'bold'))
button_quit.grid(row=11, column=0, pady=(0, 5))

# Create a frame to hold the graph
graph_frame = tk.Frame(root, bg='white')
graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create a figure for plotting
fig = plt.figure(figsize=(5, 5))
graph_canvas = FigureCanvasTkAgg(fig, master=graph_frame)
graph_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Run the main loop
root.mainloop()
# reset 
reset()
