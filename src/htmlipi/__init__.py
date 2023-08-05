from .renderer import Renderer
from .utils import dictionary_to_context

def template(func):
  r = Renderer()

  def wrapper(context_dictionary):
    context = dictionary_to_context(context_dictionary)
    func(r, context)
    return r.get_text()
  
  return wrapper