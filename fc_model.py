import json
import os
from typing import Any, TypedDict, List, Dict, Union
from numpy.typing import NDArray

from numpy import dtype, int32, int64, float64

from fc_dict import FCDict, FCSrcRequiredId
from fc_mesh import FCMesh
from fc_materials import FCMaterial
from fc_conditions import FCLoad, FCInitialSet, FCRestraint
from fc_value import FCValue, decode, encode


class FCHeader(TypedDict):
    binary: bool
    description: str
    version: int
    types: Dict[str, int]



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
    id: int
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
    id: int
    type: str
    name: str
    origin: str
    dir1: str
    dir2: str


class FCCoordinateSystem(FCSrcRequiredId[FCSrcCoordinateSystem]):
    id: int
    type: str
    name: str
    origin: NDArray[float64]
    dir1: NDArray[float64]
    dir2: NDArray[float64]


    def __init__(
        self,
        src_data: FCSrcCoordinateSystem
    ):
        self.id = src_data['id']
        self.type = src_data['type']
        self.name = src_data['name']
        self.origin = decode(src_data['origin'], dtype(float64))
        self.dir1 = decode(src_data['dir1'], dtype(float64))
        self.dir2 = decode(src_data['dir2'], dtype(float64))


    def dump(self) -> FCSrcCoordinateSystem:
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "origin": decode(self.origin, dtype(float64)),
            "dir1": decode(self.dir1, dtype(float64)),
            "dir2": decode(self.dir2, dtype(float64))
        }



class FCSrcConstraint(TypedDict):
    id: int
    name: str
    type: str
    master: str
    master_size: int
    slave: str
    slave_size: int


class FCConstraint(FCSrcRequiredId[FCSrcConstraint]):
    id: int
    name: str
    type: Union[int, str]
    master: FCValue
    slave: FCValue
    properties: Dict[str, Any]

    def __init__(
        self,
        src_data: FCSrcConstraint
    ):
        self.id = src_data['id']
        self.name = src_data['name']
        self.type = src_data['type']
        
        self.master = FCValue(src_data['master'], dtype(int32))
        self.master.resize(src_data['master_size'])
        self.slave = FCValue(src_data['slave'], dtype(int32))
        self.slave.resize(src_data['slave_size'])
        
        self.properties = {
                    key:src_data[key] for key in src_data
                    if key not in FCSrcConstraint.__annotations__.keys()}
        

    def dump(self) -> FCSrcConstraint:
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "master": encode(self.master),
            "slave": encode(self.slave),
            "master_dim": self.master_dim,
            "slave_dim": self.slave_dim,
            "properties": self.properties
        }


class FCSrcSet(TypedDict):
    id: int
    name: str
    apply_to: str
    apply_to_size: int


class FCSet(FCSrcRequiredId[FCSrcSet]):
    id: int
    apply: NDArray[int64]
    name: str

    def __init__(self, src_data: FCSrcSet):
        self.apply = decode(src_data['apply_to'], dtype(int64))
        self.id = src_data['id']
        self.name = src_data['name']

    def dump(self) -> FCSrcSet:
        return {
            "apply_to": encode(self.apply),
            "apply_to_size": len(self.apply),
            "id": self.id,
            "name": self.name
        }


class FCSrcReceiver(TypedDict):
    id: int
    name: str
    apply_to: str
    apply_to_size: int
    dofs: List[int]
    type: int


class FCReceiver(FCSrcRequiredId[FCSrcReceiver]):
    id: int
    apply: NDArray[int32]
    dofs: List[int]
    name: str
    type: int

    def __init__(self, src_data: FCSrcReceiver):
        self.apply = decode(src_data['apply_to'], dtype(int32))
        self.id = src_data['id']
        self.name = src_data['name']
        self.dofs = src_data['dofs']
        self.type = src_data['type']

    def dump(self) -> FCSrcReceiver:
        return {
            "apply_to": encode(self.apply),
            "apply_to_size": len(self.apply),
            "id": self.id,
            "name": self.name,
            "dofs": self.dofs,
            "type": self.type
        }


class FCSrcPropertyTable(TypedDict):
    id: int
    type: int
    properties: Dict[str, Any]
    additional_properties: Dict[str, Any]


