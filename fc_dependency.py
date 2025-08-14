# Dependency (const_types) enumeration mapping
from typing import Dict, List, Tuple, TypedDict, Union

from numpy import dtype, float64
from numpy.typing import NDArray

from fc_value import FCValue


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


class FCDependencyColumn(TypedDict):
    type: str  # Форма задания зависимости - значение из DEPENDENCY_TYPES
    data: FCValue


class FCDependency:
    """
    Определяет зависимость свойства от внешних факторов (температура, координаты, etc.).
    """
    type: int # -1 - таблица, иное число - константа

    const: FCValue  # Данные для зависимости (e.g., массив ID узлов)
    table: List[FCDependencyColumn]

    def __init__(self, deps_types: Union[List[int], int], dep_data: Union[List[str], str]):
        self.decode(deps_types, dep_data)

    def decode(self, deps_types: Union[List[int], int], dep_data: Union[List[str], str]):
        if isinstance(deps_types, list) and isinstance(dep_data, list):
            self.type = -1
            self.const = FCValue("", dtype(float64))
            self.table = [{
                "type": DEPENDENCY_TYPES[deps_type],
                "data": FCValue(dep_data[j], dtype(float64))
            } for j, deps_type in enumerate(deps_types)]
        elif isinstance(deps_types, int) and isinstance(dep_data, str):
            self.type = deps_types
            self.const = FCValue(dep_data, dtype(float64))
            self.table = []
        else:
            raise ValueError("Invalid dependency data")

    def encode(self) -> Tuple[Union[List[int], int], Union[List[str], str]]:
        if self.type == -1:
            return [DEPENDENCY_TYPES_REVERSE[deps['type']] for deps in self.table], [deps['data'].dump() for deps in self.table]
        else:
            return self.type, self.const.dump()


