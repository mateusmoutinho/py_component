
from os import sep
from textwrap import indent


class PyComponent(list):

    def __init__(self,tag:str=None,props={},category="normal") -> None:
        self.tag = tag 
        self.fragment = False  if self.tag else True 
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
    
    def _render_childs(self,ident:int,acumulated_ident:int)->str:
        rendered_childs = ''
        
        print(acumulated_ident)
        acumulated_ident = acumulated_ident + ident if not self.fragment else acumulated_ident
        for child in self:
            if hasattr(child,'render'):

                rendered_childs+=  child.render(ident,acumulated_ident) 
            else:
                rendered_childs+=str(child)
    
        return rendered_childs 


    def render(self, ident=4,acumulated_ident=0)->str:
        props = self._render_props()

        childs = self._render_childs(ident,acumulated_ident)
        ident_text = self.create_ident_text(acumulated_ident)
        
        if not self.tag:
            return childs
            
        if self.category == 'normal':
            return f'{ident_text}<{self.tag}{props}>{childs}{ident_text}<{self.tag}/>'

        if self.category == 'auto-close':
            return f'<{self.tag}{props}/>'

        if self.category == 'unique':
            return f'<{self.tag}{props}/>{childs}'



    def dump(self,out:str,ident=0):
        with open(out,'w') as arq:
            arq.write(self.dumps(ident))




    @staticmethod
    def create_ident_text(ident:int)->str:
        ident_text = '\n'
        for x in range(ident):
            ident_text+=' '
        return ident_text
        