class FCPropertyTable(FCSrcRequiredId[FCSrcPropertyTable]):
    id: int
    type: int
    properties: Dict[str, Any]
    additional_properties: Dict[str, Any]

    def __init__(self, src_data: FCSrcPropertyTable):
        self.id = src_data['id']
        self.type = src_data['type']
        self.properties = src_data['properties']
        self.additional_properties = src_data['additional_properties']

    def dump(self) -> FCSrcPropertyTable:
        return {
            "id": self.id,
            "type": self.type,
            "properties": self.properties,
            "additional_properties": self.additional_properties
        }



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

    mesh: FCMesh

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
        self.coordinate_systems = FCDict(FCCoordinateSystem)

        self.mesh = FCMesh()

        self.blocks = FCDict(FCBlock)
        self.property_tables = FCDict(FCPropertyTable)
        self.materials = FCDict(FCMaterial)
        
        self.loads = []
        self.restraints = []
        self.initial_sets = []

        self.contact_constraints = []
        self.coupling_constraints = []
        self.periodic_constraints = []
        self.receivers = []

        self.nodesets = FCDict(FCSet)
        self.sidesets = FCDict(FCSet)

        if filepath:
            with open(filepath, "r") as f:
                src_data = json.load(f)

            self.src_data = src_data
            self._decode_header(src_data)
            self._decode_blocks(src_data)
            self._decode_coordinate_systems(src_data)
            self._decode_contact_constraints(src_data)
            self._decode_coupling_constraints(src_data)
            self._decode_periodic_constraints(src_data)
            self._decode_mesh(src_data)
            self._decode_settings(src_data)
            self._decode_materials(src_data)
            self._decode_restraints(src_data)
            self._decode_initial_sets(src_data)
            self._decode_loads(src_data)
            self._decode_receivers(src_data)
            self._decode_property_tables(src_data)
            self._decode_sets(src_data)


    def save(self, filepath):
        with open(filepath, "w") as f:
            json.dump(self.dump(), f, indent=4)


    def dump(self):
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

        if self.coordinate_systems:
            output_data['coordinate_systems'] = self.coordinate_systems.encode()

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

        return output_data

    def _decode_header(self, input_data):
        self.header = input_data.get('header')

    def _encode_header(self, output_data):
        output_data['header'] = self.header

    def _decode_blocks(self, input_data):
        for src_block in input_data.get('blocks', []):
            self.blocks[src_block['id']] = FCBlock(src_block)

    def _encode_blocks(self, output_data):
        if self.blocks:
            output_data['blocks'] = [block.dump() for block in self.blocks]

    def _decode_coordinate_systems(self, input_data):

        for src_cs in input_data.get('coordinate_systems', []):
            coordinate_systems = FCCoordinateSystem(src_cs)
            self.coordinate_systems[coordinate_systems.id] = coordinate_systems

    def _encode_coordinate_systems(self, output_data):

        if self.coordinate_systems:
            output_data['coordinate_systems'] = [coordinate_system.dump() for coordinate_system in self.coordinate_systems]


    def _decode_contact_constraints(self, input_data):

        for cc_src in input_data.get('contact_constraints', []):
            master = decode(cc_src['master'], dtype(int32))
            slave = decode(cc_src['slave'], dtype(int32))

            self.contact_constraints.append(FCConstraint({
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
            }))


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
        self.mesh.decode(src_data['mesh'])

    def _encode_mesh(self, src_data):
        src_data['mesh'] = self.mesh.decode()


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
            material = FCMaterial(material_src)
            self.materials[material.id] = material


    def _encode_materials(self, src_data):

        if self.materials:
            src_data['materials'] = [material.dump() for material in self.materials]


    def _decode_loads(self, src_data):

        for restraint_src in src_data.get('restraints', []):

            restraint = FCRestraint(restraint_src)
            self.restraints[restraint.id] = restraint


    def _encode_loads(self, src_data):

        if self.restraints:
            src_data['restraints'] = [restraint.dump() for restraint in self.restraints]


    def _decode_restraints(self, src_data):

        for restraint_src in src_data.get('restraints', []):

            restraint = FCRestraint(restraint_src)
            self.restraints[restraint.id] = restraint


    def _encode_restraints(self, src_data):

        if self.restraints:
            src_data['restraints'] = [restraint.dump() for restraint in self.restraints]


    def _decode_initial_sets(self, src_data):

        for initial_set_src in src_data.get('initial_sets', []):
            initial_set = FCInitialSet(initial_set_src)
            self.initial_sets[initial_set.id] = initial_set


    def _encode_initial_sets(self, src_data):

        if self.initial_sets:
            src_data['initial_sets'] = [initial_set.dump() for initial_set in self.initial_sets]


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

    fc_model.dump(outputpath)
