# adapted from https://github.com/mitmul/caltech-pedestrian-dataset-converter/blob/master/scripts/convert_seqs.py

import os
import glob
import cv2 as cv


def save_img(dname, fn, i, frame):
	cv.imwrite('{}/{}_{}_{}.png'.format(
		out_dir, os.path.basename(dname),
		os.path.basename(fn).split('.')[0], i), frame)

out_dir = 'images'
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

convert('/content/set00')
convert('/content/set01')
convert('/content/set02')
convert('/content/set03')
convert('/content/set04')
convert('/content/set05')
convert('/content/set06')
convert('/content/set07')
convert('/content/set08')
convert('/content/set09')
convert('/content/set10')
