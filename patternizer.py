from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time

def anim(text, tm):
    print( len(text.split("\n")) )
    for char in text:
        time.sleep(tm)
        yield char
        
class Patternizer(object):
    def __init__(self, text):
        self.texts=filter(lambda txt: txt, text.split("\n"))
    
    def using(self, pattern_char, fontpath=None, fontsize=None):
        self.output=[]
        for text in self.texts:
            self.output.append( self._patternize_text(text,pattern_char, fontpath, fontsize) )
        return "\n\n".join(self.output)
        
    def _insert_pattern(self,array, char):
        result = np.where(array, char, " ")
        txt = '\n'.join([''.join(row) for row in result])
        return txt

    def _patternize_text(self, text, pattern_char, fontpath=None, fontsize=None):
        font = ImageFont.truetype(fontpath, fontsize)
        width, height = font.getsize(text)
        image = Image.new('L', (width, height), 1)
        drw = ImageDraw.Draw(image)
        drw.text((0,0), text, font=font)
        array = np.asarray(image)
        array = np.where(array, 0, 1)
        array = array[(array != 0).any(axis=1)]
        txt=self._insert_pattern(array, pattern_char)
        return txt
        

