import os
from pkg_resources import resource_filename

from .patternizer import _patternize_text, _patternize_image
from . import patternizer

default_font = resource_filename(
    'patternizer.resources.default_fonts', 
    'LobsterTwo-Bold.ttf'
)

def patternize_text(text=None, 
                   pattern="@", 
                   fontpath=default_font, 
                   fontsize=15):
    if text is None:
        raise TypeError("No text input.")
    
    patterns = _patternize_text(
        text,
        pattern, 
        fontpath=fontpath, 
        fontsize=fontsize
    )
    return patterns

def patternize_image(path=None, 
                   pattern="@",
                   size=None):
    if path is None:
        raise TypeError("No Image input.")
    
    patterns = _patternize_image(
        path, 
        pattern_char=pattern, 
        image_size=size
    )
    return patterns
    
    