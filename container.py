#!/usr/bin/env python

class dataContainer:
    '''
    The dataContainer store key value pairs.
    The value always store in a list
    If a key exists, then the values will extend the list.
    '''
    def __init__(self):
        '''
        Initial the data container
        '''
        self.container = {}

    def insert(self, data):
        '''
        Insert the dictionary data to the container
        If the key already in the dict, save the values in a list
        Args:
            data: {key: value}
        '''
        for key in data.keys():
            value = data.get(key)
            # Check if the key exist in the container
            if self.container.has_key ( key ):
                oriValue = self.container.get(key)
                oriValue.insert (0, value)
            else:
                # Always save the value in a list
                self.container.update ({key: [value]})

    def get(self, key):
        '''
        Return the list of value according to the key
        Args:
            key: keyword
        Returns:
            list of the value
        '''
        return self.container.get(key)

    def items(self):
        '''
        Return all items in the container
        Return:
            Dictionary of all data
        '''
        return self.container.items()

    def pop(self, key):
        '''
        Return the value according to the key, and delete the key/value
        Args:
            key: keyword
        Returns:
            list of the value
        '''
        value = self.container.get(key)
        # The value is a list, pop the last item of the list
        item = value.pop()
        if  len(value) == 0:
            # if the value list is empty, then pop the key
            self.container.pop(key)
        return item

    # return all keys in the container
    def keys(self):
        '''
        Return all keys in the container
        Return:
            keywords
        '''
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
