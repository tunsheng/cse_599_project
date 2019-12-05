import os
import h5py
import argparse
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import PIL

def main(input_dir, output_dir):
    WIDTH=256
    HEIGHT=256
    NCHANNEL=3
    filenames = os.listdir(input_dir)
    N = len(filenames)
    output_path = output_dir+'/manga.hdf5'
    # if os.path.exists(output_path):
    #     os.remove(output_path)
    # h5py_file = h5py.File(output_path, 'w')
    # dtype = h5py.special_dtype(vlen=np.dtype('uint8'))
    # dset = h5py_file.create_dataset('images', (N, HEIGHT, WIDTH, NCHANNEL), dtype=np.uint8, chunks=True)
    # for i in range(N):
    #     if filenames[i][-4:] == '.jpg':
    #         input_path = input_dir+'/'+filenames[i]
    #         image = Image.open(input_path)
    #         image = image.resize((HEIGHT, WIDTH), PIL.Image.ANTIALIAS)
    #         image = np.array(image.convert("RGB")).astype(np.uint8)
    #         dset[i] = image
    test(output_dir)

def test(output_dir):
    output_path = output_dir+'/manga.hdf5'
    h5_file = h5py.File(output_path, 'r')
    images = h5_file['images']
    print(len(images))
    print(images[0].shape)
    plt.imshow(images[0])
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_dir', dest='input_dir', type=str,
                    help='Input directory containing .jpg images')
    parser.add_argument('--output_dir', dest='output_dir', type=str,
                    help='Output directory containing .h5 images')
    args = parser.parse_args()
    if args.input_dir is None or args.output_dir is None:
        raise Exception('Please specify an input and output directory')
    print("Running")
    main(args.input_dir, args.output_dir)
