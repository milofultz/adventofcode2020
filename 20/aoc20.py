from collections import defaultdict
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


def get_corners_and_edges(tileset: dict) -> (list, list):
    edge_lookup = defaultdict(list)
    for tile_id, tile in tileset.items():
        current_tile = deepcopy(tile)
        for i in range(4):
            edge = "".join(x for x in current_tile[0])
            edge_lookup[edge].append(tile_id)
            edge_lookup[edge[::-1]].append(tile_id)
            current_tile = np.rot90(current_tile)
    edge_count = defaultdict(int)
    for side, tile_ids in edge_lookup.items():
        if len(tile_ids) == 1:
            edge_count[tile_ids[0]] += 1
    corners = [num for num in edge_count.keys() if edge_count[num] == 4]
    edges = [num for num in edge_count.keys() if num not in corners]
    return corners, edges


if __name__ == "__main__":
    # Part 1
    tileset = parse_data(P_IN)
    corner_ids, edge_ids = get_corners_and_edges(tileset)
    print(np.product(corner_ids))
