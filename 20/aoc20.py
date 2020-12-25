from collections import defaultdict, deque
from copy import deepcopy
from math import sqrt
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
    inside_ids = deque([num for num in all_ids if num not in corner_ids and num not in edge_ids])
    organized_ids = {
        "corners": corner_ids,
        "edges": edge_ids,
        "insides": inside_ids
    }
    return edge_list, organized_ids


def assemble_tiles(tiles: dict, edges: list, organized_ids: dict) -> np.array:
    macro_side_length = int(sqrt(len(tiles)))
    assembled = make_empty_list(macro_side_length)
    available_tiles = deepcopy(organized_ids)
    for y in range(len(assembled)):
        for x in range(len(assembled[y])):
            search = make_search_parameters(x, y, macro_side_length)
            tile_group = deepcopy(available_tiles[search["pool"]])
            adjacent_edges = {
                "top": ("" if search["top"] == "edge" else
                        "".join(str(char) for char in assembled[y-1][x][9])),
                "left": ("" if search["left"] == "edge" else
                         "".join(str(line[9]) for line in assembled[y][x-1]))
            }
            found = False
            while not found:
                current_tile = tiles[tile_group[0]]
                current_id = tile_group.popleft()
                for i in range(8):
                    if i % 4 == 0:
                        current_tile = np.flip(current_tile, 1)
                    current_tile = np.rot90(current_tile)
                    current_edges = {
                        "top": "".join(str(char) for char in current_tile[0, 0:]),
                        "bottom": "".join(str(char) for char in current_tile[9, 0:]),
                        "left": "".join(str(char) for char in current_tile[0:, 0]),
                        "right": "".join(str(char) for char in current_tile[0:, 9]),
                    }
                    if search["top"] == "edge" and current_edges["top"] not in edges:
                        continue
                    elif search["top"] == "inside" and current_edges["top"] != adjacent_edges["top"]:
                        continue
                    if search["bottom"] == "edge" and current_edges["bottom"] not in edges:
                        continue
                    if search["left"] == "edge" and current_edges["left"] not in edges:
                        continue
                    elif search["left"] == "inside" and current_edges["left"] != adjacent_edges["left"]:
                        continue
                    if search["right"] == "edge" and current_edges["right"] not in edges:
                        continue
                    found = True
                    break
            assembled[y][x] = current_tile
            available_tiles[search["pool"]].remove(current_id)
    return assembled


def make_empty_list(length: int) -> list:
    output = list()
    for i in range(length):
        output.append(list())
        for j in range(length):
            output[i].append(None)
    return output

def make_search_parameters(x: int, y: int, length: int) -> dict:
        search = dict()
        edge_count = 0
        search["left"] = "inside"
        search["top"] = "inside"
        if x == 0 or x == length - 1:
            search["left" if x == 0 else "right"] = "edge"
            edge_count += 1
        if y == 0 or y == length - 1:
            search["top" if y == 0 else "bottom"] = "edge"
            edge_count += 1
        if edge_count != 0:
            search["pool"] = "corners" if edge_count == 2 else "edges"
        else:
            search["pool"] = "insides"
        for side in ["top", "bottom", "left", "right"]:
            if side not in search:
                search[side] = None
        return search


def trim_all_tiles(tiles: list) -> list:
    side_length = len(tiles[0])
    trimmed_tiles = deepcopy(tiles)
    for y in range(side_length):
        for x in range(side_length):
            trimmed_element = deepcopy(trimmed_tiles[y][x])
            trimmed_element = np.delete(trimmed_element, 0, 0)
            trimmed_element = np.delete(trimmed_element, 0, 1)
            trimmed_element = np.delete(trimmed_element, -1, 0)
            trimmed_element = np.delete(trimmed_element, -1, 1)
            trimmed_tiles[y][x] = trimmed_element
    return trimmed_tiles


if __name__ == "__main__":
    # Part 1
    tileset = parse_data(P_INS)
    edge_lookup = make_edge_lookup(tileset)
    outside_edges, organized_ids = get_edge_list_and_organized_ids(edge_lookup, tileset.keys())
    print(np.product(organized_ids["corners"]))
    # Part 2
    assembled_tiles = assemble_tiles(tileset, outside_edges, organized_ids)
    borderless_tiles = trim_all_tiles(assembled_tiles)
