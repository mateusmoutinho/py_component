
from copy import deepcopy
from os import sep

from textwrap import indent
from typing import NamedTuple


class PyComponent:

    def __init__(self,tag:str=None,props:dict={},category="normal") -> None:
        self.tag = tag 
        self.childs = []
        self.props = props
        self._fragment = False  if self.tag else True 
        self._category = category


    def append(self,*elements):
        for element in elements:
                self._childs.append(*element)

    def _render_props(self)->str:
        
        return text_props
