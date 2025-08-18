from typing import List, Dict, Literal, TypedDict, Union
import numpy as np
from numpy.typing import NDArray

from fc_value import decode, encode
from fc_dict import FCDict, FCSrcRequiredId

FC_ELEMENT_TYPE_NAME = Literal[
    'NONE',
    'LUMPMASS3D',
    'LUMPMASS6D',
    'LUMPMASS2D',
    'POINT3D',
    'POINT2D',
    'POINT6D',
    'LUMPMASS2DR',
    'BEAM26',
    'BEAM36',
    'SPRING3D',
    'SPRING6D',
    'BEAM27',
    'BEAM37',
    'BAR2',
    'BAR3',
    'CABLE2',
    'CABLE3',
    'TRI3',
    'TRI6',
    'QUAD4',
    'QUAD8',
    'MITC3',
    'MITC6',
    'MITC4',
    'MITC8',
    'TETRA4',
    'TETRA10',
    'HEX8',
    'HEX20',
    'TETRA4S',
    'TETRA10S',
    'HEX8S',
    'HEX20S',
    'WEDGE6',
    'WEDGE15',
    'WEDGE6S',
    'WEDGE15S',
    'PYR5',
    'PYR13',
    'PYR5S',
    'PYR13S',
    'TRI3S',
    'TRI6S',
    'QUAD4S',
    'QUAD8S',
    'SPRING2D',
    'SHELL3S',
    'SHELL4S',
    'SHELL6S',
    'SHELL8S',
    'BEAM26S',
    'BEAM36S',
    'BEAM27S',
    'BEAM37S'
]


class FCElementType(TypedDict):
    name: FC_ELEMENT_TYPE_NAME 
    fc_id: int 
    dim: int 
    order: int 
    nodes: int 
    edges: List[List[int]]
    facets: List[List[int]]
    tetras: List[List[int]]


