
from abc import ABC, abstractmethod
from typing import Any, Generic, Type, TypeVar, TypedDict, Dict


S = TypeVar("S")


class FCSrcRequiredId(Generic[S], ABC):
    id: int
    
    @abstractmethod
    def __init__(self, src_data: S):
        pass

    @abstractmethod
    def dump(self) -> S:
        pass


T = TypeVar("T", bound=FCSrcRequiredId)


class FCDict(Generic[T]):

    """
    Специализированный класс-контейнер, похожий на словарь, для хранения
    объектов, имеющих обязательное поле 'id'.

    Обеспечивает автоматическое присвоение уникальных ID при добавлении
    новых элементов (если 'id' не указан или равен 0) и отслеживает
    максимальный использованный ID.

    Используется для хранения узлов, блоков, материалов и т.д.
    """
    EntityType: Type[T]

    data: Dict[int, T]

    max_id:int

    def __init__(self, EntityType: Type[T]):
        self.EntityType = EntityType
        self.max_id = 0
        self.data = {}

    def __getitem__(self, key:int):
        return self.data[key]

    def __setitem__(self, key:int, item: T):
        item.id = key
        if self.max_id < item.id:
            self.max_id = item.id
        self.data[item.id] = item

    def __contains__(self, key):
        return key in self.data

    def __iter__(self):
        for item in self.data:
            yield self.data[item]

    def __repr__(self) -> str:
        return f'<FCDict: {len(self.data)}>'

    def add(self, item: T):
        if item.id in self or item.id < 1:
            self[self.max_id+1] = item
        else:
            self[item.id] = item
        return item.id

    def __len__(self):
        return len(self.data)

    def keys(self):
        return self.data.keys()

    def reindex(self, index_map: Dict[int, int]):
        new_data = {}
        for key in index_map:
            if item := self.data[key]:
                item.id = index_map[key]
                new_data[index_map[key]] = item

        if len(new_data) > 1:
            self.max_id = max(*new_data.keys())
        elif len(new_data) == 1:
            self.max_id = new_data[0].id
        else:
            self.max_id = 0

        self.data = new_data

    def compress(self):
        index_map = {index: i + 1 for i, index in enumerate(self.keys())}
        self.reindex(index_map)
        return index_map

    def decode(self, input_data):
        for src_cs in input_data:
            entity = self.EntityType(src_cs)
            self[entity.id] = entity

    def encode(self):
        return [entity.dump() for entity in self]