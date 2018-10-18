from .patternizer import Patternizer, anim

def patternize(text=None, pattern="@", fontpath="./default_fonts/LobsterTwo-Bold.ttf", fontsize=15):
    if text is None:
        raise Exception("No text input.")
        
    patterns = Patternizer(text).using(pattern, fontpath=fontpath, fontsize=fontsize)
    return patterns
    
    
def animate(text, tm):
    for char in anim(text, tm):
        print(char, end="")
    print()
