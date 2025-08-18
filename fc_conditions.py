from typing import Dict, Union
from typing import List, Optional, TypedDict
from numpy import dtype

from fc_dependency import FCDependency
from fc_value import FCValue


LOADS_TYPES_KEYS = {
    # Нагрузки на грань
    1: 'FaceDeadStress',                    # Давление на грань
    3: 'FaceTrackingStress',                # Следящее давление на грань
    11: 'FaceHeatFlux',                     # Тепловой поток на грани
    13: 'FaceConvection',                   # Конвекция на грани
    15: 'FaceRadiation',                    # Излучение на грани
    19: 'FaceAbsorbingBC',                  # Поглощающее ГУ на грани
    21: 'ShellHeatfluxTopBottom',           # Тепловой поток верх и низ
    22: 'ShellHeatfluxTop',                 # Тепловой поток верх
    23: 'ShellHeatfluxBottom',              # Тепловой поток низ
    24: 'ShellConvectionTopBottom',         # Конвекция верх и низ
    25: 'ShellConvectionTop',               # Конвекция верх
    26: 'ShellConvectionBottom',            # Конвекция низ
    35: 'FaceDistributedForce',             # Распределенная сила на грань
    36: 'FaceEquivalentForce',              # Равнодействующая сила на грань
    37: 'FaceTrackingDistributedForce',     # Следящая распределенная сила на грань
    38: 'FaceTrackingEquivalentForce',      # Следящая равнодействующая сила на грань
    39: 'FaceFluidFlux',                    # Поток жидкости через грань

    # Нагрузки на ребро
    2: 'SegmentDeadStress',                 # Давление на ребро
    4: 'SegmentTrackingStress',             # Следящее давление на ребро
    12: 'SegmentHeatFlux',                  # Тепловой поток на ребре
    14: 'SegmentConvection',                # Конвективный теплообмен на ребре
    16: 'SegmentRadiation',                 # Излучение на ребре
    20: 'SegmentAbsorbingBC',               # Поглощающее ГУ на ребре
    31: 'SegmentDistributedForce',          # Распределенная сила на ребро
    32: 'SegmentEquivalentForce',           # Равнодействующая сила на ребро
    33: 'SegmentTrackingDistributedForce',  # Следящая распределенная сила на ребро
    34: 'SegmentTrackingEquivalentForce',   # Следящая равнодействующая сила на ребро
    40: 'SegmentFluidFlux',                 # Поток жидкости через ребро

    # Нагрузки на узел
    5: 'NodeForce',                         # Узловая сила
    18: 'HeatSource',                       # Узловой источник тепла
    28: 'NodeHeatFlux',                     # Узловой тепловой поток
    29: 'NodeConvection',                   # Узловая конвекция
    30: 'NodeRadiation',                    # Узловое излучение
    41: 'NodeFluidFlux',                    # Поток жидкости через узел
    43: 'FluidSource',                      # Узловой источник жидкости

    # Нагрузки на элемент
    17: 'VolumeHeatSource',                 # Объемный источник тепла
    42: 'VolumeFluidSource',                # Объемный источник жидкости
    44: 'VolumeGravityMassForce',           # Гравитация
}

LOADS_TYPES_CODES: Dict[str, int] = {code: key for key, code in LOADS_TYPES_KEYS.items()}


RESTRAINT_FLAGS_KEYS = {
    0: 'EmptyRestraint',            # Отсутствует закрепление. Применяется в массивах вместе с остальными вариантами.
    1: 'Displacement',              # ГУ по перемещениям и поворотам для узлов. Длина массива равна 6.
    2: 'Velocity',                  # ГУ по скоростям и скоростям поворотов для узлов. Длина массива равна 6
    3: 'Temperature',               # ГУ по температуре для узлов. Длина массива равна 1.
    4: 'TemperatureTop',            # Температура на верхней поверхности. Для узлов оболочечных элементов.
    5: 'TemperatureBottom',         # Температура на нижней поверхности. Для узлов оболочечных элементов.
    6: 'TemperatureMiddle',         # Температура для узлов на срединной поверхности оболочечного элемента.
    7: 'TemperatureGradient',       # Градиент температуры для узлов оболочечного элемента.
    9: 'Acceleration',              # ГУ по ускорениям и угловым ускорениям для узлов. Длина массива равна 6.
    10: 'PorePressure',             # ГУ по поровому давлению для узлов. Длина массива равна 1.
    12: 'DirectionDisplacement',    # ГУ по направлению по перемещениям. Применяется к граням элементов. Длина массива равна 1
    13: 'DirectionVelocity',        # ГУ по направлению по скоростям. Применяется к граням элементов. Длина массива равна 1
    14: 'DirectionAcceleration',    # ГУ по направлению по ускорениям. Применяется к граням элементов. Длина массива равна 1
    15: 'VolumeAngularVelocity',    # ГУ по угловым скоростям. Применяется к элементам. Длина массива равна 3.
}



