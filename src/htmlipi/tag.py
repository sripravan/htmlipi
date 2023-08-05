from .utils import dictionary_to_html_attributes_string

class Tag:
  def __init__(self, buffer, tag_name, attributes):
    self.buffer = buffer
    self.tag_name = tag_name
    self.attributes_string = " " + dictionary_to_html_attributes_string(attributes) if len(attributes) > 0 else ""
    self.buffer.append(f"<{self.tag_name}{self.attributes_string}/>")
  
  def __enter__(self):
    self.buffer.pop()
    self.buffer.append(f"<{self.tag_name}{self.attributes_string}>")
    return self
  
  def __exit__(self, exc_type, exc_value, traceback):
    self.buffer.append(f"</{self.tag_name}>")