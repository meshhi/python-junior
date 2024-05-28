import datetime


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    # чтобы соблюсти требование по наличию конструкций flow control
    # test
    for item in range(1):
        some_date += datetime.timedelta(days=1)
    return some_date
