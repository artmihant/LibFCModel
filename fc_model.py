import binascii
import json
from base64 import b64decode, b64encode
import os
from typing import Any, Callable, Generic, Literal, Optional, TypeVar, TypedDict, List, Dict, Union
import numpy as np
from numpy.typing import NDArray

from numpy import ndarray, dtype, int8, int32, int64, float64


class FCHeader(TypedDict):
    binary: bool
    description: str
    version: int
    types: Dict[str, int]


# class FCBlockMaterialSteps(TypedDict):
#     ids: NDArray[int32]
#     steps: NDArray[int32]


class FCBlock(TypedDict):
    """
    Определяет 'блок' элементов.
    Блок - это группа элементов, которая ссылается на один и тот же материал
    и имеет общие свойства.
    """
    id: int  # Уникальный идентификатор блока
    cs_id: int  # ID системы координат
    material_id: int  # ID материала, из которого состоит блок
    property_id: int  # ID таблицы свойств (если используется)
    # steps: NotRequired[NDArray[int32]]
    # material: NotRequired[FCBlockMaterialSteps]



class FCRestraintAxis(TypedDict):
    data: Union[NDArray[float64], str]
    dependency: Union[List[FCDependency], int, str]
    flag: Union[int, bool]


class FCRestraint(TypedDict):
    apply_to: Union[NDArray[int32], str]
    apply_dim: int    
    cs: Optional[int]
    name: str
    id: int
    axes: List[FCRestraintAxis]



class FCLoadAxis(TypedDict):
    data: Union[NDArray[float64], str]
    dependency: Union[List[FCDependency], int, str]


class FCLoad(TypedDict):
    apply_to: Union[NDArray[int32], str]
    apply_dim: int
    cs: Optional[int]
    name: str
    type: int
    id: int
    axes: List[FCLoadAxis]


class FCRestraintAxis(TypedDict):
    data: Union[NDArray[float64], str]
    dependency: Union[List[FCDependency], int, str]
    flag: Union[int, bool]


class FCRestraint(TypedDict):
    apply_to: Union[NDArray[int32], str]
    apply_dim: int    
    cs: Optional[int]
    name: str
    id: int
    axes: List[FCRestraintAxis]


class FCCoordinateSystem(TypedDict):
    id: int
    type: str
    name: str
    origin: NDArray[float64]
    dir1: NDArray[float64]
    dir2: NDArray[float64]


class FCConstraint(TypedDict):
    id: int
    name: str
    type: int
    master: NDArray[int32]
    slave: NDArray[int32]
    master_dim: int
    slave_dim: int
    properties: Dict[str, Any]


class FCInitialSetAxis(TypedDict):
    data: Union[NDArray[float64], str]
    dependency: Union[List[FCDependency], int, str]
    flag: Union[int, bool]


class FCInitialSet(TypedDict):
    apply_to: Union[NDArray[int32], str]
    apply_dim: int    
    cs: Optional[int]
    id: int
    axes: List[FCInitialSetAxis]
    type: int


class FCSet(TypedDict):
    apply_to: NDArray[int64]
    id: int
    name: str


class FCReceiver(TypedDict):
    apply_to: Union[NDArray[int32], str]
    dofs: List[int]
    id: int
    name: str
    type: int


class FCPropertyTable(TypedDict):
    id: int
    type: int
    properties: Dict[str, Any]
    additional_properties: Dict[str, Any]


