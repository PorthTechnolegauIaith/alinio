import codecs
import nltk.data
import subprocess
import os

class AliniwrError(Exception):
	pass

sentence_detector=nltk.data.load('tokenizers/punkt/english.pickle')

def alinio(file_cy, file_en, outfile):

	if not os.path.exists('hunalign-1.1'):
        	print("Mae angen i chi llwytho'r meddalwedd HunAlign i lawr cyn all defnyddio'r aliniwr....")
        	print("Ewch i http://mokk.bme.hu/en/resources/hunalign/ am manylion")

	f=codecs.open(outfile,"w","utf-8")
	cmd="./hunalign-1.1/src/hunalign/hunalign data/cy-en.dic -text -utf -realign " + file_cy + " " + file_en
	subprocess.call(cmd,shell=True, stdout=f)
	f.close()


def brawddegau(inFile, outFile):
	
	fo=codecs.open(outfile,"w","utf8")
	with codecs.open(inFile,'r',encoding='utf8') as fi:
		for rawtext in fi:
			sentences=sentence_detector.tokenize(rawtext.strip())
			for sentence in sentences:
				fo.write("\n" + sentence)

	fi.close()
	fo.close()

if __name__ == '__main__':

	
		 	
