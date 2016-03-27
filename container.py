#!/usr/bin/env python

# The dataContainer store key value pairs.
# The value always store in a list
# If a key exists, then the values will extend the list.
class dataContainer:
    def __init__(self):
        self.container = {}

    # insert the dictionary data to the container
    def insert(self, data ):
        for key in data.keys():
            value = data.get(key)
            # Check if the key exist in the container
            if self.container.has_key ( key ):
                oriValue = self.container.get(key)
                oriValue.insert (0, value)
            else:
                # Always save the value in a list
                self.container.update ({key: [value]})

    # Return the list of value according to the key
    def get(self, key ):
        return self.container.get(key)

    # Return all items in the container
    def items(self):
        return self.container.items()

    # Return the value according to the key, and delete the key/value
    def pop(self, key ):
        value = self.container.get(key)
        # The value is a list, pop the last item of the list
        item = value.pop()
        if  len(value) == 0:
            # if the value list is empty, then pop the key
            self.container.pop(key)
        return item

    # return all keys in the container
    def keys(self):
        return self.container.keys() 

if __name__ == "__main__":
    c = dataContainer()
    c.insert ({'List' : [1,2,3]})
    c.insert ({'List' : "123"})
    l = [2,3,4]
    c.insert ({'List' : l})
    c.insert ({'List' : 456})
    c.insert ({'a' : 1})
    c.insert ({'b' : 2})

    print c.items()
    print c.get('List')
    print c.pop('List')
    print c.items()
    print c.pop('List')
    print c.items()
    print c.get('a')
    print c.pop('a')
    print c.pop('List')
    print c.pop('List')
    print c.items()
    print c.keys()
