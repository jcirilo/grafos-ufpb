from graph import Graph

def write_out_file(colors, path):
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
        path = f"in/graph_{i}"
        g = Graph(path)
        dfs = g.search_dfs(0)
        bfs = g.search_bfs(0)
        write_out_file(colors=dfs, path=f"out/graph_{i}_dfs.gdf")
        write_out_file(colors=bfs, path=f"out/graph_{i}_bfs.gdf")

run()