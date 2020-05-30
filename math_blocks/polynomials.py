from .chains import chain

class polynomial(chain):
    def __init__(self, items, sign=True):
        chain.__init__(self, items=items, sign=sign)
