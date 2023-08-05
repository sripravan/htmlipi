from collections import namedtuple

def dictionary_to_html_attributes_string(dictionary):
  return " ".join(map(lambda key: f"{key}=\"{dictionary[key]}\"", dictionary.keys()))

def dictionary_to_context(dictionary):
  Context = namedtuple('Context', dictionary.keys())
  context = Context(**dictionary)
  return context