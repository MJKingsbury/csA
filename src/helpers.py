# Helper Functions
from typing import List, Dict, Tuple
from collections import Counter
from math import sqrt

def arr_to_dict(arr: List) -> Dict:
    return dict(Counter(arr))

# Euclidean Distance Between Two 3D Points
def calculate_distance(coords1: Tuple[float, float, float], 
                       coords2: Tuple[float, float, float]) -> float:
    if any(v is None for v in (*coords1, *coords2)):
        return 0
    (x1, y1, z1) = coords1
    (x2, y2, z2) = coords2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

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