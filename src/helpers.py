# Helper Functions
from typing import List, Dict, Tuple, Callable, Set
from collections import Counter
from math import sqrt

def arr_to_dict(arr: List) -> Dict:
    return dict(Counter(arr))

# Euclidean Distance Between Two 3D Points
def euclidean_distance(coords1: Tuple[float, float, float], 
                       coords2: Tuple[float, float, float]) -> float:
    if any(v is None for v in (*coords1, *coords2)):
        return 0
    (x1, y1, z1) = coords1
    (x2, y2, z2) = coords2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

# Hamming Distance of Two Arrays
def hamming_distance(list1: List, list2: List) -> int:
    assert len(list1) == len(list2), "Lists must have the same length"
    return sum(el1 != el2 for el1, el2 in zip(list1, list2))

# Calculates the distance between Two Sets by comparing their union and intersection
def jaccard_distance(x: Set, y: Set) -> float:
    union = x.union(y)
    intersect = x.intersection(y)
    return (len(union) - len(intersect)) / len(union)

# Add an x, y, z coordinates tuple to the current round's list of positions for each player
def add_trajectory(id: str, 
                   round: int, 
                   coords: Tuple[float, float], 
                   trajectories: Dict[str, Dict[int, List[Tuple[float, float]]]]) -> None:
    if id not in trajectories:
        trajectories[id] = {}
    if round not in trajectories[id]:
        trajectories[id][round] = [coords]
    else:
        trajectories[id][round].append(coords)
