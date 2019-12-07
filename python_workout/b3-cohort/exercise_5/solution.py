class ImmutableParent():
    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, f"_{attr}", value)

        setattr(self, _frozen, True)

    def __getattr__(self, attr):
        return getattr(self, f"_{attr}")


    def __setattr__(self, attr, value):
        if f"_{attr}" in vars(self).keys():
            raise ImmutableMeansImmutableError(f"Cannot set {attr}")
        super().__setattr__(attr, value)


class ImmutableMeansImmutableError(Exception):
    pass
