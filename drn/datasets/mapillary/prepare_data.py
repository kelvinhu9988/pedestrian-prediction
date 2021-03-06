import os
import numpy as np
from collections import namedtuple
from PIL import Image

Label = namedtuple('Label' , [
    'name'        , # The identifier of this label, e.g. 'car', 'person', ... .
                    # We use them to uniquely name a class

    'id'          , # An integer ID that is associated with this label.
                    # The IDs are used to represent the label in ground truth images
                    # An ID of -1 means that this label does not have an ID and thus
                    # is ignored when creating ground truth images (e.g. license plate).
                    # Do not modify these IDs, since exactly these IDs are expected by the
                    # evaluation server.

    'trainId'     , # Feel free to modify these IDs as suitable for your method. Then create
                    # ground truth images with train IDs, using the tools provided in the
                    # 'preparation' folder. However, make sure to validate or submit results
                    # to our evaluation server using the regular IDs above!
                    # For trainIds, multiple labels might have the same ID. Then, these labels
                    # are mapped to the same class in the ground truth images. For the inverse
                    # mapping, we use the label that is defined first in the list below.
                    # For example, mapping all void-type classes to the same ID in training,
                    # might make sense for some approaches.
                    # Max value is 255!

    'hasInstances', # Whether this label distinguishes between single instances or not

    'color'       , # The color of this label
])

labels = [
    Label(name='Bird',                     id=0,  trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Ground Animal',            id=1,  trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Curb',                     id=2,  trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Fence',                    id=3,  trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Guard Rail',               id=4,  trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Barrier',                  id=5,  trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Wall',                     id=6,  trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Bike Lane',                id=7,  trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Crosswalk - Plain',        id=8,  trainId=0,  hasInstances=True,   color=(255, 255, 255)),
    Label(name='Curb Cut',                 id=9,  trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Parking',                  id=10, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Pedestrian Area',          id=11, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Rail Track',               id=12, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Road',                     id=13, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Service Lane',             id=14, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Sidewalk',                 id=15, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Bridge',                   id=16, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Building',                 id=17, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Tunnel',                   id=18, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Person',                   id=19, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Bicyclist',                id=20, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Motorcyclist',             id=21, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Other Rider',              id=22, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Lane Marking - Crosswalk', id=23, trainId=0,  hasInstances=True,   color=(255, 255, 255)),
    Label(name='Lane Marking - General',   id=24, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Mountain',                 id=25, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Sand',                     id=26, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Sky',                      id=27, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Snow',                     id=28, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Terrain',                  id=29, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Vegetation',               id=30, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Water',                    id=31, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Banner',                   id=32, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Bench',                    id=33, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Bike Rack',                id=34, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Billboard',                id=35, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Catch Basin',              id=36, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='CCTV Camera',              id=37, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Fire Hydrant',             id=38, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Junction Box',             id=39, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Mailbox',                  id=40, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Manhole',                  id=41, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Phone Booth',              id=42, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Pothole',                  id=43, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Street Light',             id=44, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Pole',                     id=45, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Traffic Sign Frame',       id=46, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Utility Pole',             id=47, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Traffic Light',            id=48, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Traffic Sign (Back)',      id=49, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Traffic Sign (Front)',     id=50, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Trash Can',                id=51, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Bicycle',                  id=52, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Boat',                     id=53, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Bus',                      id=54, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Car',                      id=55, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Caravan',                  id=56, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Motorcycle',               id=57, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='On Rails',                 id=58, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Other Vehicle',            id=59, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Trailer',                  id=60, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Truck',                    id=61, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Wheeled Slow',             id=62, trainId=1,  hasInstances=True,   color=(0, 0, 0)),
    Label(name='Car Mount',                id=63, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Ego Vehicle',              id=64, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
    Label(name='Unlabeled',                id=65, trainId=1,  hasInstances=False,  color=(0, 0, 0)),
]

def prepare_mapillary_training(label_dir, out_dir, out_color_dir):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    if not os.path.exists(out_color_dir):
        os.makedirs(out_color_dir)
    length = len(os.listdir(label_dir))
    count = 0
    DUO_PALETTE = np.array([[217, 83, 79], [0, 0, 0]], dtype=np.uint8)
    for i, file_name in enumerate(os.listdir(label_dir)):
        image = np.array(Image.open(os.path.join(label_dir, file_name)))

        if is_valid(image):      
            # Save id maps
            id_map = label_to_train_id(image)
            out_path = os.path.join(out_dir, file_name)
            
            # Save color maps
            color_map = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
            color_map[id_map == 0] = DUO_PALETTE[0]
            color_map[id_map == 1] = DUO_PALETTE[1]
            color_map = Image.fromarray(color_map)
            out_color_path = os.path.join(out_color_dir, file_name)
            
            print('({i}/{length}) Writing to {out_path}'.format(i=i+1, length=length, out_path=out_path))
            id_map = Image.fromarray(id_map)
            id_map.save(out_path)
            color_map.save(out_color_path)

            count += 1
        else:
            print('({i}/{length}) Skipping'.format(i=i+1, length=length))
    print('Finish preparing {} crosswalk masks'.format(count))


def is_valid(array):
    threshold = 512
    num_pixels = np.sum(array == 0)
    return num_pixels > threshold

# Convert label ids in a label mask to corresponding train ids
def label_to_train_id(array):
    out_array = np.empty_like(array)
    for l in labels:
        out_array[array == l.id] = l.trainId
    return out_array


if __name__ == "__main__":
    label_dirs = ['training/labels', 'validation/labels']
    out_dirs = ['training/train_ids', 'validation/train_ids']
    out_color_dirs = ['training/train_ids_color', 'validation/train_ids_color']
    for i in range(len(label_dirs)):
        prepare_mapillary_training(label_dirs[i], out_dirs[i], out_color_dirs[i])