#!/usr/bin/env python

# The dataContainer store key value pairs.
# If a key exists, then the values will save in a list.
# Please do not store list to the data container.
class dataContainer:
    def __init__(self):
        self.container = {}

    # insert the dictionary data to the container
    def insert(self, data ):
        for key in data.keys():
            value = data.get(key)
            # Check if the key exist
            if self.container.has_key ( key ):
                oriValue =  self.container.get(key)
                value = [value]
                if type(oriValue) is list:
                    value.extend ( oriValue )
                else:
                    value.append ( oriValue )
            # update the container
            self.container.update ({key: value})

    # Return the value according to the key
    def get(self, key=None ):
        if key==None:
            return self.container.items()
        else:
            return self.container.get(key)

    # Return the value according to the key, and delete the key/value
    def pop(self, key ):
        value = self.container.get(key)
        if type(value) is list:
            # If the value is a list, pop the last item of the list
            item = value.pop()
            return item
        else:
            return self.container.pop(key)

    # return all keys in the container
    def keys(self):
        return 

if __name__ == "__main__":
    c.insert ({'List' : "123"})
    c.insert ({'List' : "abc"})
    c.insert ({'List' : "345"})
    c.insert ({'a' : 1})
    c.insert (b = 2)

    print c.get()
    print c.pop('List')
    print c.get()
    print c.pop('a')
    print c.get()
