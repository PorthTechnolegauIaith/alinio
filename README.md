# Alinio

Er mwyn alinio testunau Cymraeg a Saesneg, rydym yn awgrymu eich bod chi'n defnyddio [hunalign](http://mokk.bme.hu/en/resources/hunalign/). 
Mae hunalign yn rhaglen ar ffurf gorchmynion terfynnell. Os oes well gennych chi ddefnyddio rhaglen gyda rhyngwyneb, mae [LF Aligner](http://aligner.sourceforge.net/) yn ddewis da ar gyfer Windows.

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
 
 Bydd angen gosod cydran segmentu NLTK fel hyn :
 
 ```python
 $ python
 Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
 [GCC 4.8.2] on linux2
 Type "help", "copyright", "credits" or "license" for more information.
 >>> import nltk
 >>> nltk.download()
 NLTK Downloader
---------------------------------------------------------------------------
    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
---------------------------------------------------------------------------
Downloader> d
Download which package (l=list; x=cancel)?
  Identifier> punkt
    Downloading package punkt to /home/gallu/nltk_data...
      Unzipping tokenizers/punkt.zip.
```

* Ffeil `.dic` ar gyfer hunalign a ddarparir gennym ni:

```sh
 $ cd hunalign-1.1/data
 $ wget wget http://techiaith.org/alinio/hunalign/cy-en.dic
 ```

Ar ôl dod â'r tri peth yma at eu gilydd, mae modd i chi alinio.



### Twitorial LFAligner

Gweler y ffeil [LFAligner](tut/LFAligner.md) am fwy o wybodaeth.

# Aligning

In order to align Welsh and English texts, we recommend that you use [hunalign](http://mokk.bme.hu/en/resources/hunalign/).
Hunalign uses a terminal and command line interface. If you prefer a programme with a graphical interface, [LF Aligner](http://aligner.sourceforge.net/) is a good option for Windows.

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

*  You'll need to install the NLTK segmenting program like this :

 ```python
 $ python
 Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
 [GCC 4.8.2] on linux2
 Type "help", "copyright", "credits" or "license" for more information.
 >>> import nltk
 >>> nltk.download()
 NLTK Downloader
---------------------------------------------------------------------------
    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
---------------------------------------------------------------------------
Downloader> d
Download which package (l=list; x=cancel)?
  Identifier> punkt
    Downloading package punkt to /home/gallu/nltk_data...
      Unzipping tokenizers/punkt.zip.
```

* A `.dic` file used by hunalign which we distribute 

```sh
 $ cd hunalign-1.1/data
 $ wget wget http://techiaith.org/alinio/hunalign/cy-en.dic
 ```

After bringing together these three elements, you are ready to start aligning your text.


### LFAligner Tutorial

See the file [LFAligner](tut/LFAligner.md) for more information.