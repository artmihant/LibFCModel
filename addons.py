
from fc_model import FCModel

def compress(self: FCModel):

    # TODO всюду где есть ссылки на узлы и элементы, осуществить грамотную переиндексацию
    # TODO добавить системы координат


    # 1. Убираем неиспользуемые узлы и переиндексируем используемые

    nodes_id_map = {index: i + 1
                    for i, index in enumerate(set(self.elems.nodes_list))}

    self.nodes.reindex(nodes_id_map)

    for elem in self.elems:
        elem['nodes'] = [nodes_id_map[nid] for nid in elem['nodes']]

    # 2. Убираем неиспользуемые блоки и переиндексируем используемые

    blocks_id_map = {index: i + 1
                        for i, index in enumerate(set([elem['block'] for elem in self.elems]))}

    self.blocks.reindex(blocks_id_map)

    for elem in self.elems:
        elem['block'] = blocks_id_map[elem['block']]


    # 3. Убираем неиспользуемые свойтсва и переиндексируем используемые

    property_id_map = {index: i + 1
                        for i, index in enumerate(set([block['property_id']
                                                        for block in self.blocks]))}

    self.property_tables.reindex(property_id_map)

    for block in self.blocks:
        block['property_id'] = property_id_map[block['property_id']]

    # 4. Переиндексируем используемые материалы

    material_id_map = self.materials.compress()

    for block in self.blocks:
        block['material_id'] = material_id_map[block['material_id']]


    # 5. Переиндексируем используемые граничные условия

    load_id_map = self.loads.compress()

    restraint_id_map = self.restraints.compress()


    # 6. Переиндексируем существующие элементы

    elems_id_map = self.elems.compress()

    for material in self.materials:
        for key in material['properties']:
            for property in material['properties'][key]:

                if isinstance(property['dependency'], list) and property['dependency']:
                    for dep in property['dependency']:
                        if isinstance(dep['data'], ndarray):
                            if dep['type'] == 10:
                                for i, n in enumerate(dep['data']):
                                    dep['data'][i] = elems_id_map[int(n)]
                            if dep['type'] == 11:
                                for i, n in enumerate(dep['data']):
                                    dep['data'][i] = nodes_id_map[int(n)]