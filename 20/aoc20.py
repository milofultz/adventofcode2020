from collections import defaultdict, deque
from copy import deepcopy
import numpy as np


P_IN = "aoc20-data"
P_INS = "aoc20-data-small"


def parse_data(fp: str) -> dict:
    with open(fp, 'r') as f:
        data = f.read().split("\n\n")
    output = dict()
    for entry in data:
        key, value = entry.split("\n", 1)
        key = int(key[5:-1])
        value = parse_array(value)
        output[key] = value
    return output


def parse_array(raw: str) -> np.array:
    array = []
    for line in raw.split("\n"):
        array.append(list(line))
    return np.array(array)


def make_edge_lookup(tileset: dict) -> dict:
    edge_lookup = defaultdict(list)
    for tile_id, tile in tileset.items():
        current_tile = deepcopy(tile)
        for i in range(4):
            edge = "".join(x for x in current_tile[0])
            edge_lookup[edge].append(tile_id)
            edge_lookup[edge[::-1]].append(tile_id)
            current_tile = np.rot90(current_tile)
    return edge_lookup


def get_edge_list_and_organized_ids(edges: dict, all_ids: list) -> (list, dict):
    edge_count = defaultdict(int)
    # Edges are a unique side that are only found on one tile
    edge_list = list()
    for edge, id_list in edges.items():
        if len(id_list) == 1:
            edge_count[id_list[0]] += 1
            edge_list.append(edge)
    # Corners have two unique sides (four if flipped)
    edge_ids = deque([num for num in edge_count.keys() if edge_count[num] == 2])
    corner_ids = deque([num for num in edge_count.keys() if edge_count[num] > 2])
    inside_ids = deque([num for num in all_ids if num not in sum([corner_ids, edge_ids], [])])
    organized_ids = {
        "corners": corner_ids,
        "edges": edge_ids,
        "insides": inside_ids
    }
    return edge_list, organized_ids


if __name__ == "__main__":
    # Part 1
    tileset = parse_data(P_IN)
    edge_lookup = make_edge_lookup(tileset)
    outside_edges, organized_ids = get_edge_list_and_organized_ids(edge_lookup, tileset.keys())
    print(np.product(organized_ids["corners"]))
    # Part 2
