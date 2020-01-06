import numpy as np
import scipy.misc as misc

def render_image_font(x, path,img_per_row,unit_scale=True):
    if unit_scale:
        bitmaps=(x * 255.).astype(dtype=np.int16) % 256
    else:
        bitmaps= x

    num_imgs,w,h=x.shape
    assert w==h
    side=int(w)

    width = img_per_row * side
    height = int(np.ceil(float(num_imgs) / img_per_row)) * side
    canvas = np.zeros(shape=(height, width), dtype=np.int16)
    canvas.fill(255)
    for idx, bm in enumerate(bitmaps):
        x = side * int(idx / img_per_row)
        y = side * int(idx % img_per_row)
        canvas[x: x + side, y: y + side] = bm
    misc.toimage(canvas).save(path)
    return path
