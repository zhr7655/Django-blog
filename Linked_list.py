#链表的基础实现
class Link:
    def __init__(self,first,rest=None):
        if rest:
            assert isinstance(rest,Link)
        self.first = first
        self.rest = rest

    def len(self):
        length = 0
        lnk = self
        while lnk:
            length += 1
            lnk = lnk.rest
        return length



        
    def __repr__(self):
        if self.rest:
            return 'Link(' + str(self.first) + ',' + self.rest.__repr__() +')'
        else:
            return 'Link(' + str(self.first) + ')'

    def __str__(self):
        if self.rest:
            return '< ' + str(self.first) + ' ' + self.rest.__str__() + '>'
        else:
            return '< ' + str(self.first) + '>'   
        
a = Link(1,Link(2,Link(3)))

def map(lnk,f):
    link = lnk
    while link:
        link.first = f(link.first)
        link = link.rest
    return lnk

def sumation(lnk,f):
    lnk = map(lnk,f)
    link = lnk
    result = 0
    while link:
        result += link.first
        link = link.rest
    return result

def reverse(lnk):
    lnk1 = lnk
    lnk2 = lnk.rest
    lnk1.rest = None
    while lnk2:
        lnk3 = lnk1
        lnk1 = lnk2
        lnk2 = lnk2.rest
        lnk1.rest = lnk3
    return lnk1


