class ImmutableParent():
    def __init__(self, **kwargs):
        # We could also go above the __setattr__ method of this class and use
        # object's within this __init__function by using:
        # object.__setattr__(self, key, value)
        self.__dict__ = kwargs

    def __setattr__(self, attr, value):
        if self.__dict__:
            raise ImmutableMeansImmutableError(f"Cannot set {attr}")
        super().__setattr__(attr, value)


class ImmutableMeansImmutableError(Exception):
    pass
