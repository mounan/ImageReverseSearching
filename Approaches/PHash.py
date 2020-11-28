import imagehash

def get_phash_vector(img):
    '''
    img: PIL.Image.open('path')
    '''
    return imagehash.phash(img)

def dist(h1, h2):
    '''
    hamming distance
    '''
    pass
