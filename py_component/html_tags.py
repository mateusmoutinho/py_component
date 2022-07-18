
from typing import Callable
from py_component import PyComponent
from py_component.tag_types import * 


def creates_tag_creator(tag:str,tag_type:str=DEFAULT):
    def tag_creator(*elements)->PyComponent:
        props = {}
        if len(elements)> 0:
            if elements[0].__class__ == dict:
                props = elements[0]
                elements = elements[1::]
        
        component = PyComponent(tag,props,tag_type)
        component.append_childs(*elements)
        
        return component
    return tag_creator

Input = creates_tag_creator('input',NO_CLOSE)
div = creates_tag_creator('div')
h3 = creates_tag_creator('h3')