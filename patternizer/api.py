import os
from pkg_resources import resource_filename

from .patternizer import Patternizer, anim
from . import patternizer

default_font = resource_filename(
    'patternizer.resources.default_fonts', 
    'LobsterTwo-Bold.ttf'
)

def patternize(text=None, 
               pattern="@", 
               fontpath=default_font, 
               fontsize=15):
    if text is None:
        raise Exception("No text input.")
    
    patterns = Patternizer(text).using(
        pattern, 
        fontpath=fontpath, 
        fontsize=fontsize
    )
    return patterns
    
    
def animate(text, tm):
    for char in anim(text, tm):
        print(char, end="")
    print()
