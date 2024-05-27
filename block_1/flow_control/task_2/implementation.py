from enum import Enum


class DEGREE_TYPE(Enum):
    FARENHEIT = "F"
    CELCIUS = "C"


def convert_temperature(value, to_scale):
    """Конвертирует температуру в нужную системы счисления

    Args:
        value: значение температуры
        to_scale: система счисления, в которую нужно конвертировать значение

    Returns: значение как результат конвертации
    """
    try:
        to_scale = DEGREE_TYPE(to_scale)
        if to_scale == DEGREE_TYPE.FARENHEIT:
            return value * 9 / 5 + 32
        elif to_scale == DEGREE_TYPE.CELCIUS:
            return (value - 32) * 5 / 9
    except:
        return value