class FCModel:
    """
    Основной класс для представления, загрузки и сохранения модели в формате Fidesys Case (.fc).

    Представляет собой контейнер для всех сущностей модели: узлов, элементов,
    материалов, нагрузок, закреплений и т.д.

    Атрибуты:
        header (FCHeader): Заголовок файла.
        coordinate_systems (FCDict[FCCoordinateSystem]): Коллекция систем координат.
        nodes (FCDict[FCNode]): Коллекция узлов сетки.
        elems (FCElems): Контейнер для коллекций элементов различных типов.
        blocks (FCDict[FCBlock]): Коллекция блоков, связывающих элементы с материалами.
        materials (FCDict[FCMaterial]): Коллекция материалов и их физических свойств.
        loads (List[FCLoad]): Список нагрузок, приложенных к модели.
        restraints (List[FCRestraint]): Список закреплений (ограничений).
        ... и другие коллекции сущностей.

    Пример использования:
    
    # Создание или загрузка модели
    model = FCModel() # Создать пустую модель
    # model = FCModel(filepath="path/to/model.fc") # Загрузить из файла

    # ... (добавление узлов, элементов, материалов)

    # Сохранение модели
    model.save("new_model.fc")
    """

    header: FCHeader = {
        "binary": True,
        "description": "Fidesys Case Format",
        "types": {"char": 1, "short_int": 2, "int": 4, "double": 8, },
        "version": 3
    }

    coordinate_systems: FCDict[FCCoordinateSystem]

    nodes: FCDict[FCNode]
    elems: FCElems

    blocks: FCDict[FCBlock]
    property_tables: FCDict[FCPropertyTable]
    materials: FCDict[FCMaterial]

    loads: List[FCLoad]
    restraints: List[FCRestraint]
    initial_sets: List[FCInitialSet]

    contact_constraints: List[FCConstraint]
    coupling_constraints: List[FCConstraint]
    periodic_constraints: List[FCConstraint]


    receivers: List[FCReceiver]

    nodesets: FCDict[FCSet]
    sidesets: FCDict[FCSet]

    settings: dict = {}


    def __init__(self, filepath=None):
        """
        Инициализирует объект FCModel.

        Если указан `filepath`, модель будет загружена из этого файла.
        В противном случае будет создана пустая модель с инициализированными коллекциями.

        Args:
            filepath (str, optional): Путь к файлу .fc для загрузки. Defaults to None.
        """
        
        # Инициализация всех коллекций как пустых
        self.coordinate_systems = FCDict()

        self.nodes = FCDict()
        self.elems = FCElems()

        self.blocks = FCDict()
        self.property_tables = FCDict()
        self.materials = FCDict()
        
        self.loads = []
        self.restraints = []
        self.initial_sets = []

        self.contact_constraints = []
        self.coupling_constraints = []
        self.periodic_constraints = []
        self.receivers = []

        self.nodesets = FCDict()
        self.sidesets = FCDict()

        if filepath:
            with open(filepath, "r") as f:
                input_data = json.load(f)

            self.src_data = input_data
            self._decode_header(input_data)
            self._decode_blocks(input_data)
            self._decode_coordinate_systems(input_data)
            self._decode_contact_constraints(input_data)
            self._decode_coupling_constraints(input_data)
            self._decode_periodic_constraints(input_data)
            self._decode_mesh(input_data)
            self._decode_settings(input_data)
            self._decode_materials(input_data)
            self._decode_restraints(input_data)
            self._decode_initial_sets(input_data)
            self._decode_loads(input_data)
            self._decode_receivers(input_data)
            self._decode_property_tables(input_data)
            self._decode_sets(input_data)


    def save(self, filepath):
        """
        Сохраняет текущее состояние модели в файл формата .fc.

        Собирает данные из всех коллекций (узлы, элементы, материалы и т.д.),
        кодирует их в нужный формат (JSON с base64 для бинарных данных)
        и записывает в указанный файл.

        Args:
            filepath (str): Путь к файлу, в который будет сохранена модель.
        """

        output_data: Dict = {}

        self._encode_blocks(output_data)
        self._encode_contact_constraints(output_data)
        self._encode_coordinate_systems(output_data)
        self._encode_coupling_constraints(output_data)
        self._encode_periodic_constraints(output_data)
        self._encode_header(output_data)
        self._encode_loads(output_data)
        self._encode_materials(output_data)
        self._encode_mesh(output_data)
        self._encode_receivers(output_data)
        self._encode_restraints(output_data)
        self._encode_initial_sets(output_data)
        self._encode_settings(output_data)
        self._encode_property_tables(output_data)
        self._encode_sets(output_data)

        with open(filepath, "w") as f:
            json.dump(output_data, f, indent=4)


    def _decode_header(self, input_data):
        self.header = input_data.get('header')


    def _encode_header(self, output_data):
        output_data['header'] = self.header


    def _decode_blocks(self, input_data):
        for block in input_data.get('blocks'):
            self.blocks[block['id']] = {
                "id": block['id'],
                "material_id": block['material_id'],
                "property_id": block['property_id'],
                "cs_id": block['cs_id']
            }


    def _encode_blocks(self, output_data):
        if self.blocks:
            output_data['blocks'] = [{
                "id": block['id'],
                "material_id": block['material_id'],
                "property_id": block['property_id'],
                "cs_id": block['cs_id']
            } for block in self.blocks]


    def _decode_coordinate_systems(self, input_data):

        for cs in input_data.get('coordinate_systems'):
            self.coordinate_systems[cs['id']] = {
                'dir1': decode(cs['dir1'], dtype(float64)),
                'dir2': decode(cs['dir2'], dtype(float64)),
                'origin': decode(cs['origin'], dtype(float64)),
                "id": cs['id'],
                "name": cs['name'],
                "type": cs['type']
            }

    def _encode_coordinate_systems(self, output_data):

        if self.coordinate_systems:
            output_data['coordinate_systems'] = [{
                'dir1': encode(cs['dir1']),
                'dir2': encode(cs['dir2']),
                'origin': encode(cs['origin']),
                "id": cs['id'],
                "name": cs['name'],
                "type": cs['type']
            } for cs in self.coordinate_systems]


    def _decode_contact_constraints(self, input_data):

        for cc_src in input_data.get('contact_constraints', []):
            master = decode(cc_src['master'], dtype(int32))
            slave = decode(cc_src['slave'], dtype(int32))

            self.contact_constraints.append({
                'id': cc_src['id'],
                'name': cc_src['name'],
                'type': cc_src['type'],
                'master': master,
                'master_dim': len(master)//cc_src['master_size'] if cc_src['master_size'] else 0,
                'slave': slave,
                'slave_dim': len(slave)//cc_src['slave_size'] if cc_src['slave_size'] else 0,
                'properties': {
                    key:cc_src[key] for key in cc_src
                    if key not in [
                        'id','name','type',
                        'master','master_size',
                        'slave','slave_size',
                    ]}
            })


    def _encode_contact_constraints(self, output_data):
        if self.contact_constraints:
            output_data['contact_constraints'] = []

            for cc in self.contact_constraints:
                cc_src = {
                    'id': cc['id'],
                    'type': cc['type'],
                    'name': cc['name'],
                    'master': encode(cc['master']),
                    'master_size': len(cc['master'])//cc['master_dim'] if cc['master_dim'] else 0,
                    'slave': encode(cc['slave']),
                    'slave_size': len(cc['slave'])//cc['slave_dim'] if cc['slave_dim'] else 0,
                }
                for key in cc['properties']:
                    cc_src[key] = cc['properties'][key]

                output_data['contact_constraints'].append(cc_src)


    def _decode_coupling_constraints(self, input_data):

        for cc_src in input_data.get('coupling_constraints', []):
            master = decode(cc_src['master'], dtype(int32))
            slave = decode(cc_src['slave'], dtype(int32))

            self.coupling_constraints.append({
                'id': cc_src['id'],
                'name': cc_src['name'],
                'type': cc_src['type'],
                'master': master,
                'master_dim': len(master)//cc_src['master_size'] if cc_src['master_size'] else 0,
                'slave': slave,
                'slave_dim': len(slave)//cc_src['slave_size'] if cc_src['slave_size'] else 0,
                'properties': {
                    key:cc_src[key] for key in cc_src
                    if key not in [
                        'id','name','type',
                        'master','master_size',
                        'slave','slave_size',
                    ]}
            })


    def _encode_coupling_constraints(self, output_data):
        if self.coupling_constraints:
            output_data['coupling_constraints'] = []

            for cc in self.coupling_constraints:
                cc_src = {
                    'id': cc['id'],
                    'type': cc['type'],
                    'name': cc['name'],
                    'master': encode(cc['master']),
                    'master_size': len(cc['master'])//cc['master_dim'] if cc['master_dim'] else 0,
                    'slave': encode(cc['slave']),
                    'slave_size': len(cc['slave'])//cc['slave_dim'] if cc['slave_dim'] else 0,
                }
                for key in cc['properties']:
                    cc_src[key] = cc['properties'][key]

                output_data['coupling_constraints'].append(cc_src)


    def _decode_periodic_constraints(self, input_data):

        for cc_src in input_data.get('periodic_constraints', []):
            master = decode(cc_src['master'], dtype(int32))
            slave = decode(cc_src['slave'], dtype(int32))

            self.periodic_constraints.append({
                'id': cc_src['id'],
                'name': cc_src['name'],
                'type': cc_src['type'],
                'master': master,
                'master_dim': len(master)//cc_src['master_size'] if cc_src['master_size'] else 0,
                'slave': slave,
                'slave_dim': len(slave)//cc_src['slave_size'] if cc_src['slave_size'] else 0,
                'properties': {
                    key:cc_src[key] for key in cc_src
                    if key not in [
                        'id','name','type',
                        'master','master_size',
                        'slave','slave_size',
                    ]}
            })


    def _encode_periodic_constraints(self, output_data):
        if self.periodic_constraints:
            output_data['periodic_constraints'] = []

            for cc in self.periodic_constraints:
                cc_src = {
                    'id': cc['id'],
                    'type': cc['type'],
                    'name': cc['name'],
                    'master': encode(cc['master']),
                    'master_size': len(cc['master'])//cc['master_dim'] if cc['master_dim'] else 0,
                    'slave': encode(cc['slave']),
                    'slave_size': len(cc['slave'])//cc['slave_dim'] if cc['slave_dim'] else 0,
                }
                for key in cc['properties']:
                    cc_src[key] = cc['properties'][key]

                output_data['periodic_constraints'].append(cc_src)


    def _decode_sets(self, src_data):

        if 'sets' in src_data:

            for nodeset_src in src_data['sets'].get('nodesets', []):
                self.nodesets[nodeset_src['id']] = {
                    'id': nodeset_src['id'],
                    'name': nodeset_src['name'],
                    'apply_to': decode(nodeset_src['apply_to'], dtype(int32))
                }

            for sideset_src in src_data['sets'].get('sidesets', []):
                self.sidesets[sideset_src['id']] = {
                    'id': sideset_src['id'],
                    'name': sideset_src['name'],
                    'apply_to': decode(sideset_src['apply_to'], dtype(int32)),
                }



    def _encode_sets(self,  src_data):

        if not (self.nodesets or self.sidesets):
            return

        src_data['sets'] = {}

        if self.nodesets:
            src_data['sets']['nodesets'] = [{
                'id': nodeset['id'],
                'name': nodeset['name'],
                'apply_to': encode(nodeset['apply_to']),
                'apply_to_size': len(nodeset['apply_to']),
            } for nodeset in self.nodesets]

        if self.sidesets:
            src_data['sets']['sidesets'] = [{
                'id': sideset['id'],
                'name': sideset['name'],
                'apply_to': encode(sideset['apply_to']),
                'apply_to_size': len(sideset['apply_to'])//2,
            } for sideset in self.sidesets]


    def _decode_mesh(self, src_data):

        node_ids = decode(src_data['mesh']['nids'])
        node_coords = decode(src_data['mesh']['nodes'], dtype('float64')).reshape(-1, 3)

        for i, nid in enumerate(node_ids):

            self.nodes[nid] = {
                'id': nid,
                'xyz':node_coords[i]
            }

        self.elems.decode(src_data['mesh'])


    def _encode_mesh(self, src_data):

        nodes_count = len(self.nodes)
        node_ids: NDArray = np.zeros(nodes_count, np.int32)
        node_xyzs: NDArray = np.zeros((nodes_count,3), np.float64)

        for i, node in enumerate(self.nodes):
            node_ids[i] = node['id']
            node_xyzs[i] = node['xyz']

        src_data['mesh'] = {
            "nodes_count": nodes_count,
            "nids": encode(node_ids),
            "nodes": encode(node_xyzs),
            **self.elems.encode()
        }


    def _decode_settings(self, src_data):
        self.settings = src_data.get('settings')


    def _encode_settings(self, src_data):
        settings = self.settings
        src_data['settings'] = settings


    def _decode_property_tables(self, src_data):
        for property_table in src_data.get('property_tables', []):
            self.property_tables[property_table['id']] = {
                'id': property_table['id'],
                'type': property_table['type'],
                'properties': property_table['properties'],
                'additional_properties': {key:property_table[key] for key in property_table if key not in ['id', 'type', 'properties']},
            }


    def _encode_property_tables(self, src_data):
        if self.property_tables:
            src_data['property_tables'] = [{
                'id': value['id'],
                'type': value['type'],
                'properties': value['properties'],
                **value['additional_properties']
            } for value in self.property_tables]


    def _decode_materials(self, src_data):

        for material_src in src_data.get('materials', []):

            properties: FCMaterialProperties = {}

            for property_name in material_src:
                properties_src = material_src[property_name]

                if not isinstance(properties_src, list):
                    continue

                named_properties:list  = []

                properties[property_name] = named_properties

                for property_src in properties_src:
                    for i, constants in enumerate(property_src["constants"]):

                        type_code = property_src["type"]
                        type_name = MATERIAL_PROPERTY_TYPES.get(property_name, {}).get(type_code, type_code)
                        const_code = property_src["const_names"][i]
                        const_name = CONST_NAME_MAP.get(property_name, {}).get(const_code, const_code)

                        property: FCMaterialProperty = {
                            "name": const_name,
                            "data": decode(constants, dtype(float64)),
                            "type": type_name,
                            "dependency": decode_dependency(
                                property_src["const_types"][i],
                                property_src["const_dep"][i]
                            )
                        }

                        named_properties.append(property)

            self.materials[material_src['id']] = {
                "id": material_src['id'],
                "name": material_src['name'],
                "properties": properties
            }


    def _encode_materials(self, src_data):

        if self.materials:

            src_data['materials'] = []

            for material in self.materials:

                material_src = {
                    "id": material['id'],
                    "name": material['name'],
                }

                for property_type in material["properties"]:

                    property_groups = {}

                    for material_property in material["properties"][property_type]:

                        if not material_property["type"] in property_groups:

                            material_property_group = {
                                "const_dep": [],
                                "const_dep_size": [],
                                "const_names": [],
                                "const_types": [],
                                "constants": [],
                                "type": material_property["type"]
                            }

                            property_groups[material_property["type"]] = material_property_group

                        const_types, const_dep = encode_dependency(material_property["dependency"])

                        property_groups[material_property["type"]]['const_dep'].append(const_dep)
                        property_groups[material_property["type"]]['const_dep_size'].append(len(material_property["data"]))
                        property_groups[material_property["type"]]['const_names'].append(material_property["name"])
                        property_groups[material_property["type"]]['const_types'].append(const_types)
                        property_groups[material_property["type"]]['constants'].append(fencode(material_property["data"]))
                    
                    remapped = []
                    for key in property_groups:
                        group = property_groups[key]
                        type_code = MATERIAL_PROPERTY_TYPES_REVERSE.get(property_type, {}).get(group['type'] if 'type' in group else key, key)
                        group_out = dict(group)
                        group_out['type'] = type_code
                        # map constant names back to codes
                        group_out['const_names'] = [
                            CONST_NAME_REVERSE.get(property_type, {}).get(n, n) for n in group_out['const_names']
                        ]
                        remapped.append(group_out)
                    material_src[property_type] = remapped

                src_data['materials'].append(material_src)


    def _decode_restraints(self, src_data):

        for restraint_src in src_data.get('restraints', []):

            axes: List[FCRestraintAxis] = []

            for i, dep_type in enumerate(restraint_src.get("dependency_type", [])):
                if 'dep_var_num' in restraint_src:
                    axes.append({
                        "data": fdecode(restraint_src['data'][i], dtype('float64')),
                        "dependency": decode_dependency(dep_type, restraint_src['dep_var_num'][i]),
                        "flag": restraint_src['flag'][i],
                    })

            apply_to = fdecode(restraint_src['apply_to'], dtype('int32'))

            if type(apply_to) == str:
                apply_dim = 0
            else:
                apply_to_size = restraint_src['apply_to_size']
                assert apply_to_size != 0 and len(apply_to)%apply_to_size == 0
                apply_dim = len(apply_to)//apply_to_size

            self.restraints.append({
                "id": restraint_src['id'],
                "name": restraint_src['name'],
                "cs": restraint_src['cs'] if 'cs' in restraint_src else 0,
                "apply_to": apply_to,
                "apply_dim": apply_dim,
                "axes": axes,
            })


    def _encode_restraints(self, src_data):

        if self.restraints:

            src_data['restraints'] = []

            for restraint in self.restraints:

                restraint_src_data:list = []
                restraint_src_flag:list = []
                restraint_src_dependency_type:list = []
                restraint_src_dep_var_num:list = []
                restraint_src_dep_var_size:list = []

                restraint_src = {
                    'id': restraint['id'],
                    'name': restraint['name'],
                    'apply_to': fencode(restraint['apply_to']),
                    'apply_to_size': len(restraint['apply_to'])//restraint['apply_dim'] if restraint['apply_dim'] else 0,
                    'data': restraint_src_data,
                    'flag': restraint_src_flag,
                    'dependency_type': restraint_src_dependency_type,
                    'dep_var_num': restraint_src_dep_var_num,
                    'dep_var_size': restraint_src_dep_var_size,
                }

                if restraint['cs']:
                    restraint_src['cs'] = restraint['cs']

                for axis in restraint['axes']:
                    if type(axis) == dict:
                        const_types, const_dep = encode_dependency(axis["dependency"])

                        restraint_src_data.append(fencode(axis['data']))
                        restraint_src_flag.append(axis['flag'])
                        restraint_src_dependency_type.append(const_types)
                        restraint_src_dep_var_num.append(const_dep)
                        restraint_src_dep_var_size.append(len(axis['data']) if const_dep else 0)

                    else:
                        restraint_src_data.append(fencode(axis['data']))
                        restraint_src_dependency_type.append(0)
                        restraint_src_dep_var_num.append("")
                        restraint_src_dep_var_size.append(0)
                        restraint_src_flag.append(15)

                src_data['restraints'].append(restraint_src)


    def _decode_initial_sets(self, src_data):

        for initial_set_src in src_data.get('initial_sets', []):

            axes: List[FCInitialSetAxis] = []

            for i, dep_type in enumerate(initial_set_src.get("dependency_type", [])):
                if 'dep_var_num' in initial_set_src:
                    axes.append({
                        "data": fdecode(initial_set_src['data'][i], dtype('float64')),
                        "dependency": decode_dependency(dep_type, initial_set_src['dep_var_num'][i]),
                        "flag": initial_set_src['flag'][i],
                    })

            apply_to = fdecode(initial_set_src['apply_to'], dtype('int32'))

            if type(apply_to) == str:
                apply_dim = 0
            else:
                apply_to_size = initial_set_src['apply_to_size']
                assert apply_to_size != 0 and len(apply_to)%apply_to_size == 0
                apply_dim = len(apply_to)//apply_to_size

            self.initial_sets.append({
                "id": initial_set_src['id'],
                "cs": initial_set_src['cs'] if 'cs' in initial_set_src else 0,
                "apply_to": apply_to,
                "apply_dim": apply_dim,
                "axes": axes,
                "type": initial_set_src['type'],
            })


    def _encode_initial_sets(self, src_data):

        if self.initial_sets:

            src_data['initial_sets'] = []

            for initial_set in self.initial_sets:

                initial_set_src_data:list = []
                initial_set_src_flag:list = []
                initial_set_src_dependency_type:list = []
                initial_set_src_dep_var_num:list = []
                initial_set_src_dep_var_size:list = []

                initial_set_src = {
                    'id': initial_set['id'],
                    "type": initial_set['type'],
                    'apply_to': fencode(initial_set['apply_to']),
                    'apply_to_size': len(initial_set['apply_to'])//initial_set['apply_dim'] if initial_set['apply_dim'] else 0,
                    'data': initial_set_src_data,
                    'flag': initial_set_src_flag,
                    'dependency_type': initial_set_src_dependency_type,
                    'dep_var_num': initial_set_src_dep_var_num,
                    'dep_var_size': initial_set_src_dep_var_size,
                }

                if initial_set['cs']:
                    initial_set_src['cs'] = initial_set['cs']

                for axis in initial_set['axes']:
                    if type(axis) == dict:
                        const_types, const_dep = encode_dependency(axis["dependency"])

                        initial_set_src_data.append(fencode(axis['data']))
                        initial_set_src_flag.append(axis['flag'])
                        initial_set_src_dependency_type.append(const_types)
                        initial_set_src_dep_var_num.append(const_dep)
                        initial_set_src_dep_var_size.append(len(axis['data']) if const_dep else 0)

                    else:
                        initial_set_src_data.append(fencode(axis['data']))
                        initial_set_src_dependency_type.append(0)
                        initial_set_src_dep_var_num.append("")
                        initial_set_src_dep_var_size.append(0)
                        initial_set_src_flag.append(15)

                src_data['initial_sets'].append(initial_set_src)


    def _decode_receivers(self, src_data):

        for r in src_data.get('receivers', []):
            receiver: FCReceiver = {
                'apply_to': fdecode(r['apply_to']),
                'dofs': r['dofs'],
                "id": r['id'],
                "name": r['name'],
                "type": r['type']
            }
            assert len(receiver['apply_to']) == r['apply_to_size']

            self.receivers.append(receiver)


    def _encode_receivers(self, src_data):

        if self.receivers:
            src_data['receivers'] = [{
                'apply_to': fencode(r['apply_to']),
                'apply_to_size': len(r['apply_to']),
                'dofs': r['dofs'],
                "id": r['id'],
                "name": r['name'],
                "type": r['type']
            } for r in self.receivers]



if __name__ == '__main__':
    name = "profile_model_local"
    datapath = "/home/antonov/Base/Coworks/CoworkMilenteva/"

    inputpath = os.path.join(datapath, f"{name}.fc")
    outputpath = os.path.join(datapath, f"{name}_new.fc")

    fc_model = FCModel(inputpath)

    fc_model.save(outputpath)
