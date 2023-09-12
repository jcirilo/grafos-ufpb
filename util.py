def write_file_formatted(graph, first_node, path):
    color_palette = ['0,0,0','0,0,255','255,0,0','0,255,0','255,255,0']
    file = open(path, 'w', encoding='utf-8')
    n = graph.n
    color_matrix = graph.search(first_node)
    file.write('nodedef>name VARCHAR,label VARCHAR\n')
    for i in range(n):
        file.write(f"{i+1},{i+1}\n")
    file.write('edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n')
    for i in range(n):
        for j in range(n):
            color_code = color_matrix[i][j]
            if color_code:
                line = f"{i+1},{j+1},false,'{color_palette[color_code]}'\n"
                file.write(line)