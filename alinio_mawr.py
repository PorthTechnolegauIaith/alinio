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


def alinio(file_cy, file_en, out_file, batch_name):

	have_hunalign = False
	status = os.system("hunalign >/dev/null 2>&1")
	if status != 127 or os.path.exists(local_hunalign):
		have_hunalign = True
	
	if not have_hunalign:
		print("Mae angen i chi llwytho'r meddalwedd HunAlign i lawr cyn all defnyddio'r aliniwr....")
		print("Ewch i http://mokk.bme.hu/en/resources/hunalign/ am manylion")
		return

	#cmd = "./hunalign-1.1/src/hunalign/hunalign hunalign-1.1/data/cy-en.dic -text -utf -realign '%s' '%s'" % (file_cy, file_en)
	cmd = "python hunalign-1.1/scripts/partialAlign.py %s %s %s cy en 5000 > %s " % (file_cy, file_en, out_file, batch_name)

	subprocess.call(cmd, shell=True)


def alinio_batch(batch_name):
	
        cmd = "./hunalign-1.1/src/hunalign/hunalign hunalign-1.1/data/cy-en.dic -text -utf -realign -batch %s" % (batch_name)
        #cmd = "python hunalign-1.1/scripts/partialAlign.py %s %s %s cy en 5000 > %s " % (file_cy, file_en, out_file, batch_name)

        subprocess.call(cmd, shell=True)
	

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


def main(file_cy, file_en, out_file, batch_name, detect_sentences, **args):

	if (detect_sentences=='YES'):
		cy_aligned = brawddegau(file_cy)
		en_aligned = brawddegau(file_en)
		alinio(cy_aligned, en_aligned, out_file, batch_name)
	else:
		alinio(file_cy, file_en, out_file, batch_name)

	alinio_batch(batch_name)

	
if __name__ == '__main__':

	parser = ArgumentParser(description="Aliniwr Syml Python")
	parser.add_argument('-e', '--english', dest="file_en", required=True, help="Ffeil mawr Saesneg i'w alinio")
	parser.add_argument('-c', '--cymraeg', dest='file_cy', required=True, help="Ffeil mawr Cymraeg i'w alinio")
	parser.add_argument('-b', '--batchname', dest='batch_name', required=True, help="Enw ar gyfer y casgliad o ffeiliau ar gyfer alinio llawn")
	parser.add_argument('-s', '--sentence-detect', dest='detect_sentences', required=True, help="Os dylid canfod brawddegau (YES / NO)")
	parser.add_argument(dest='out_file', help="Ffeil i cadw allbwn hunalign. Defnyddiwch '-' ar gyfer stdout")
	parser.set_defaults(func=main)
	args = parser.parse_args()

	try:
		args.func(**vars(args))
	except Exception as e:
		print(e)
		print("e.e. python alinio_mawr.py -e CofnodYCynulliad/CofnodYCynulliad.en -c CofnodYCynulliad/CofnodYCynulliad.cy -b CofnodYCynulliad/hunspell_batch CofnodYCynulliad/CofnodYCynulliad.aligned")


