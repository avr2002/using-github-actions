# pylint: disable=R0903, C0114, E0015
class Duck:
    """
    Random Duck class.
    Duck can quack and swim.
    """

    def __init__(self) -> None: ...

    def __getattr__(self, attr: str):
        if attr == "quack":
            return lambda: print("quack")

        if attr == "swim":
            return lambda: print("splash")

        raise AttributeError


duck = Duck()


# # no type hinting!!
duck.quack()
duck.swim()
# duck.eat() # noqa: ERA001
