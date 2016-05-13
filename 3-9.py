class Comparator(object):
  def __init__(self, x):
    self.value = x
  def _cmp(self, value):
    if self.value == value:
      return 0
    else:
      return (self.value > value) - (self.value < value)

  def compare(self, other):
    try:
      return _cmp(other.value)
    except AttributeError:
      return 1
