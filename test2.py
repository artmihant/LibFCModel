from base64 import b64decode, b64encode
import binascii
from typing import Literal, Tuple, Union

import numpy as np
from numpy.typing import NDArray


def isBase64(sb):
    """Проверяет, является ли строка корректной base64 (строгая проверка)."""
    try:
        if isinstance(sb, str):
            sb_bytes = bytes(sb, 'ascii')
        elif isinstance(sb, bytes):
            sb_bytes = sb
        else:
            raise ValueError("Argument must be string or bytes")

        # Длина base64 строки должна быть кратна 4
        if len(sb_bytes) % 4 != 0:
            return False

        decoded = b64decode(sb_bytes, validate=True)
        return b64encode(decoded) == sb_bytes
    except (TypeError, binascii.Error, ValueError):
        return False


print(isBase64('AgAAAAoAAAABAAAA'))