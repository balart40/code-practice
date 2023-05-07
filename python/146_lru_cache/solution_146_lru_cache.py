class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.kv = dict()
        self.filo = []

    def checkLen(self):
        if len(self.kv) > self.cap:
            k = self.filo.pop(-1)
            del self.kv[k]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        doesExist = self.kv.get(key, None)
        if doesExist != None:
            idx = self.filo.index(key)
            self.filo.pop(idx)
            self.filo.insert(0,key)
            return self.kv[key]
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        doesExist = self.kv.get(key, None)
        if doesExist != None:
            idx = self.filo.index(key)
            self.filo.pop(idx)
        self.kv[key] = value
        self.filo.insert(0,key)
        self.checkLen()