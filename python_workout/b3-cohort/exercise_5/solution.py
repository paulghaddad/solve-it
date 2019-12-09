class ImmutableParent():
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __setattr__(self, attr, value):
        if self.__dict__:
            raise ImmutableMeansImmutableError(f"Cannot set {attr}")
        super().__setattr__(attr, value)


class ImmutableMeansImmutableError(Exception):
    pass
