from graph_depth import GraphDepth
from graph_breadth import GraphBreadth
from util import write_file_result

for i in range(1, 21):
    gpath = f"in/graph_{i}"
    gd = GraphDepth(gpath)
    gb = GraphBreadth(gpath)
    write_file_formatted(gd, 0, f"run_result/graph_{i}_depth.gdf")
    write_file_formatted(gb, 0, f"run_result/graph_{i}_breadth.gdf")