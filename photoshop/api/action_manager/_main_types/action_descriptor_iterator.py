from ..utils import *

class ActionDescriptor_Iterator:
  '''An iterator. You don't need to initialize it manually.'''

  def __init__(self, psobj: 'ActionDescriptor'):
    self.curobj = psobj
    self.n = -1

  def __next__(self) -> str:
    self.n += 1
    try:
      keyid = self.curobj.getKey(self.n)
    except:
      raise StopIteration
    keystr = id2str(keyid)
    return keystr

  def __repr__(self):
    return '<ActionDescriptor_Iterator at index:%d>'%self.n