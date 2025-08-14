from typing import List, Dict, TypedDict, Union
import numpy as np
from numpy.typing import NDArray

from fc_value import decode, encode
from fc_dict import FCDict


class FCElementType(TypedDict):
    name: str 
    fc_id: int 
    dim: int 
    order: int 
    nodes: int 
    structure: Dict[int, np.ndarray]
    edges: List[List[int]]
    facets: List[List[int]]
    tetras: List[List[int]]


FC_ELEMENT_TYPES: Dict[int, FCElementType] = {
    0: {
        'name': 'NONE',
        'fc_id': 0,
        'dim': 0,
        'order': 0,
        'nodes': 0,
        'edges': [],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    38: {
        'name': 'LUMPMASS3D',
        'fc_id': 38,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    40: {
        'name': 'LUMPMASS6D',
        'fc_id': 40,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    82: {
        'name': 'LUMPMASS2D',
        'fc_id': 82,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    99: {
        'name': 'POINT3D',
        'fc_id': 99,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    100: {
        'name': 'POINT2D',
        'fc_id': 100,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    101: {
        'name': 'POINT6D',
        'fc_id': 101,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    105: {
        'name': 'LUMPMASS2DR',
        'fc_id': 105,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    36: {
        'name': 'BEAM26',
        'fc_id': 36,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    37: {
        'name': 'BEAM36',
        'fc_id': 37,
        'dim': 1,
        'order': 2,
        'nodes': 3,
        'edges': [[0, 2, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    39: {
        'name': 'SPRING3D',
        'fc_id': 39,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    41: {
        'name': 'SPRING6D',
        'fc_id': 41,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    89: {
        'name': 'BEAM27',
        'fc_id': 89,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    90: {
        'name': 'BEAM37',
        'fc_id': 90,
        'dim': 1,
        'order': 2,
        'nodes': 3,
        'edges': [[0, 2, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    107: {
        'name': 'BAR2',
        'fc_id': 107,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    108: {
        'name': 'BAR3',
        'fc_id': 108,
        'dim': 1,
        'order': 2,
        'nodes': 3,
        'edges': [[0, 2, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    109: {
        'name': 'CABLE2',
        'fc_id': 109,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    110: {
        'name': 'CABLE3',
        'fc_id': 110,
        'dim': 1,
        'order': 2,
        'nodes': 3,
        'edges': [[0, 2, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    10: {
        'name': 'TRI3',
        'fc_id': 10,
        'dim': 2,
        'order': 1,
        'nodes': 3,
        'edges': [[0, 1, 2, 0]],
        'facets': [[0, 1, 2]],
        'tetras': [],
        'structure': {}
    },
    11: {
        'name': 'TRI6',
        'fc_id': 11,
        'dim': 2,
        'order': 2,
        'nodes': 6,
        'edges': [[0, 3, 1, 4, 2, 5, 0]],
        'facets': [[0, 3, 1, 4, 2, 5]],
        'tetras': [],
        'structure': {}
    },
    12: {
        'name': 'QUAD4',
        'fc_id': 12,
        'dim': 2,
        'order': 1,
        'nodes': 4,
        'edges': [[0, 1, 2, 3, 0]],
        'facets': [[0, 1, 2, 3]],
        'tetras': [],
        'structure': {}
    },
    13: {
        'name': 'QUAD8',
        'fc_id': 13,
        'dim': 2,
        'order': 2,
        'nodes': 8,
        'edges': [[0, 4, 1, 5, 2, 6, 3, 7, 0]],
        'facets': [[0, 4, 1, 5, 2, 6, 3, 7]],
        'tetras': [],
        'structure': {}
    },
    29: {
        'name': 'MITC3',
        'fc_id': 29,
        'dim': 2,
        'order': 1,
        'nodes': 3,
        'edges': [[0, 1, 2, 0]],
        'facets': [[0, 1, 2]],
        'tetras': [],
        'structure': {}
    },
    30: {
        'name': 'MITC6',
        'fc_id': 30,
        'dim': 2,
        'order': 2,
        'nodes': 6,
        'edges': [[0, 3, 1, 4, 2, 5, 0]],
        'facets': [[0, 3, 1, 4, 2, 5]],
        'tetras': [],
        'structure': {}
    },
    31: {
        'name': 'MITC4',
        'fc_id': 31,
        'dim': 2,
        'order': 1,
        'nodes': 4,
        'edges': [[0, 1, 2, 3, 0]],
        'facets': [[0, 1, 2, 3]],
        'tetras': [],
        'structure': {}
    },
    32: {
        'name': 'MITC8',
        'fc_id': 32,
        'dim': 2,
        'order': 2,
        'nodes': 8,
        'edges': [[0, 4, 1, 5, 2, 6, 3, 7, 0]],
        'facets': [[0, 4, 1, 5, 2, 6, 3, 7]],
        'tetras': [],
        'structure': {}
    },
    1: {
        'name': 'TETRA4',
        'fc_id': 1,
        'dim': 3,
        'order': 1,
        'nodes': 4,
        'edges': [[0, 1, 2, 0], [0, 3], [1, 3], [2, 3]],
        'facets': [[0, 2, 1], [0, 1, 3], [1, 2, 3], [2, 0, 3]],
        'tetras': [[0, 1, 2, 3]],
        'structure': {}
    },
    2: {
        'name': 'TETRA10',
        'fc_id': 2,
        'dim': 3,
        'order': 2,
        'nodes': 10,
        'edges': [[0, 4, 1, 5, 2, 6, 0], [0, 7, 3], [1, 8, 3], [2, 9, 3]],
        'facets': [[0, 6, 2, 5, 1, 4], [0, 4, 1, 8, 3, 5], [1, 5, 2, 9, 3, 8], [2, 6, 0, 5, 3, 9]],
        'tetras': [],
        'structure': {}
    },
    3: {
        'name': 'HEX8',
        'fc_id': 3,
        'dim': 3,
        'order': 1,
        'nodes': 8,
        'edges': [[0, 1, 2, 3, 0], [4, 5, 6, 7, 4], [0, 4], [1, 5], [2, 6], [3, 7]],
        'facets': [[3, 2, 1, 0], [4, 5, 6, 7], [1, 2, 6, 5], [0, 1, 5, 4], [0, 4, 7, 3], [2, 3, 7, 6]],
        'tetras': [[1, 3, 4, 6], [3, 1, 4, 0], [1, 3, 6, 2], [4, 1, 6, 5], [3, 4, 6, 7]],
        'structure': {}
    },
    4: {
        'name': 'HEX20',
        'fc_id': 4,
        'dim': 3,
        'order': 2,
        'nodes': 20,
        'edges': [[0, 8, 1, 9, 2, 10, 3, 11, 0], [4, 12, 5, 13, 6, 14, 7, 15, 4],
                  [0, 0, 4], [1, 0, 5], [2, 0, 6], [3, 0, 7]],
        'facets': [[3, 10, 2, 9, 1, 8, 0, 11], [4, 12, 5, 13, 6, 14, 7, 15], [1, 9, 2, 18, 6, 13, 5, 17],
                   [0, 8, 1, 17, 5, 12, 4, 16], [0, 16, 4, 15, 7, 19, 3, 11], [2, 10, 3, 19, 7, 14, 6, 18]],
        'tetras': [],
        'structure': {}
    },
    15: {
        'name': 'TETRA4S',
        'fc_id': 15,
        'dim': 3,
        'order': 1,
        'nodes': 4,
        'edges': [[0, 1, 2, 0], [0, 3], [1, 3], [2, 3]],
        'facets': [[0, 2, 1], [0, 1, 3], [1, 2, 3], [2, 0, 3]],
        'tetras': [[0, 1, 2, 3]],
        'structure': {}
    },
    16: {
        'name': 'TETRA10S',
        'fc_id': 16,
        'dim': 3,
        'order': 2,
        'nodes': 10,
        'edges': [[0, 4, 1, 5, 2, 6, 0], [0, 7, 3], [1, 8, 3], [2, 9, 3]],
        'facets': [[0, 6, 2, 5, 1, 4], [0, 4, 1, 8, 3, 5], [1, 5, 2, 9, 3, 8], [2, 6, 0, 5, 3, 9]],
        'tetras': [],
        'structure': {}
    },
    17: {
        'name': 'HEX8S',
        'fc_id': 17,
        'dim': 3,
        'order': 1,
        'nodes': 8,
        'edges': [[0, 1, 2, 3, 0], [4, 5, 6, 7, 4], [0, 4], [1, 5], [2, 6], [3, 7]],
        'facets': [[3, 2, 1, 0], [4, 5, 6, 7], [1, 2, 6, 5], [0, 1, 5, 4], [0, 4, 7, 3], [2, 3, 7, 6]],
        'tetras': [[1, 3, 4, 6], [3, 1, 4, 0], [1, 3, 6, 2], [4, 1, 6, 5], [3, 4, 6, 7]],
        'structure': {}
    },
    18: {
        'name': 'HEX20S',
        'fc_id': 18,
        'dim': 3,
        'order': 2,
        'nodes': 20,
        'edges': [[0, 8, 1, 9, 2, 10, 3, 11, 0], [4, 12, 5, 13, 6, 14, 7, 15, 4],
                  [0, 0, 4], [1, 0, 5], [2, 0, 6], [3, 0, 7]],
        'facets': [[3, 10, 2, 9, 1, 8, 0, 11], [4, 12, 5, 13, 6, 14, 7, 15], [1, 9, 2, 18, 6, 13, 5, 17],
                   [0, 8, 1, 17, 5, 12, 4, 16], [0, 16, 4, 15, 7, 19, 3, 11], [2, 10, 3, 19, 7, 14, 6, 18]],
        'tetras': [],
        'structure': {}
    },
    6: {
        'name': 'WEDGE6',
        'fc_id': 6,
        'dim': 3,
        'order': 1,
        'nodes': 5,
        'edges': [[0, 1, 2, 0], [3, 4, 5, 3], [0, 3], [1, 4], [2, 5]],
        'facets': [[0, 1, 2], [5, 4, 3], [0, 2, 5, 3], [0, 3, 4, 1], [1, 4, 5, 2]],
        'tetras': [[0, 5, 4, 3], [0, 4, 2, 1], [0, 2, 4, 5]],
        'structure': {}
    },
    7: {
        'name': 'WEDGE15',
        'fc_id': 7,
        'dim': 3,
        'order': 2,
        'nodes': 15,
        'edges': [[0, 5, 1, 6, 2, 7, 3, 8, 0], [0, 9, 4], [1, 10, 4], [2, 11, 4], [3, 12, 4]],
        'facets': [[3, 7, 2, 6, 1, 5, 0, 8],
                   [0, 5, 1, 10, 4, 9], [1, 6, 2, 11, 4, 10], [2, 7, 3, 12, 4, 11], [3, 8, 0, 9, 4, 12]],
        'tetras': [],
        'structure': {}
    },
    20: {
        'name': 'WEDGE6S',
        'fc_id': 20,
        'dim': 3,
        'order': 1,
        'nodes': 5,
        'edges': [[0, 1, 2, 0], [3, 4, 5, 3], [0, 3], [1, 4], [2, 5]],
        'facets': [[0, 1, 2], [5, 4, 3], [0, 2, 5, 3], [0, 3, 4, 1], [1, 4, 5, 2]],
        'tetras': [[0, 5, 4, 3], [0, 4, 2, 1], [0, 2, 4, 5]],
        'structure': {}
    },
    21: {
        'name': 'WEDGE15S',
        'fc_id': 21,
        'dim': 3,
        'order': 2,
        'nodes': 15,
        'edges': [[0, 5, 1, 6, 2, 7, 3, 8, 0], [0, 9, 4], [1, 10, 4], [2, 11, 4], [3, 12, 4]],
        'facets': [[3, 7, 2, 6, 1, 5, 0, 8],
                   [0, 5, 1, 10, 4, 9], [1, 6, 2, 11, 4, 10], [2, 7, 3, 12, 4, 11], [3, 8, 0, 9, 4, 12]],
        'tetras': [],
        'structure': {}
    },
    8: {
        'name': 'PYR5',
        'fc_id': 8,
        'dim': 3,
        'order': 1,
        'nodes': 5,
        'edges': [[0, 1, 2, 3, 0], [0, 4], [1, 4], [2, 4], [3, 4]],
        'facets': [[3, 2, 1, 0], [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4]],
        'tetras': [[1, 3, 4, 0], [3, 4, 1, 2]],
        'structure': {}
    },
    9: {
        'name': 'PYR13',
        'fc_id': 9,
        'dim': 3,
        'order': 2,
        'nodes': 13,
        'edges': [[0, 5, 1, 6, 2, 7, 3, 8, 0], [0, 9, 4], [1, 10, 4], [2, 11, 4], [3, 12, 4]],
        'facets': [[3, 7, 2, 6, 1, 5, 0, 8],
                   [0, 5, 1, 10, 4, 9], [1, 6, 2, 11, 4, 10], [2, 7, 3, 12, 4, 11], [3, 8, 0, 9, 4, 12]],
        'tetras': [],
        'structure': {}
    },
    22: {
        'name': 'PYR5S',
        'fc_id': 22,
        'dim': 3,
        'order': 1,
        'nodes': 5,
        'edges': [[0, 1, 2, 3, 0], [0, 4], [1, 4], [2, 4], [3, 4]],
        'facets': [[3, 2, 1, 0], [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4]],
        'tetras': [[1, 3, 4, 0], [3, 4, 1, 2]],
        'structure': {}
    },
    23: {
        'name': 'PYR13S',
        'fc_id': 23,
        'dim': 3,
        'order': 2,
        'nodes': 13,
        'edges': [[0, 5, 1, 6, 2, 7, 3, 8, 0], [0, 9, 4], [1, 10, 4], [2, 11, 4], [3, 12, 4]],
        'facets': [[3, 7, 2, 6, 1, 5, 0, 8],
                   [0, 5, 1, 10, 4, 9], [1, 6, 2, 11, 4, 10], [2, 7, 3, 12, 4, 11], [3, 8, 0, 9, 4, 12]],
        'tetras': [],
        'structure': {}
    },
    24: {
        'name': 'TRI3S',
        'fc_id': 24,
        'dim': 2,
        'order': 1,
        'nodes': 3,
        'edges': [[0, 1, 2, 0]],
        'facets': [[0, 1, 2]],
        'tetras': [],
        'structure': {}
    },
    25: {
        'name': 'TRI6S',
        'fc_id': 25,
        'dim': 2,
        'order': 2,
        'nodes': 6,
        'edges': [[0, 3, 1, 4, 2, 5, 0]],
        'facets': [[0, 3, 1, 4, 2, 5]],
        'tetras': [],
        'structure': {}
    },
    26: {
        'name': 'QUAD4S',
        'fc_id': 26,
        'dim': 2,
        'order': 1,
        'nodes': 4,
        'edges': [[0, 1, 2, 3, 0]],
        'facets': [[0, 1, 2, 3]],
        'tetras': [],
        'structure': {}
    },
    27: {
        'name': 'QUAD8S',
        'fc_id': 27,
        'dim': 2,
        'order': 2,
        'nodes': 8,
        'edges': [[0, 4, 1, 5, 2, 6, 3, 7, 0]],
        'facets': [[0, 4, 1, 5, 2, 6, 3, 7]],
        'tetras': [],
        'structure': {}
    },
    83: {
        'name': 'SPRING2D',
        'fc_id': 83,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    84: {
        'name': 'SHELL3S',
        'fc_id': 84,
        'dim': 2,
        'order': 1,
        'nodes': 3,
        'edges': [[0, 1, 2, 0]],
        'facets': [[0, 1, 2]],
        'tetras': [],
        'structure': {}
    },
    85: {
        'name': 'SHELL4S',
        'fc_id': 85,
        'dim': 2,
        'order': 1,
        'nodes': 4,
        'edges': [[0, 1, 2, 3, 0]],
        'facets': [[0, 1, 2, 3]],
        'tetras': [],
        'structure': {}
    },
    86: {
        'name': 'SHELL6S',
        'fc_id': 86,
        'dim': 2,
        'order': 2,
        'nodes': 6,
        'edges': [[0, 3, 1, 4, 2, 5, 0]],
        'facets': [[0, 3, 1, 4, 2, 5]],
        'tetras': [],
        'structure': {}
    },
    87: {
        'name': 'SHELL8S',
        'fc_id': 87,
        'dim': 2,
        'order': 2,
        'nodes': 8,
        'edges': [[0, 4, 1, 5, 2, 6, 3, 7, 0]],
        'facets': [[0, 4, 1, 5, 2, 6, 3, 7]],
        'tetras': [],
        'structure': {}
    },
    95: {
        'name': 'BEAM26S',
        'fc_id': 95,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    96: {
        'name': 'BEAM36S',
        'fc_id': 96,
        'dim': 1,
        'order': 2,
        'nodes': 3,
        'edges': [[0, 2, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    97: {
        'name': 'BEAM27S',
        'fc_id': 97,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    },
    98: {
        'name': 'BEAM37S',
        'fc_id': 98,
        'dim': 1,
        'order': 2,
        'nodes': 3,
        'edges': [[0, 2, 1]],
        'facets': [],
        'tetras': [],
        'structure': {}
    }
}


def split_facet(facet: List[int]) -> List[int]:
    if len(facet) == 3:
        return facet
    if len(facet) < 3:
        return []
    tail = facet[2:]
    tail.append(facet[1])
    tris = [facet[-1], facet[0], facet[1]]
    tris.extend(split_facet(tail))
    return tris


def split_edge(edge: List[int]) -> List[int]:
    if len(edge) == 2:
        return edge
    if len(edge) < 2:
        return []
    tail = edge[1:]
    pairs = [edge[0], edge[1]]
    pairs.extend(split_edge(tail))
    return pairs


def split_polihedron(tetra: List[int]) -> List[int]:
    return tetra

def make_structure():
    for eid in FC_ELEMENT_TYPES:
        element_type = FC_ELEMENT_TYPES[eid]
        element_type['structure'][0] = np.arange(element_type['nodes'], dtype=np.int32)

        if element_type['dim'] > 0:

            pairs = []
            for edge in element_type['edges']:
                pairs.extend(split_edge(edge))

            element_type['structure'][1] = np.array(pairs, dtype=np.int32)

        if element_type['dim'] > 1:

            trangles = []
            for facet in element_type['facets']:
                trangles.extend(split_facet(facet))

            element_type['structure'][2] = np.array(trangles, dtype=np.int32)

        if element_type['dim'] > 2:

            tetras = []
            for tetra in element_type['tetras']:
                tetras.extend(split_polihedron(tetra))

            element_type['structure'][3] = np.array(tetras, dtype=np.int32)

# Инициализация предрасчитанных структур для типов элементов
make_structure()


class FCElem(TypedDict):
    """
    Определяет один конечный элемент в сетке.
    """
    id: int  # Уникальный идентификатор элемента
    block: int  # ID блока, к которому принадлежит элемент
    parent_id: int  # ID родительского элемента (используется при измельчении сетки)
    type: FCElementType  # Словарь, описывающий тип элемента (e.g., HEX8, TETRA4)
    nodes: List[int]  # Список ID узлов, образующих элемент
    order: int  # Порядок элемента (1 - линейный, 2 - квадратичный)


class FCNode(TypedDict):
    """
    Определяет один узел в конечно-элементной сетке.
    """
    id: int  # Уникальный идентификатор узла
    xyz: NDArray[np.float64]  # Numpy массив с 3-мя координатами [x, y, z]


class FCElems:
    """
    Контейнер для хранения всех элементов модели, сгруппированных по типам.

    Внутри `FCElems` элементы хранятся не в одном списке, а в словаре `data`,
    где ключами являются строковые имена типов элементов (e.g., 'HEX8', 'TETRA4'),
    а значениями - объекты `FCDict`, содержащие элементы соответствующего типа.

    Этот класс также управляет общей кодировкой и декодировкой всего набора
    элементов в/из формата .fc.
    """

    data: Dict[str, FCDict[FCElem]]

    def __init__(self, data=None):
        self.data = {
            fc_type['name']: FCDict() for fc_type in FC_ELEMENT_TYPES.values()
        }

        if data:
            self.decode(data)


    def decode(self, data=None):
        if data is None:
            return

        elem_blocks = decode(data.get('elem_blocks', ''))
        elem_orders = decode(data.get('elem_orders', ''))
        elem_parent_ids = decode(data.get('elem_parent_ids', ''))
        elem_types = decode(data.get('elem_types', ''), np.dtype('int8'))
        elem_ids = decode(data.get('elemids',''))
        elem_nodes = decode(data.get('elems', ''))

        elem_sizes = np.vectorize(lambda t: FC_ELEMENT_TYPES[t]['nodes'])(elem_types)
        elem_offsets = [0, *np.cumsum(elem_sizes)]

        for i, eid in enumerate(elem_ids):
            fc_type = FC_ELEMENT_TYPES[elem_types[i]]

            self.data[fc_type['name']][eid] = {
                'id': eid,
                'type': fc_type,
                'nodes': elem_nodes[elem_offsets[i]:elem_offsets[i+1]].tolist(),
                'block': elem_blocks[i],
                'order': elem_orders[i],
                'parent_id': elem_parent_ids[i],
            }


    def encode(self):

        elems_count = len(self)

        elem_ids: NDArray = np.zeros(elems_count, np.int32)
        elem_blocks: NDArray = np.zeros(elems_count, np.int32)
        elem_orders: NDArray = np.zeros(elems_count, np.int32)
        elem_parent_ids: NDArray = np.zeros(elems_count, np.int32)
        elem_types: NDArray = np.zeros(elems_count, np.int8)

        for i, elem in enumerate(self):
            elem_ids[i] = elem['id']
            elem_blocks[i] = elem['block']
            elem_parent_ids[i] = elem['parent_id']
            elem_orders[i] = elem['order']
            elem_types[i] = elem['type']['fc_id']

        elem_nodes: NDArray = np.array(self.nodes_list, np.int32)

        return {
            "elem_blocks": encode(elem_blocks),
            "elem_orders": encode(elem_orders),
            "elem_parent_ids": encode(elem_parent_ids),
            "elem_types": encode(elem_types),
            "elemids": encode(elem_ids),
            "elems": encode(elem_nodes),
            "elems_count": elems_count,
        }


    def __len__(self):
        return sum([len(self.data[typename]) for typename in self.data])

    def __bool__(self):
        return len(self) > 0

    def __iter__(self):
        for typename in self.data:
            for elem in self.data[typename]:
                yield elem

    def __contains__(self, key):
        for tp in self.data:
            if key in self.data[tp]:
                return True
        return False

    def __getitem__(self, key:Union[int, str]):
        if isinstance(key, str):
            return self.data[key]
        elif isinstance(key, int):
            for typename in self.data:
                if key in self.data[typename]:
                    return self.data[typename][key]
        raise KeyError(f'{key}')

    def __setitem__(self, key:int, item: FCElem):
        self.data[item['type']['name']].add(item)

    @property
    def nodes_list(self):
        return [node for elem in self for node in elem['nodes']]

    def compress(self):
        index_map = {elem['id']: i + 1 for i, elem in enumerate(self)}
        self.reindex(index_map)
        return index_map

    def reindex(self, index_map):
        for typename in self.data:
            self.data[typename].reindex(index_map)

    @property
    def max_id(self):
        max_id = 0
        for tp in self.data:
            if max_id < self.data[tp].max_id:
                max_id = self.data[tp].max_id
        return max_id

    def add(self, item: FCElem):
        if item['id'] in self or item['id'] < 1:
            item['id'] = self.max_id+1

        return self.data[item['type']['name']].add(item)

