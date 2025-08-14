from base64 import b64decode, b64encode
import binascii
from typing import Union

import numpy as np
from numpy.typing import NDArray

ValueArray = Union[np.ndarray, str, int]

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


def fdecode(src: str, dtype:np.dtype = np.dtype('int32')) -> ValueArray:
    """
    "Гибкое" декодирование. Если строка является base64, декодирует ее в numpy массив.
    В противном случае, возвращает строку как есть (например, для значения 'all').
    """
    if src == '':
        return np.array([], dtype=dtype)
    if isBase64(src):
        return decode(src, dtype)
    return src


def fencode(data: ValueArray) -> str:
    """
    "Гибкое" кодирование. Если данные являются numpy массивом, кодирует его в строку base64.
    В противном случае, возвращает строку как есть (например, для значения 'all').
    """
    if isinstance(data, str):
        return data
    if isinstance(data, int):
        return str(data)
    if isinstance(data, np.ndarray):
        return encode(data)
    return ''