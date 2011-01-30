
import types
import copy

#Note: Make this less stupid
def module_loader(namespace='', module_list=[]):
  for module in module_list:
    module_arguments = None
    module_file = module

    if type(module) == types.TupleType:
      module_file = module[0]
      if len(module) > 1:
        module_arguments = module[1]

    elements = module_file.split('.')

    for i in range(1,len(elements)):
      elements_range = elements[0:i]
      module_path = '.'.join([namespace] + elements_range)
      module_import = __import__(module_path)

    if module_arguments:
      m = getattr(module_import, elements_range[0])
      for i in elements_range[1:]:
        m = getattr(m, i)
      m.args = copy.copy(module_arguments)
