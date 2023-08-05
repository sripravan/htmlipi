import html

from .tag import Tag

class Renderer:
  def __init__(self):
    self.buffer = []
  
  def tag(self, tag_name, attributes):
    return Tag(self.buffer, tag_name, attributes)
  
  def __getattr__(self, name):
    def method(**kwargs):
      return self.tag(name, kwargs)
    return method
  
  def __call__(self, text, escape=True):
    if escape:
      self.buffer.append(html.escape(text))
    else:
      self.buffer.append(text) 

  def get_text(self):
    buffer_text = "".join(self.buffer)
    self.buffer = []
    return buffer_text