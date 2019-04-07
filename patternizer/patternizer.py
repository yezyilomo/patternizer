import numpy as np
from PIL import Image, ImageDraw, ImageFont

def _insert_pattern(array, char):
    result = np.where(array, char, " ")
    text = '\n'.join([''.join(row) for row in result])
    return text


def _patternize_text_line(text, pattern_char, fontpath=None, fontsize=None):
    font = ImageFont.truetype(fontpath, fontsize)
    width, height = font.getsize(text)
    image = Image.new('L', (width, height), 1)
    drw = ImageDraw.Draw(image)
    drw.text((0,0), text, font=font)
    array = np.asarray(image)
    array = np.where(array, 0, 1)
    array = array[(array != 0).any(axis=1)]
    text = _insert_pattern(array, pattern_char)
    return text


def _patternize_text(text, pattern_char, fontpath=None, fontsize=None):
    output=[]
    text_lines=filter(lambda text: text, text.split("\n"))
    for text_line in text_lines:
        output.append(
            _patternize_text_line(text,pattern_char, fontpath, fontsize)
        )
    return "\n\n".join(output)


def _patternize_image(image_path, pattern_char, image_size=None):
    img = Image.open(image_path)
    if image_size is not None:
        img.thumbnail(image_size, Image.ANTIALIAS)
    ary = np.array(img)
    
    # Split the three channels
    r,g,b, _ = np.split(ary, 4, axis=2)
    r=r.reshape(-1)
    g=r.reshape(-1)
    b=r.reshape(-1)
    
    # Standard RGB to grayscale 
    bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], zip(r,g,b)))
    bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
    bitmap = np.dot((bitmap > 128).astype(float),255)
    
    array = bitmap
    #array = np.where(array, 0, 1)
    #array = array[(array != 0).any(axis=1)]
    text = _insert_pattern(array, pattern_char)
    return text
    