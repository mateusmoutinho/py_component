
from copy import deepcopy
from os import sep

from textwrap import indent
from typing import NamedTuple


class PyComponent:

    def __init__(self,tag:str=None,props:dict={},self_close:bool=False) -> None:
        self.childs = []
        self.props = props
        self.tag = tag 
        self.self_close = self_close


    def append(self,*elements):
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

    def _render_props(self):
        text = ''
        for key,value in self.props.items():
            text+=f'{key}="{value}" '
        return text 

    def _render_component(self)->str:    
        child_text = self._render_childs()
    
        if self.tag:
            props_text = self._render_props()
            if self.self_close:
                return  f'<{self.tag} {props_text}/>'
            else:
                return  f'<{self.tag} {props_text}>{child_text}</{self.tag}>'
        else:
            return child_text
    
    def render(self,ident=4):
        text = self._render_component()
        return text

