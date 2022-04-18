
from os import sep
from textwrap import indent


class PyComponent(list):

    def __init__(self,tag:str=None,props={},category="normal") -> None:
        self.tag = tag 
        self.props = props
        self.category = category


    def append(self,*elements):
        for element in elements:
            if element.__class__ == list:
                self.append(*element)
            super().append(element)
        return self 

    def _render_props(self)->str:
        keys = self.props.keys()
        text_props = ''
        for key in keys:

            text_props+= f' {key}="{self.props[key]}"'
        return text_props
    
    def _render_childs(self,ident:int)->str:
        rendered_childs = ''
        ident_text = self.create_ident_text(ident + ident)
        old_ident = self.create_ident_text(ident)
        for child in self:
            if hasattr(child,'render'):
                rendered_childs+= old_ident + child.render(ident) + old_ident
            else:
                rendered_childs+=str(child)

        return rendered_childs 

    @staticmethod
    def create_ident_text(ident:int)->str:
        ident_text = '\n'
        for x in range(ident):
            ident_text+=' '
        return ident_text
        
    def render(self, ident=4,old_ident=4)->str:
        
        props = self._render_props()
        childs = self._render_childs(ident)
        ident_text = ''
        if not self.tag:
            return childs
            
        if self.category == 'normal':
            return f'<{self.tag}{props}>{childs}<{self.tag}/>'

        if self.category == 'auto-close':
            return f'<{self.tag}{props}/>'

        if self.category == 'unique':
            return f'<{self.tag}{props}/>{childs}'




    def dump(self,out:str,ident=0):
        with open(out,'w') as arq:
            arq.write(self.dumps(ident))




