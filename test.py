
from PIL import Image
import Approaches.ColorQuantization as cq
import Approaches.PHash as phash
from Constructor.FeatureVectorConstructor import FeatureVectorConstructor as FVC


fvc1 = FVC('Data/Originals', 'phash')
fvc1.construct()
originals_p = fvc1.get_vector_dict()
t1 = fvc1.get_time_rate()
flip_p = fvc1.construct_with_attack('flip')

print(flip_p)
















