from base64 import b64decode, b64encode
import binascii
from re import L
from typing import Literal, Union

import numpy as np
from numpy.typing import NDArray


def isBase64(sb):
    """Проверяет, является ли строка base64."""
    if sb == 'all':
        return False
    try:
        if isinstance(sb, str):
            sb_bytes = bytes(sb, 'ascii')
        elif isinstance(sb, bytes):
            sb_bytes = sb
        else:
            raise ValueError("Argument must be string or bytes")
        return b64encode(b64decode(sb_bytes)) == sb_bytes
    except (TypeError, binascii.Error):
        return False


def decode(src: str, dtype:np.dtype = np.dtype('int32')) -> NDArray:
    """Декодирует строку base64 в numpy массив с заданным типом данных."""
    if src == '':
        return np.array([], dtype=dtype) 
    return np.frombuffer(b64decode(src), dtype)


def encode(data: np.ndarray) -> str:
    """Кодирует numpy массив в строку base64."""
    return b64encode(data.tobytes()).decode()


class FCValue:

    type: Literal['formula', 'array', 'null'] = 'null'
    data: Union[np.ndarray, str]
    dim: int

    def __init__(self, src_data: str, dtype:np.dtype = np.dtype('int32'), dim=1):

        if src_data == '':
            self.data = np.array([], dtype=dtype)
            self.type = 'null'
        if isBase64(src_data):
            self.data = decode(src_data, dtype).reshape(-1, dim)
            self.type = 'array'
        else:
            self.data = src_data
            self.type = 'formula'

        self.dim = dim

    def resize(self, size: int):
        if isinstance(self.data, np.ndarray) and size > 0 and self.data.size % size == 0:
            self.data = self.data.reshape(size, -1)
            self.dim = self.data.shape[1]

    def dump(self) -> str:
        if isinstance(self.data, np.ndarray):
            return encode(self.data)
        else:
            return self.data

    def __len__(self):
        if self.type == 'array':
            return len(self.data)
        else:
            return 0