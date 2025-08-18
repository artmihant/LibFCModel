from typing import TypedDict
from numpy.typing import NDArray

from numpy import ndarray, dtype, int8, int32, int64, float64

from fc_dict import FCDict, FCSrcRequiredId
from fc_value import decode, encode, FCValue


# class FCBlockMaterialSteps(TypedDict):
#     ids: NDArray[int32]
#     steps: NDArray[int32]


class FCSrcBlock(TypedDict):
    id: int
    cs_id: int
    material_id: int
    property_id: int
    # steps: NotRequired[NDArray[int32]]
    # material: NotRequired[FCBlockMaterialSteps]


class FCBlock(FCSrcRequiredId[FCSrcBlock]):
    """
    Определяет 'блок' элементов.
    Блок - это группа элементов, которая ссылается на один и тот же материал
    и имеет общие свойства.
    """

    cs_id: int
    material_id: int
    property_id: int

    def __init__(self, src_data: FCSrcBlock):
        self.id = src_data['id']
        self.cs_id = src_data['cs_id']
        self.material_id = src_data['material_id']
        self.property_id = src_data['property_id']

    def dump(self) -> FCSrcBlock:

        return {
            "id": self.id,
            "material_id": self.material_id,
            "property_id": self.property_id,
            "cs_id": self.cs_id,
        }





class FCSrcCoordinateSystem(TypedDict):
    type: str
    name: str
    origin: str
    dir1: str
    dir2: str



class FCCoordinateSystem(FCSrcRequiredId[FCSrcCoordinateSystem]):
    type: str
    name: str
    origin: NDArray[float64]
    dir1: NDArray[float64]
    dir2: NDArray[float64]

    def __init__(
        self,
        id: int,
        type: str,
        name: str,
        origin: NDArray[float64],
        dir1: NDArray[float64],
        dir2: NDArray[float64]
    ):
        self.id = id
        self.type = type
        self.name = name
        self.origin = decode(origin, dtype(float64)),
        self.dir1 = decode(origin, dtype(float64)),
        self.dir2 = dir2


    def dump(self):
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "origin": decode(self.origin, dtype(float64)),
            "dir1": decode(self.dir1, dtype(float64)),
            "dir2": decode(self.dir2, dtype(float64))
        }