class FCConditionAxis:
    data: FCValue
    dependency: FCDependency
    flag: Union[str, None]
    def __init__(self, data: FCValue, dependency: FCDependency, flag: Union[str, None] = None):
        """
        Инициализация оси применения гранусловия.

        :param data: Значение нагрузки (FCValue)
        :param dependency: Зависимость (FCDependency)
        """
        self.data = data
        self.dependency = dependency
        self.flag = flag


class SrcFCLoadStrict(TypedDict):
    apply_to: str
    apply_to_size: int
    data: list
    dep_var_num: list
    dep_var_size: list
    dependency_type: list
    id: int
    name: str
    type: int

class SrcFCLoad(SrcFCLoadStrict, total=False):
    cs: int


class FCLoad:
    id: int
    name: str
    type: str

    apply: FCValue
    cs_id: int
    axes: List[FCConditionAxis]

    def __init__(self, src_load:SrcFCLoad):

        self.id = src_load['id']
        self.name = src_load['name']
        self.cs_id = src_load.get('cs', 0)

        self.apply = FCValue(src_load['apply_to'], dtype('int32'))
        self.apply.resize(src_load.get('apply_to_size', 0))

        self.type = LOADS_TYPES_KEYS[src_load['type']]

        axes: List[FCConditionAxis] = []

        for i, dep_type in enumerate(src_load.get("dependency_type", [])):
            axes.append(FCConditionAxis(
                data = FCValue(src_load['data'][i], dtype('float64')),
                dependency = FCDependency(dep_type, src_load.get('dep_var_num', {i:""})[i]),
            ))

    def dump(self) -> SrcFCLoad:

        load_src_data: list = []
        load_src_dependency_type: list = []
        load_src_dep_var_num: list = []
        load_src_dep_var_size: list = []

        load_src: SrcFCLoad = {
            'id': self.id,
            'name': self.name,
            'type': LOADS_TYPES_CODES[self.type],
            'apply_to': self.apply.dump(),
            'apply_to_size': len(self.apply),
            'data': load_src_data,
            'dependency_type': load_src_dependency_type,
            'dep_var_num': load_src_dep_var_num,
            'dep_var_size': load_src_dep_var_size,
        }

        if self.cs_id:
            load_src['cs'] = self.cs_id

        for axis in self.axes:
            const_types, const_dep = axis.dependency.dump()

            load_src_data.append(axis.data.dump())
            load_src_dependency_type.append(const_types)
            load_src_dep_var_num.append(const_dep)
            load_src_dep_var_size.append(len(axis.dependency))

        return load_src


class FCRestraint:
    id: int
    name: str

    apply: FCValue
    cs_id: int
    axes: List[FCConditionAxis]

    def __init__(self, src_load:SrcFCLoad):

        self.id = src_load['id']
        self.name = src_load['name']
        self.cs_id = src_load.get('cs', 0)

        self.apply = FCValue(src_load['apply_to'], dtype('int32'))
        self.apply.resize(src_load.get('apply_to_size', 0))

        self.type = LOADS_TYPES_KEYS[src_load['type']]

        axes: List[FCConditionAxis] = []

        for i, dep_type in enumerate(src_load.get("dependency_type", [])):
            axes.append(FCConditionAxis(
                data = FCValue(src_load['data'][i], dtype('float64')),
                dependency = FCDependency(dep_type, src_load.get('dep_var_num', {i:""})[i]),
            ))
            
    # TODO добавить флаги
    def dump(self) -> SrcFCLoad:

        load_src_data: list = []
        load_src_dependency_type: list = []
        load_src_dep_var_num: list = []
        load_src_dep_var_size: list = []

        load_src: SrcFCLoad = {
            'id': self.id,
            'name': self.name,
            'type': LOADS_TYPES_CODES[self.type],
            'apply_to': self.apply.dump(),
            'apply_to_size': len(self.apply),
            'data': load_src_data,
            'dependency_type': load_src_dependency_type,
            'dep_var_num': load_src_dep_var_num,
            'dep_var_size': load_src_dep_var_size,
        }

        if self.cs_id:
            load_src['cs'] = self.cs_id

        for axis in self.axes:
            const_types, const_dep = axis.dependency.dump()

            load_src_data.append(axis.data.dump())
            load_src_dependency_type.append(const_types)
            load_src_dep_var_num.append(const_dep)
            load_src_dep_var_size.append(len(axis.dependency))

        return load_src