# adapted from https://github.com/mitmul/caltech-pedestrian-dataset-converter/blob/master/scripts/convert_seqs.py

import os
import glob
import cv2 as cv


def save_img(dname, fn, i, frame):
	cv.imwrite('{}/{}_{}_{}.png'.format(
		out_dir, os.path.basename(dname),
		os.path.basename(fn).split('.')[0], i), frame)

out_dir = '/content/darknet/build/darknet/x64/data/obj'
if not os.path.exists(out_dir):
	os.makedirs(out_dir)

def convert(dir):
	for dname in sorted(glob.glob(dir)):
		for fn in sorted(glob.glob('{}/*.seq'.format(dname))):
			cap = cv.VideoCapture(fn)
			i = 0
			while True:
				ret, frame = cap.read()
				if not ret:
					break
				save_img(dname, fn, i, frame)
				i += 1
			print(fn)

convert('/content/darknet/data/set00')
convert('/content/darknet/data/set01')
convert('/content/darknet/data/set02')
convert('/content/darknet/data/set03')
convert('/content/darknet/data/set04')
convert('/content/darknet/data/set05')
convert('/content/darknet/data/set06')
convert('/content/darknet/data/set07')
convert('/content/darknet/data/set08')
convert('/content/darknet/data/set09')
convert('/content/darknet/data/set10')
