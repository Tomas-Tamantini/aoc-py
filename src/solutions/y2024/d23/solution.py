from src.core.io_handler import IOHandler
from src.solutions.shared.graph import UndirectedGraph
from src.solutions.shared.parser import parse_csv
from src.solutions.y2024.d23.logic.cliques import cliques


def solve(io_handler: IOHandler) -> None:
    prob_id = 2024, 23
    graph = UndirectedGraph()
    for pair in parse_csv(io_handler.input_reader(*prob_id), separator="-"):
        graph.add_edge(*pair)
    num_three_cliques = 0
    max_clique: frozenset[str] = frozenset()
    io_handler.progress_monitor(*prob_id, part=1).estimate_remaining_time(
        estimation="5s"
    )
    for clique in cliques(graph):
        clique_size = len(clique)
        if clique_size == 3 and any(node.startswith("t") for node in clique):
            num_three_cliques += 1
        if clique_size > len(max_clique):
            max_clique = clique
    io_handler.write_result(*prob_id, part=1, result=num_three_cliques)
    password = ",".join(sorted(max_clique))
    io_handler.write_result(*prob_id, part=2, result=password)
