

from typing import Any


class Props:

    def __init__(self,props:dict={}) -> None:
        self._props = props
    
    def render(self):
        text = ''
        for key,value in self._props.items():
            text+=f'{key}="{value}" '
        return text 
    
