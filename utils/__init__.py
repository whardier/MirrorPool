#Make this less stupid
def module_loader(namespace='', module_list=[], submodule=[]):
  for module in module_list:
    elements = module.split('.')
    for i in range(1,len(elements)):
      module_path = '.'.join([namespace] + elements[0:1])
      __import__(module_path)
