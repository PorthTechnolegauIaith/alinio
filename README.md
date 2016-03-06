# Alinio

Er mwyn alinio testunau Cymraeg a Saesneg, rydym yn awgrymu eich bod chi'n defnyddio [hunalign](http://mokk.bme.hu/en/resources/hunalign/) fel y gwelir isod. 
Mae hunalign yn rhaglen ar ffurf gorchmynion terfynnell. 

Os oes well gennych chi ddefnyddio rhaglen gyda rhyngwyneb, mae [LF Aligner](http://aligner.sourceforge.net/) yn ddewis da ar gyfer Windows.

### Gosod y Meddalwedd Alinio

Mae'r project yma yn cynnwys cod Python sy'n hwyluso defnyddio hunalign o fewn terfynnell.  

Cyn cychwyn alinio, bydd angen 3 peth:

 * Gosod Hunalign (neu LF Aligner) ar eich peiriant gyda'r gorchmynion canlynol:

```sh
 $ wget ftp://ftp.mokk.bme.hu/Hunglish/src/hunalign/latest/hunalign-1.1.tgz
 $ tar zxvf hunalign-1.1.tgz 
 $ cd hunalign-1.1/src/hunalign
 $ make
```

 * Gosod NLTK, bydd o gymorth wrth segmentu'r testun yn frawddegau:

```sh
 $ sudo easy_install pip
 $ sudo pip install -U nltk
 ```

 * Gosod ffeil `.dic` ar gyfer hunalign a ddarparir gennym ni:

```sh
 $ wget http://techiaith.org/alinio/hunalign/cy-en.dic -O hunalign-1.1/data/cy-en.dic
 ```

Ar ôl dod â'r tri peth yma at eu gilydd, mae modd i chi alinio.

### Alinio ffeiliau testun

Defnyddiwch y sgript python `alinio.py` er mwyn alinio ffeiliau testun.

Mae angen 3 'mewnbwn' ar y sgript:
* Eich ffeil testun Saesneg
* Eich ffeil testun Cymraeg
* Enw ar gyfer ffeil allbwn y data sydd wedi'i alinio (neu `-` ar gyfer stdout)

Yna gallwch redeg y sgript gyda'r gorchymyn isod:

```sh
$ python alinio.py -e ffeil_saesneg.txt -c ffeil_cymraeg.txt allbwn.txt
```

Agorwch y ffeil `allbwn.txt` er mwyn gweld y data wedi'i alinio:
```
Ffonau symudol Android ac iOS       Android and iOS mobile phones       1.3
Cyfrifiaduron bwrdd gwaith      Desktop computers       0.158824
Gliniaduron     Laptops     0.15
Pa Wasanaethau API sydd ar gael?        What API Services are available?        0.789286
```


### Twitorial LFAligner

Gweler y ffeil [LFAligner](tut/LFAligner.md) am fwy o wybodaeth.

--------

# Aligning

In order to align Welsh and English texts, we recommend that you use [hunalign](http://mokk.bme.hu/en/resources/hunalign/) as seen below.
Hunalign uses a terminal and command line interface. 

If you prefer a programme with a graphical interface, [LF Aligner](http://aligner.sourceforge.net/) is a good option for Windows.

## Setup 
This project contains Python code which makes using hunalign in a terminal easier.  

Before starting your alignment, you will need 3 things:

* An installation of hunalign (or LF Aligner) on your machine

```sh
 $ wget ftp://ftp.mokk.bme.hu/Hunglish/src/hunalign/latest/hunalign-1.1.tgz
 $ tar zxvf hunalign-1.1.tgz 
 $ cd hunalign-1.1/src/hunalign
 $ make
```

* An installation of NLTK, which will help you in the process of segmenting text into 
sentences: 

```sh
 $ sudo easy_install pip
 $ sudo pip install -U nltk
 ```

* A `.dic` file used by hunalign which we distribute 

```sh
 $ cd hunalign-1.1/data
 $ wget http://techiaith.org/alinio/hunalign/cy-en.dic -O hunalign-1.1/data/cy-en.dic
 ```

After bringing together these three elements, you are ready to start aligning your text.

### Alinining text files

User the Python script `alinio.py` to align your text files1

The script requirest three input parameters:
* The name of your English text file
* The name of your Welsh text file
* A name for your output file where aligned data is stored. (use `-` for stdout)

You can then use the script in the following way:

```sh
$ python alinio.py -e enlgish_file.txt -c welsh_file.txt output.txt
```

Open the `output.txt` file to see your aligned data:
```
Ffonau symudol Android ac iOS       Android and iOS mobile phones       1.3
Cyfrifiaduron bwrdd gwaith      Desktop computers       0.158824
Gliniaduron     Laptops     0.15
Pa Wasanaethau API sydd ar gael?        What API Services are available?        0.789286
```


### LFAligner Tutorial
See the file [LFAligner](tut/LFAligner.md) for more information.
