def soma(x, y):
    """Soma x e Y

    >>> soma(10, 20)
    30

    >>> soma(10, 20)
    150

    >>> soma(10, 140)
    150

    >>> soma('10', 140)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    """

    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x + y


def subtrai(x, y):
    """subtrai x e Y

    >>> subtrai(10, 20)
    -10

    >>> subtrai(10, 20)
    150

    >>> subtrai(10, 140)
    -130

    >>> subtrai('10', 140)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float

    >>> subtrai(10, '140')
    Traceback (most recent call last):
    ...
    AssertionError: y precisa ser int ou float
    """

    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x - y


if __name__ == '__main__':
    import doctest

    # doctest.testmod() # Mostra apenas os quebrados
    doctest.testmod(verbose=True)  # Mostra todos os testes
