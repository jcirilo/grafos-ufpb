from graph import Graph

def write_out_file(path, colors):
    n = len(colors)
    f = open(file=path, mode='w', encoding='utf-8')
    f.write("nodedef>name VARCHAR,label VARCHAR\n")
    for i in range(1, n+1):
        f.write(f"{i},{i}\n")
    f.write("edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n")
    for i in range(n):
        for j in range(n):
            color = colors[i][j]
            if color:
                f.write(f"{i+1},{j+1},false,{color}\n")

def run():
    for i in range(1, 21):
        path = f"in/p2/graph_{i}"
        g = Graph(path)
        print("grafo %2d, diametro: %d, raio: %d, dmed: %1.16f" % (i, g.diameter(), g.radius(), g.apl()))
        #dfs = g.search_dfs(0)
        #bfs = g.search_bfs(0)
        #write_out_file(path=f"out/p2/graph_{i}_dfs.gdf", colors=dfs)
        #write_out_file(path=f"out/p2/graph_{i}_bfs.gdf", colors=bfs)

run()