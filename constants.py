from typing import List, Dict, TypedDict
import numpy as np


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


# Dependency (const_types) enumeration mapping
DEPENDENCY_TYPES: Dict[int, str] = {
    0: "CONSTANT",
    1: "TABULAR_X",
    2: "TABULAR_Y",
    3: "TABULAR_Z",
    4: "TABULAR_TIME",
    5: "TABULAR_TEMPERATURE",
    6: "FORMULA",
    7: "TABULAR_FREQUENCY",
    8: "TABULAR_STRAIN",
    10: "TABULAR_ELEMENT_ID",
    11: "TABULAR_NODE_ID",
    12: "TABULAR_MODE_ID",
}

DEPENDENCY_TYPES_REVERSE: Dict[str, int] = {v: k for k, v in DEPENDENCY_TYPES.items()}


# Material property type codes per group
MATERIAL_PROPERTY_TYPES: Dict[str, Dict[int, str]] = {
    "elasticity": {
        0: "HOOK",
        1: "HOOK_ORTHOTROPIC",
        2: "HOOK_TRANSVERSAL_ISOTROPIC",
        3: "BLATZ_KO",
        4: "MURNAGHAN",
        11: "COMPR_MOONEY",
        20: "NEO_HOOK",
        21: "ANISOTROPIC",
    },
    "common": {0: "USUAL"},
    "thermal": {0: "ISOTROPIC", 1: "ORTHOTROPIC", 2: "TRANSVERSAL_ISOTROPIC"},
    "geomechanic": {
        0: "BIOT_ISOTROPIC",
        1: "BIOT_ORTHOTROPIC",
        2: "BIOT_TRANSVERSAL_ISOTROPIC",
    },
    "plasticity": {0: "MISES", 1: "DRUCKER_PRAGER", 4: "DRUCKER_PRAGER_CREEP", 9: "MOHR_COULOMB"},
    "hardening": {0: "LINEAR", 1: "MULTILINEAR"},
    "creep": {0: "NORTON"},
    "preload": {0: "INITIAL"},
    "strength": {0: "ISOTROPIC"},
}

MATERIAL_PROPERTY_TYPES_REVERSE: Dict[str, Dict[str, int]] = {
    group: {name: code for code, name in mapping.items()} for group, mapping in MATERIAL_PROPERTY_TYPES.items()
}


# Constant (const_names) codes per group
CONST_NAME_MAP: Dict[str, Dict[int, str]] = {
    "elasticity": {
        0: "YOUNG_MODULE",
        1: "POISSON_RATIO",
        2: "SHEAR_MODULUS",
        3: "BULK_MODULUS",
        4: "MU",
        5: "ALPHA",
        6: "BETA",
        7: "LAME_MODULE",
        8: "C3",
        9: "C4",
        10: "C5",
        16: "E_T",
        17: "E_L",
        18: "PR_T",
        19: "PR_TL",
        20: "G_TL",
        21: "G12",
        22: "G23",
        23: "G13",
        24: "PRXY",
        25: "PRYZ",
        26: "PRXZ",
        27: "C1",
        28: "C2",
        29: "D",
        82: "C_1111",
        83: "C_1112",
        84: "C_1113",
        85: "C_1122",
        86: "C_1123",
        87: "C_1133",
        88: "C_1212",
        89: "C_1213",
        90: "C_1222",
        91: "C_1223",
        92: "C_1233",
        93: "C_1313",
        94: "C_1322",
        95: "C_1323",
        96: "C_1333",
        97: "C_2222",
        98: "C_2223",
        99: "C_2233",
        100: "C_2323",
        101: "C_2333",
        102: "C_3333",
    },
    "common": {0: "DENSITY", 1: "STRUCTURAL_DAMPING_RATIO", 2: "MASS_DAMPING_RATIO", 3: "STIFFNESS_DAMPING_RATIO"},
    "thermal": {
        0: "COEF_LIN_EXPANSION",
        1: "COEF_THERMAL_CONDUCTIVITY",
        5: "COEF_THERMAL_CONDUCTIVITY_XX",
        9: "COEF_THERMAL_CONDUCTIVITY_YY",
        13: "COEF_THERMAL_CONDUCTIVITY_ZZ",
        14: "COEF_LIN_EXPANSION_X",
        15: "COEF_LIN_EXPANSION_Y",
        16: "COEF_LIN_EXPANSION_Z",
        17: "COEF_THERMAL_CONDUCTIVITY_T",
        18: "COEF_THERMAL_CONDUCTIVITY_L",
        19: "COEF_LIN_EXPANSION_T",
        20: "COEF_LIN_EXPANSION_L",
    },
    "geomechanic": {
        1: "FLUID_VISCOSITY",
        2: "POROSITY",
        3: "FLUID_BULK_MODULUS",
        4: "SOLID_BULK_MODULUS",
        19: "FLUID_DENSITY",
        20: "BIOT_MODULUS",
        0: "PERMEABILITY",
        5: "BIOT_ALPHA",
        6: "PERMEABILITY_XX",
        7: "PERMEABILITY_XY",
        8: "PERMEABILITY_XZ",
        9: "PERMEABILITY_YX",
        10: "PERMEABILITY_YY",
        11: "PERMEABILITY_YZ",
        12: "PERMEABILITY_ZX",
        13: "PERMEABILITY_ZY",
        14: "PERMEABILITY_ZZ",
        21: "BIOT_ALPHA_X",
        22: "BIOT_ALPHA_Y",
        23: "BIOT_ALPHA_Z",
        15: "PERMEABILITY_T",
        16: "PERMEABILITY_TT",
        17: "PERMEABILITY_TL",
        18: "PERMEABILITY_L",
        24: "BIOT_ALPHA_T",
        25: "BIOT_ALPHA_L",
    },
    "plasticity": {
        0: "YIELD_STRENGTH",
        5: "YIELD_STRENGTH_COMPR",
        7: "COHESION",
        8: "INTERNAL_FRICTION_ANGLE",
        9: "DILATANCY_ANGLE",
        21: "DPC_A",
        22: "DPC_N",
        23: "DPC_M",
    },
    "hardening": {
        2: "E_TAN",
        10: "E_TAN_COMPR",
        1: "TENSILE_STRAIN",
        6: "TENSILE_STRAIN_COMPR",
        0: "COMPRESSIVE_STRAIN",
        7: "COMPRESSIVE_STRAIN_COMPR",
        8: "STRESS",
        3: "MULTILINEAR_STRESS",
        9: "HARDENING",
        4: "HARDENING_COMPR",
        5: "PLASTIC_STRAIN",
        11: "PLASTIC_STRAIN_COMPR",
        12: "TABULAR_MODE_ID",
    },
}

CONST_NAME_REVERSE: Dict[str, Dict[str, int]] = {
    group: {name: code for code, name in mapping.items()} for group, mapping in CONST_NAME_MAP.items()
}


