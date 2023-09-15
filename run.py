from graph import Graph

def write_search(colored_edges, path):
    file = open(path, 'w', encoding='utf-8')
    color_palette = ['0,0,0','0,0,255','255,0,0','255,255,0','0,255,0']
    gsize = len(colored_edges)
    file.write('nodedef>name VARCHAR,label VARCHAR\n')
    for i in range(gsize):
        file.write(f"{i+1},{i+1}\n")
    file.write('edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n')
    for i in range(gsize):
        for j in range(gsize):
            color_code = colored_edges[i][j]
            if color_code:
                line = f"{i+1},{j+1},false,'{color_palette[color_code]}'\n"
                file.write(line)

for i in range(1, 21):
    path = f"in/graph_{i}"
    g = Graph(path)
    print("graph_{}\tdiametro: {}\traio: {}".format(i, g.diameter(), g.radius()))
    write_search(g.depth_search(0), f"out/graph_{i}_dfs.gdf")
    write_search(g.breadth_search(0, only_lvl=False), f"out/graph_{i}_bfs.gdf")
