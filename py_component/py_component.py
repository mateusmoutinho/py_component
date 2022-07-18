
from copy import deepcopy
from os import sep
import re

from textwrap import indent
from typing import Any, Callable, NamedTuple

from py_component.props import Props
from py_component.tag_types import *


class PyComponent:

    def __init__(self,tag:str=None,props:dict={},tag_type:str=DEFAULT) -> None:
        
        self.childs = []
        self.props = props

        self.tag = tag 
        if tag_type not in VALID_TAG_TYPES:
            raise AttributeError(f'{tag_type} is invalid')
        self._tag_type = tag_type


    def get_prop(self,prop:str):
        return self.props.get(prop)
    
    def set_prop(self,prop:str,value:Any):
        self.props[prop] = value


    def find_by_function(self,filter_function:Callable):        
        for child in self.childs: 

            if child.__class__!= PyComponent:return 
            child:PyComponent
            
            result:bool = filter_function(child)
            if result:return child

            element:PyComponent = child.find_by_function(filter_function)
            if element:return element



    def find_by_id(self,id:str):
        return self.find_by_function(
            lambda child:child.get_prop('id') == id 
        )

    
    def append_childs(self,*elements):
        for element in elements:
                self.childs.append(element)
        return self 


    def _render_childs(self):
        text = ''
        for child in self.childs:
            
            if hasattr(child,'render'):
                text+=child.render()
            
            elif callable(child):
                text+=child()
            else:
                text+=f'{child} '
        return text 

    
    def render(self)->str:    
        child_text = self._render_childs()
    
        if self.tag:

            props_text = Props(self.props).render()

            if self._tag_type == DEFAULT:
                return  f'<{self.tag} {props_text}>{child_text}</{self.tag}>'

            if self._tag_type == NO_CLOSE:
                return f'<{self.tag} {props_text}>'

            if self._tag_type == AUTO_CLOSE:
                return  f'<{self.tag} {props_text}/>'
        
        else:
            return child_text
    
    
    def dumps(self,ident=4):
        text = self.render()
        return text