FC_ELEMENT_TYPES: List[FCElementType] = [
    {
        'name': 'NONE',
        'fc_id': 0,
        'dim': 0,
        'order': 0,
        'nodes': 0,
        'edges': [],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'LUMPMASS3D',
        'fc_id': 38,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'LUMPMASS6D',
        'fc_id': 40,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'LUMPMASS2D',
        'fc_id': 82,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'POINT3D',
        'fc_id': 99,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'POINT2D',
        'fc_id': 100,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'POINT6D',
        'fc_id': 101,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'LUMPMASS2DR',
        'fc_id': 105,
        'dim': 0,
        'order': 1,
        'nodes': 1,
        'edges': [],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'BEAM26',
        'fc_id': 36,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'BEAM36',
        'fc_id': 37,
        'dim': 1,
        'order': 2,
        'nodes': 3,
        'edges': [[0, 2, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'SPRING3D',
        'fc_id': 39,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'SPRING6D',
        'fc_id': 41,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'BEAM27',
        'fc_id': 89,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'BEAM37',
        'fc_id': 90,
        'dim': 1,
        'order': 2,
        'nodes': 3,
        'edges': [[0, 2, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'BAR2',
        'fc_id': 107,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'BAR3',
        'fc_id': 108,
        'dim': 1,
        'order': 2,
        'nodes': 3,
        'edges': [[0, 2, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'CABLE2',
        'fc_id': 109,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'CABLE3',
        'fc_id': 110,
        'dim': 1,
        'order': 2,
        'nodes': 3,
        'edges': [[0, 2, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'TRI3',
        'fc_id': 10,
        'dim': 2,
        'order': 1,
        'nodes': 3,
        'edges': [[0, 1, 2, 0]],
        'facets': [[0, 1, 2]],
        'tetras': [],
    },
    {
        'name': 'TRI6',
        'fc_id': 11,
        'dim': 2,
        'order': 2,
        'nodes': 6,
        'edges': [[0, 3, 1, 4, 2, 5, 0]],
        'facets': [[0, 3, 1, 4, 2, 5]],
        'tetras': [],
    },
    {
        'name': 'QUAD4',
        'fc_id': 12,
        'dim': 2,
        'order': 1,
        'nodes': 4,
        'edges': [[0, 1, 2, 3, 0]],
        'facets': [[0, 1, 2, 3]],
        'tetras': [],
    },
    {
        'name': 'QUAD8',
        'fc_id': 13,
        'dim': 2,
        'order': 2,
        'nodes': 8,
        'edges': [[0, 4, 1, 5, 2, 6, 3, 7, 0]],
        'facets': [[0, 4, 1, 5, 2, 6, 3, 7]],
        'tetras': [],
    },
    {
        'name': 'MITC3',
        'fc_id': 29,
        'dim': 2,
        'order': 1,
        'nodes': 3,
        'edges': [[0, 1, 2, 0]],
        'facets': [[0, 1, 2]],
        'tetras': [],
    },
    {
        'name': 'MITC6',
        'fc_id': 30,
        'dim': 2,
        'order': 2,
        'nodes': 6,
        'edges': [[0, 3, 1, 4, 2, 5, 0]],
        'facets': [[0, 3, 1, 4, 2, 5]],
        'tetras': [],
    },
    {
        'name': 'MITC4',
        'fc_id': 31,
        'dim': 2,
        'order': 1,
        'nodes': 4,
        'edges': [[0, 1, 2, 3, 0]],
        'facets': [[0, 1, 2, 3]],
        'tetras': [],
    },
    {
        'name': 'MITC8',
        'fc_id': 32,
        'dim': 2,
        'order': 2,
        'nodes': 8,
        'edges': [[0, 4, 1, 5, 2, 6, 3, 7, 0]],
        'facets': [[0, 4, 1, 5, 2, 6, 3, 7]],
        'tetras': [],
    },
    {
        'name': 'TETRA4',
        'fc_id': 1,
        'dim': 3,
        'order': 1,
        'nodes': 4,
        'edges': [[0, 1, 2, 0], [0, 3], [1, 3], [2, 3]],
        'facets': [[0, 2, 1], [0, 1, 3], [1, 2, 3], [2, 0, 3]],
        'tetras': [[0, 1, 2, 3]],
    },
    {
        'name': 'TETRA10',
        'fc_id': 2,
        'dim': 3,
        'order': 2,
        'nodes': 10,
        'edges': [[0, 4, 1, 5, 2, 6, 0], [0, 7, 3], [1, 8, 3], [2, 9, 3]],
        'facets': [[0, 6, 2, 5, 1, 4], [0, 4, 1, 8, 3, 5], [1, 5, 2, 9, 3, 8], [2, 6, 0, 5, 3, 9]],
        'tetras': [],
    },
    {
        'name': 'HEX8',
        'fc_id': 3,
        'dim': 3,
        'order': 1,
        'nodes': 8,
        'edges': [[0, 1, 2, 3, 0], [4, 5, 6, 7, 4], [0, 4], [1, 5], [2, 6], [3, 7]],
        'facets': [[3, 2, 1, 0], [4, 5, 6, 7], [1, 2, 6, 5], [0, 1, 5, 4], [0, 4, 7, 3], [2, 3, 7, 6]],
        'tetras': [[1, 3, 4, 6], [3, 1, 4, 0], [1, 3, 6, 2], [4, 1, 6, 5], [3, 4, 6, 7]],
    },
    {
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
    },
    {
        'name': 'TETRA4S',
        'fc_id': 15,
        'dim': 3,
        'order': 1,
        'nodes': 4,
        'edges': [[0, 1, 2, 0], [0, 3], [1, 3], [2, 3]],
        'facets': [[0, 2, 1], [0, 1, 3], [1, 2, 3], [2, 0, 3]],
        'tetras': [[0, 1, 2, 3]],
    },
    {
        'name': 'TETRA10S',
        'fc_id': 16,
        'dim': 3,
        'order': 2,
        'nodes': 10,
        'edges': [[0, 4, 1, 5, 2, 6, 0], [0, 7, 3], [1, 8, 3], [2, 9, 3]],
        'facets': [[0, 6, 2, 5, 1, 4], [0, 4, 1, 8, 3, 5], [1, 5, 2, 9, 3, 8], [2, 6, 0, 5, 3, 9]],
        'tetras': [],
    },
    {
        'name': 'HEX8S',
        'fc_id': 17,
        'dim': 3,
        'order': 1,
        'nodes': 8,
        'edges': [[0, 1, 2, 3, 0], [4, 5, 6, 7, 4], [0, 4], [1, 5], [2, 6], [3, 7]],
        'facets': [[3, 2, 1, 0], [4, 5, 6, 7], [1, 2, 6, 5], [0, 1, 5, 4], [0, 4, 7, 3], [2, 3, 7, 6]],
        'tetras': [[1, 3, 4, 6], [3, 1, 4, 0], [1, 3, 6, 2], [4, 1, 6, 5], [3, 4, 6, 7]],
    },
    {
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
    },
    {
        'name': 'WEDGE6',
        'fc_id': 6,
        'dim': 3,
        'order': 1,
        'nodes': 5,
        'edges': [[0, 1, 2, 0], [3, 4, 5, 3], [0, 3], [1, 4], [2, 5]],
        'facets': [[0, 1, 2], [5, 4, 3], [0, 2, 5, 3], [0, 3, 4, 1], [1, 4, 5, 2]],
        'tetras': [[0, 5, 4, 3], [0, 4, 2, 1], [0, 2, 4, 5]],
    },
    {
        'name': 'WEDGE15',
        'fc_id': 7,
        'dim': 3,
        'order': 2,
        'nodes': 15,
        'edges': [[0, 5, 1, 6, 2, 7, 3, 8, 0], [0, 9, 4], [1, 10, 4], [2, 11, 4], [3, 12, 4]],
        'facets': [[3, 7, 2, 6, 1, 5, 0, 8],
                   [0, 5, 1, 10, 4, 9], [1, 6, 2, 11, 4, 10], [2, 7, 3, 12, 4, 11], [3, 8, 0, 9, 4, 12]],
        'tetras': [],
    },
    {
        'name': 'WEDGE6S',
        'fc_id': 20,
        'dim': 3,
        'order': 1,
        'nodes': 5,
        'edges': [[0, 1, 2, 0], [3, 4, 5, 3], [0, 3], [1, 4], [2, 5]],
        'facets': [[0, 1, 2], [5, 4, 3], [0, 2, 5, 3], [0, 3, 4, 1], [1, 4, 5, 2]],
        'tetras': [[0, 5, 4, 3], [0, 4, 2, 1], [0, 2, 4, 5]],
    },
    {
        'name': 'WEDGE15S',
        'fc_id': 21,
        'dim': 3,
        'order': 2,
        'nodes': 15,
        'edges': [[0, 5, 1, 6, 2, 7, 3, 8, 0], [0, 9, 4], [1, 10, 4], [2, 11, 4], [3, 12, 4]],
        'facets': [[3, 7, 2, 6, 1, 5, 0, 8],
                   [0, 5, 1, 10, 4, 9], [1, 6, 2, 11, 4, 10], [2, 7, 3, 12, 4, 11], [3, 8, 0, 9, 4, 12]],
        'tetras': [],
    },
    {
        'name': 'PYR5',
        'fc_id': 8,
        'dim': 3,
        'order': 1,
        'nodes': 5,
        'edges': [[0, 1, 2, 3, 0], [0, 4], [1, 4], [2, 4], [3, 4]],
        'facets': [[3, 2, 1, 0], [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4]],
        'tetras': [[1, 3, 4, 0], [3, 4, 1, 2]],
    },
    {
        'name': 'PYR13',
        'fc_id': 9,
        'dim': 3,
        'order': 2,
        'nodes': 13,
        'edges': [[0, 5, 1, 6, 2, 7, 3, 8, 0], [0, 9, 4], [1, 10, 4], [2, 11, 4], [3, 12, 4]],
        'facets': [[3, 7, 2, 6, 1, 5, 0, 8],
                   [0, 5, 1, 10, 4, 9], [1, 6, 2, 11, 4, 10], [2, 7, 3, 12, 4, 11], [3, 8, 0, 9, 4, 12]],
        'tetras': [],
    },
    {
        'name': 'PYR5S',
        'fc_id': 22,
        'dim': 3,
        'order': 1,
        'nodes': 5,
        'edges': [[0, 1, 2, 3, 0], [0, 4], [1, 4], [2, 4], [3, 4]],
        'facets': [[3, 2, 1, 0], [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4]],
        'tetras': [[1, 3, 4, 0], [3, 4, 1, 2]],
    },
    {
        'name': 'PYR13S',
        'fc_id': 23,
        'dim': 3,
        'order': 2,
        'nodes': 13,
        'edges': [[0, 5, 1, 6, 2, 7, 3, 8, 0], [0, 9, 4], [1, 10, 4], [2, 11, 4], [3, 12, 4]],
        'facets': [[3, 7, 2, 6, 1, 5, 0, 8],
                   [0, 5, 1, 10, 4, 9], [1, 6, 2, 11, 4, 10], [2, 7, 3, 12, 4, 11], [3, 8, 0, 9, 4, 12]],
        'tetras': [],
    },
    {
        'name': 'TRI3S',
        'fc_id': 24,
        'dim': 2,
        'order': 1,
        'nodes': 3,
        'edges': [[0, 1, 2, 0]],
        'facets': [[0, 1, 2]],
        'tetras': [],
    },
    {
        'name': 'TRI6S',
        'fc_id': 25,
        'dim': 2,
        'order': 2,
        'nodes': 6,
        'edges': [[0, 3, 1, 4, 2, 5, 0]],
        'facets': [[0, 3, 1, 4, 2, 5]],
        'tetras': [],
    },
    {
        'name': 'QUAD4S',
        'fc_id': 26,
        'dim': 2,
        'order': 1,
        'nodes': 4,
        'edges': [[0, 1, 2, 3, 0]],
        'facets': [[0, 1, 2, 3]],
        'tetras': [],
    },
    {
        'name': 'QUAD8S',
        'fc_id': 27,
        'dim': 2,
        'order': 2,
        'nodes': 8,
        'edges': [[0, 4, 1, 5, 2, 6, 3, 7, 0]],
        'facets': [[0, 4, 1, 5, 2, 6, 3, 7]],
        'tetras': [],
    },
    {
        'name': 'SPRING2D',
        'fc_id': 83,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'SHELL3S',
        'fc_id': 84,
        'dim': 2,
        'order': 1,
        'nodes': 3,
        'edges': [[0, 1, 2, 0]],
        'facets': [[0, 1, 2]],
        'tetras': [],
    },
    {
        'name': 'SHELL4S',
        'fc_id': 85,
        'dim': 2,
        'order': 1,
        'nodes': 4,
        'edges': [[0, 1, 2, 3, 0]],
        'facets': [[0, 1, 2, 3]],
        'tetras': [],
    },
    {
        'name': 'SHELL6S',
        'fc_id': 86,
        'dim': 2,
        'order': 2,
        'nodes': 6,
        'edges': [[0, 3, 1, 4, 2, 5, 0]],
        'facets': [[0, 3, 1, 4, 2, 5]],
        'tetras': [],
    },
    {
        'name': 'SHELL8S',
        'fc_id': 87,
        'dim': 2,
        'order': 2,
        'nodes': 8,
        'edges': [[0, 4, 1, 5, 2, 6, 3, 7, 0]],
        'facets': [[0, 4, 1, 5, 2, 6, 3, 7]],
        'tetras': [],
    },
    {
        'name': 'BEAM26S',
        'fc_id': 95,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'BEAM36S',
        'fc_id': 96,
        'dim': 1,
        'order': 2,
        'nodes': 3,
        'edges': [[0, 2, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'BEAM27S',
        'fc_id': 97,
        'dim': 1,
        'order': 1,
        'nodes': 2,
        'edges': [[0, 1]],
        'facets': [],
        'tetras': [],
    },
    {
        'name': 'BEAM37S',
        'fc_id': 98,
        'dim': 1,
        'order': 2,
        'nodes': 3,
        'edges': [[0, 2, 1]],
        'facets': [],
        'tetras': [],
    }
]

FC_ELEMENT_TYPES_KEYID: Dict[int, FCElementType] = {
    element_type['fc_id']:element_type for element_type in FC_ELEMENT_TYPES
}

FC_ELEMENT_TYPES_KEYNAME: Dict[FC_ELEMENT_TYPE_NAME, FCElementType] = {
    element_type['name']:element_type for element_type in FC_ELEMENT_TYPES
}


class FCElem(FCSrcRequiredId):
    """
    Определяет один конечный элемент в сетке.
    """
    id: int
    block: int
    parent_id: int
    type: FCElementType
    nodes: List[int]
    order: int

    def __init__(self, id: int, block: int, parent_id: int, type: FCElementType, nodes: List[int], order: int):
        """
        Инициализатор для FCElem.

        :param id: Уникальный идентификатор элемента
        :param block: ID блока, к которому принадлежит элемент
        :param parent_id: ID родительской топологической сущности
        :param type: Словарь, описывающий тип элемента (например, HEX8, TETRA4)
        :param nodes: Список ID узлов, образующих элемент
        :param order: Порядок элемента (1 - линейный, 2 - квадратичный)
        """
        self.id = id
        self.block = block
        self.parent_id = parent_id
        self.type = type
        self.nodes = nodes
        self.order = order


class FCMesh:
    """
    Контейнер для хранения всех элементов модели, сгруппированных по типам.

    Внутри `FCElems` элементы хранятся не в одном списке, а в словаре `data`,
    где ключами являются строковые имена типов элементов (e.g., 'HEX8', 'TETRA4'),
    а значениями - объекты `FCDict`, содержащие элементы соответствующего типа.

    Этот класс также управляет общей кодировкой и декодировкой всего набора
    элементов в/из формата .fc.
    """

    nodes_ids: NDArray[np.int32] # Сделан не через FCDict с целью оптимизации.
    nodes_xyz: NDArray[np.float64]

    data: Dict[FC_ELEMENT_TYPE_NAME, FCDict[FCElem]]

    def __init__(self):

        # INSERT_YOUR_CODE
        self.nodes_ids = np.array([], dtype=np.int32)
        self.nodes_xyz = np.array([], dtype=np.float64)

        self.data = {}

    def decode(self, src_mesh=None):

        self.nodes_ids = decode(src_mesh['nids'], np.dtype('int32'))
        self.nodes_xyz = decode(src_mesh['nodes'], np.dtype('float64')).reshape(-1, 3)

        elem_blocks = decode(src_mesh.get('elem_blocks', ''))
        elem_orders = decode(src_mesh.get('elem_orders', ''))
        elem_parent_ids = decode(src_mesh.get('elem_parent_ids', ''))
        elem_types = decode(src_mesh.get('elem_types', ''), np.dtype('int8'))
        elem_ids = decode(src_mesh.get('elemids',''))
        elem_nodes = decode(src_mesh.get('elems', ''))

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

