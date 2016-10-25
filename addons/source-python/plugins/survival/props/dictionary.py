'''



'''

__all__ = ('PropDictionary', )

from .entity import Prop
from .transmit import no_transmit_indexes

#
#
#

class PropDictionary(dict):
    "Dictionary to manage all props owned by a player."

    def __init__(self, owner, *args, **kwargs):
        "Initialize the helper dictionary."
        # Initialize python's built in dictionary.
        super().__init__(*args, **kwargs)
        # Store the owner which we use to define the props owners later.
        self.owner = owner

    def __missing__(self, name):
        "Call if item is missing from the dictionary."
        # Create the prop if non-existant.
        instance = self[name] = Prop.create_prop(name, self.owner)
        no_transmit_indexes.add(instance.index)
        return instance

    def __delitem__(self, name):
        "Delete item from the dictionary if existant."
        # No point to delete if not existant.
        if name not in self:
            return
        no_transmit_indexes.discard(self[name].index)
        super().__delitem__(name)

