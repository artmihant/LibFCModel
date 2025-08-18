from base64 import b64decode, b64encode
import binascii
from typing import Literal, Tuple, Union

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

    def __init__(self, data_str: str, size: int, dtype:np.dtype = np.dtype('int32')):

        if data_str == '':
            self.data = np.array([], dtype=dtype)
            self.type = 'null'
        if isBase64(data_str):
            self.data = decode(data_str, dtype).reshape(size, -1)
            self.type = 'array'
        else:
            self.data = data_str
            self.type = 'formula'

    def dump(self) -> Tuple[str, int]:
        if isinstance(self.data, np.ndarray):
            return encode(self.data), len(self.data)
        else:
            return self.data, 0

    def __len__(self):
        if self.type == 'array':
            return len(self.data)
        else:
            return 0

