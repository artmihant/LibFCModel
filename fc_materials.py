# Material property type codes per group
from typing import Dict, List, Literal, TypedDict, Union

from numpy import float64
from numpy.typing import NDArray

from fc_dependency import FCDependency


MATERIAL_PROPERTY_TYPES: Dict[str, Dict[int, str]] = {
    "elasticity": {
        0: "HOOK",
        1: "HOOK_ORTHOTROPIC",
        2: "HOOK_TRANSVERSAL_ISOTROPIC",
        3: "BLATZ_KO",
        4: "MURNAGHAN",
        11: "COMPR_MOONEY",
        20: "NEO_HOOK",
        21: "ANISOTROPIC",
    },
    "common": {0: "USUAL"},
    "thermal": {0: "ISOTROPIC", 1: "ORTHOTROPIC", 2: "TRANSVERSAL_ISOTROPIC"},
    "geomechanic": {
        0: "BIOT_ISOTROPIC",
        1: "BIOT_ORTHOTROPIC",
        2: "BIOT_TRANSVERSAL_ISOTROPIC",
    },
    "plasticity": {0: "MISES", 1: "DRUCKER_PRAGER", 4: "DRUCKER_PRAGER_CREEP", 9: "MOHR_COULOMB"},
    "hardening": {0: "LINEAR", 1: "MULTILINEAR"},
    "creep": {0: "NORTON"},
    "preload": {0: "INITIAL"},
    "strength": {0: "ISOTROPIC"},
}

MATERIAL_PROPERTY_TYPES_REVERSE: Dict[str, Dict[str, int]] = {
    group: {name: code for code, name in mapping.items()} for group, mapping in MATERIAL_PROPERTY_TYPES.items()
}


# Constant (const_names) codes per group
CONST_NAME_MAP: Dict[str, Dict[int, str]] = {
    "elasticity": {
        0: "YOUNG_MODULE",
        1: "POISSON_RATIO",
        2: "SHEAR_MODULUS",
        3: "BULK_MODULUS",
        4: "MU",
        5: "ALPHA",
        6: "BETA",
        7: "LAME_MODULE",
        8: "C3",
        9: "C4",
        10: "C5",
        16: "E_T",
        17: "E_L",
        18: "PR_T",
        19: "PR_TL",
        20: "G_TL",
        21: "G12",
        22: "G23",
        23: "G13",
        24: "PRXY",
        25: "PRYZ",
        26: "PRXZ",
        27: "C1",
        28: "C2",
        29: "D",
        82: "C_1111",
        83: "C_1112",
        84: "C_1113",
        85: "C_1122",
        86: "C_1123",
        87: "C_1133",
        88: "C_1212",
        89: "C_1213",
        90: "C_1222",
        91: "C_1223",
        92: "C_1233",
        93: "C_1313",
        94: "C_1322",
        95: "C_1323",
        96: "C_1333",
        97: "C_2222",
        98: "C_2223",
        99: "C_2233",
        100: "C_2323",
        101: "C_2333",
        102: "C_3333",
    },
    "common": {0: "DENSITY", 1: "STRUCTURAL_DAMPING_RATIO", 2: "MASS_DAMPING_RATIO", 3: "STIFFNESS_DAMPING_RATIO"},
    "thermal": {
        0: "COEF_LIN_EXPANSION",
        1: "COEF_THERMAL_CONDUCTIVITY",
        5: "COEF_THERMAL_CONDUCTIVITY_XX",
        9: "COEF_THERMAL_CONDUCTIVITY_YY",
        13: "COEF_THERMAL_CONDUCTIVITY_ZZ",
        14: "COEF_LIN_EXPANSION_X",
        15: "COEF_LIN_EXPANSION_Y",
        16: "COEF_LIN_EXPANSION_Z",
        17: "COEF_THERMAL_CONDUCTIVITY_T",
        18: "COEF_THERMAL_CONDUCTIVITY_L",
        19: "COEF_LIN_EXPANSION_T",
        20: "COEF_LIN_EXPANSION_L",
    },
    "geomechanic": {
        1: "FLUID_VISCOSITY",
        2: "POROSITY",
        3: "FLUID_BULK_MODULUS",
        4: "SOLID_BULK_MODULUS",
        19: "FLUID_DENSITY",
        20: "BIOT_MODULUS",
        0: "PERMEABILITY",
        5: "BIOT_ALPHA",
        6: "PERMEABILITY_XX",
        7: "PERMEABILITY_XY",
        8: "PERMEABILITY_XZ",
        9: "PERMEABILITY_YX",
        10: "PERMEABILITY_YY",
        11: "PERMEABILITY_YZ",
        12: "PERMEABILITY_ZX",
        13: "PERMEABILITY_ZY",
        14: "PERMEABILITY_ZZ",
        21: "BIOT_ALPHA_X",
        22: "BIOT_ALPHA_Y",
        23: "BIOT_ALPHA_Z",
        15: "PERMEABILITY_T",
        16: "PERMEABILITY_TT",
        17: "PERMEABILITY_TL",
        18: "PERMEABILITY_L",
        24: "BIOT_ALPHA_T",
        25: "BIOT_ALPHA_L",
    },
    "plasticity": {
        0: "YIELD_STRENGTH",
        5: "YIELD_STRENGTH_COMPR",
        7: "COHESION",
        8: "INTERNAL_FRICTION_ANGLE",
        9: "DILATANCY_ANGLE",
        21: "DPC_A",
        22: "DPC_N",
        23: "DPC_M",
    },
    "hardening": {
        2: "E_TAN",
        10: "E_TAN_COMPR",
        1: "TENSILE_STRAIN",
        6: "TENSILE_STRAIN_COMPR",
        0: "COMPRESSIVE_STRAIN",
        7: "COMPRESSIVE_STRAIN_COMPR",
        8: "STRESS",
        3: "MULTILINEAR_STRESS",
        9: "HARDENING",
        4: "HARDENING_COMPR",
        5: "PLASTIC_STRAIN",
        11: "PLASTIC_STRAIN_COMPR",
        12: "TABULAR_MODE_ID",
    },
}

CONST_NAME_REVERSE: Dict[str, Dict[str, int]] = {
    group: {name: code for code, name in mapping.items()} for group, mapping in CONST_NAME_MAP.items()
}


class FCMaterialProperty(TypedDict):
    """
    Определяет одно физическое свойство материала (e.g., плотность, модуль Юнга).
    """
    type: int  # Дополнительный ID типа свойства (обычно 0, но не всегда)
    name: int  # ID типа свойства (например, 0 - для плотности, если FCMaterialProperty относится к common)
    data: Union[NDArray[float64], str]  # Значение свойства (константа или массив для зависимостей)
    dependency: Union[List[FCDependency], int, str]  # Описание зависимости свойства


FCMaterialPropertiesTypes = Literal[
    "elasticity", # Упругость и вязкоупругость
    "common", # Общие свойства
    "thermal",  # Температурные свойства
    "geomechanic", # Геомеханика
    "plasticity", # Пластичность
    "hardening",  # Упрочнение
    "creep", # Позучесть
    "preload", # Преднагружение
    "strength" # Прочность
]

FCMaterialProperties = Dict[FCMaterialPropertiesTypes, List[FCMaterialProperty]]


class FCMaterial(TypedDict):
    """
    Определяет материал и набор его физических свойств.
    """
    id: int  # Уникальный идентификатор материала
    name: str  # Имя материала
    properties: FCMaterialProperties  # Словарь, где свойства сгруппированы по типам

