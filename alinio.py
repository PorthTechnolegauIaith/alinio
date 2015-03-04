import codecs
import nltk.data
import subprocess
import os
from argparse import ArgumentParser
import sys

class AliniwrError(Exception):
	pass

try:
	sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
except LookupError:
	os.system("./gosod_nltk.sh")
	sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	
local_hunalign = "/hunalign-1.1/src/hunalign/hunalign"

def alinio(file_cy, file_en, out_file):
	have_hunalign = False
	status = os.system("hunalign >/dev/null 2>&1")
	if status != 127 or os.path.exists(local_hunalign):
		have_hunalign = True
	
	if not have_hunalign:
		print("Mae angen i chi llwytho'r meddalwedd HunAlign i lawr cyn all defnyddio'r aliniwr....")
		print("Ewch i http://mokk.bme.hu/en/resources/hunalign/ am manylion")
		return

	if out_file == '-':
		f = sys.stdout
	else:
		f = codecs.open(out_file,"w","utf-8")
	cmd = "./hunalign-1.1/src/hunalign/hunalign hunalign-1.1/data/cy-en.dic -text -utf -realign '%s' '%s'" % (file_cy, file_en)
	subprocess.call(cmd,shell=True, stdout=f)
	f.close()


def brawddegau(in_file):
	out_file = u"%s-token%s" % (os.path.splitext(in_file))
	fo = codecs.open(out_file,"w","utf8")
	try:
		with codecs.open(in_file,'r',encoding='utf8') as fi:
			for rawtext in fi:
				sentences = sentence_detector.tokenize(rawtext.strip())
				for sentence in sentences:
					fo.write("\n" + sentence)
	except Exception as e:
		raise AliniwrError(str(e))
	finally:
		fo.close()
	return out_file

def main(file_cy, file_en, out_file, **args):
	cy_aligned = brawddegau(file_cy)
	en_aligned = brawddegau(file_en)
	alinio(cy_aligned, en_aligned, out_file)
	
if __name__ == '__main__':
	parser = ArgumentParser(description="Aliniwr Syml Python")
	parser.add_argument('-e', '--english', dest="file_en", required=True, help="Ffeil Saesneg i'w alinio")
	parser.add_argument('-c', '--cymraeg', dest='file_cy', required=True, help="Ffeil Cymraeg i'w alinio")
	parser.add_argument(dest='out_file', help="Ffeil i cadw allbwn hunalign. Defnyddiwch '-' ar gyfer stdout")
	parser.set_defaults(func=main)
	args = parser.parse_args()
	try:
		args.func(**vars(args))
	except Exception as e:
		print(e)