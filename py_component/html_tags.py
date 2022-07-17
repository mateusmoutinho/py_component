
from typing import Callable
from py_component import PyComponent


def creates_tag_creator(tag:str):
    def tag_creator(*elements)->PyComponent:
        
        props = {}
        if len(elements)> 0:
            if elements[0].__class__ == dict:
                props = elements[0]
                elements = elements[1::]
        
        component = PyComponent(tag,props)
        component.append(*elements)
        
        return component
    return tag_creator


div = creates_tag_creator('div')
h3 = creates_tag_creator('h3')