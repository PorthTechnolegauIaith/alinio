## *** Cyflwyniad ***

Bwriedir LF Aligner at ddefnydd cyfieithwyr sydd eisiau creu atgofion cyfieithu o gyfieithiadau a grëwyd heb arf CAT neu o unrhyw destun arall sydd ar gael mewn dwy neu fwy iaith. Ysgrifennwyd y rhaglen er mwyn gwneud yr algorithm alinio brawddegau awtomatig, Hunalign, (gwelwch http://mokk.bme.hu/resources/hunalign) yn haws i’w defnyddio. Mae gan LF Aligner hefyd nodweddion a’u dyluniwyd ar gyfer adeiladu corpora ar raddfa mawr, gan gynnwys y gallu i drin setiau data enfawr, hidlo data integredig, modd swp, segmentu awtomatig a gweithredu heb gymorth. Mae gan yr aliniwr hefyd nodweddion eraill fel creu ffeiliau TMX a llwytho rheolau yr Undeb Ewropeaidd neu unrhyw wefan HTML i lawr ar gyfer alinio.

Mae LF aligner yn defnyddio algorithm clyfar i benderfynu pa frawddeg sy’n mynd gyda pa un, trwy ddibynnu ar hyd y frawddeg, geiriadur a tipyn o hud a lledrith. Pendraw y peth yw nad oes angen arnoch baru segmentau gyda llaw, dim ond golygu y parau gwnaethpwyd gan y rhaglen a gwneud unrhyw gywiriadau angenrheidiol. Y rhan fwyaf o’r amser byddwch yn cael cyfieithiad peirianyddol gellir ei defnyddio heb unrhyw fewnbwn dynol. Mae paru awtomatig Hunalign yn dibynnu yn llwyr ar ansawdd y deunydd ffynhonnell (p’un ai ydych chi wedi tynnu penawdau a throednodiadau ac ati) a p’un ai mae ganddo eiriadur da neu beidio, ond mae canrannau yn y nawdegau uchel yn gyffredin (mae data geiriadur da ar gyfer 800 cyfuniad o fwy na 32 iaith yn dod wedi ei becynnu gyda’r aliniwr. Gallwch wirio yn y log i weld os yw’r data geiriadur yma wedi’i ddefnyddio ar gyfer eich aliniad). Y prif allbwn yw TMX, ond nid oes rhaid defnyddio meddalwedd sy’n gweithio gyda TMX, gall yr aliniwr gynhyrchu ffeiliau XLS ar eich rhan. Cynhyrchir ffeiliau tab delimited pob tro hefyd, addas ar gyfer defnydd gyda Apsis Xbench neu brosesu gyda arfau eraill. 

Mae LF Aligner hefyd yn cynnig rheolaeth lawn dros yr holl broses: yn y TMX, gallwch osod y dyddiad a’r amser, codau iaith, ID creawdwr, ychwanegu nodiadau at bob segment ac ati, ac mae gennych ddewisiadau addasu eang ar gyfer ffwythiannau eraill hefyd. Jest agorwch aligner_setup.txt er mwyn gweld y prif ddewisiadau gosod. 

Mae’r readme hwn yn eithaf hir... os ydych chi eisiau dechrau arni yn gyflym heb ddarllen yr holl beth, gallwch wneud hyn drwy ddilyn y camau disgrifir yn sample/howto.txt, ond mae’n debyg y dylech ddod yn ôl at y readme hwn rywbryd, yn enwedig os ydych chi yn cael trafferth â rhywbeth.  

## *** INTRO ***

LF Aligner is intended for translators who wish to create translation memories from translations made without a CAT tool or from any other text that is available in two or more languages. I wrote it to make what is probably the best open source automatic sentence aligning algorithm, Hunalign (see http://mokk.bme.hu/resources/hunalign) more convenient to use. LF Aligner also has a couple of features designed for larger-scale corpus building, such as handling huge data sets, built-in data filtering, batch mode, automatic segmentation evaluation and unattended operation.
The aligner also has other features like creating TMX files and downloading EU legislation or any other bilingual HTML webpage for alignment (see details on the web features further down).

The reason why you may want to use this simple tool instead of the flashy and complicated aligners from the big players is Hunalign. It uses a smart algorithm to determine which sentence goes with which, relying on sentence length, a dictionary and, as near as I can tell, black magic, and it does a really good job. The upshot is that you don't have to manually pair up the segments, only review the pairings and do any necessary corrections - or not even that. Most of the time you will get a very usable TM without human input.
The accuracy of Hunalign's automatic pairings depends entirely on the quality of the source material (whether you have removed page headers and footers etc.) and whether it has a good dictionary to work with, but percentages in the high nineties are common. (Reasonably good dictionary data is bundled with LF Aligner for more than 800 combinations of 32 languages. You can check the log to see if this dictionary data was used for your alignment.)
The primary output is TMX, but if you don't use TMX-compatible software, the aligner can generate xls files for you. Tab delimited txt files are always generated as well, suitable for use with Apsic Xbench or processing with other tools.

LF Aligner also gives you complete control over the whole process: in the TMX, you can set the date and time, language codes, creator ID, add notes to each segment etc., and you have extensive customisation options regarding a bunch of other features, too. Just open aligner_setup.txt to see the main setup options.

I kept adding information and this readme ended up being pretty long... if you want to get started quickly without reading the whole thing, you can do so by following the steps described in sample/howto.txt, but you should probably come back to this readme later, especially if you get stuck with something.

## *** USE ***

The folder named "sample" contains a pair of sample files and a txt with instructions on how to use the script. You can follow the instructions there to see the aligner in operation and learn the basics, and then come back to this readme for more detailed information.

The input files can be txt, doc, docx, odt, rtf, tmx, HTML, pdf and a few other formats. Always use UTF-8 encoding in your txt files. See details on preparing input files further below.

No installation is needed, just double click on LF_aligner_XXX to launch the program. A graphical or command line window will open, and prompt you for input as needed. (Note: the initial startup may be very slow on Windows. Just wait until the first prompt appears; it will show up eventually, and things will speed up from then on.) Read the prompts, type or click what you are asked to and press Enter or click Next. Any error messages will also be displayed in the same window. If something went wrong, read the error messages carefully, check the log in the scripts folder, then run the program again if you have an idea about what went wrong.
To "uninstall", just delete the aligner folder. LF Aligner makes no changes to the registry or other system settings, so the aligner folder is all there is.

It is highly advisable to create a new folder for each new alignment project, containing only the two files to be aligned, or else old files may be overwritten etc. Your project folder can be anywhere on your computer. (Note: on Windows, use only ASCII characters in file and folder names!) If you use the web features (to download and align EU legislation etc.), your files will be downloaded to the program folder.


Note on all input document formats:
The import of every "rich text" document format, i.e. everything apart from txt and (hopefully) tmx is potentially lossy.
E.g. if your pdf, html, doc, docx, rtf or other file contains tables, they are probably going to come out wrong. Tables are best handled manually, i.e. you should move each cell to a separate line for best results. Most other elements that occur in running text are handled well, but no promises, especially with pdf. Hyperlinks, special symbols, footnotes, sidenotes, page headers and generally everything other than running text with "normal characters" may not come out the way you expect them to. Txt input files are always going to be the safest, so use txt whenever you can.
See "Using your CAT to extract/segment text:" on how to get around the problem by piggybacking on your CAT tool.


Note on doc import: this is done with Antiword, which seems to work really well, although I haven't bothered testing it very much. Headers and footers are not conserved, but hidden text is. Footnotes are added to the end of the document. Pictures are represented by [pic], which the aligner subsequently deletes if it's on a line by itself.
On Windows, doc conversion should work out of the box, just launch LF Aligner and drop in your doc files. The Windows version of Antiword requires the file C:\antiword\UTF-8.txt, so this is created by the aligner. This is the only file the aligner creates or modifies outside of its own folder. (Note: disregard the "I can't find the name of your HOME directory" messages, they are of no importance.)
On non-Windows systems, you'll have to install Antiword yourself. Sudo apt-get install antiword should take care of it in Debian, Ubuntu & co - in other distros, check your package manager. If you are an OS X user, these should get you started: http://www.winfield.demon.nl/ http://antiword.darwinports.com/ 
As always, check the results; comparing the word/character numbers reported by the aligner to the word count numbers from Word is probably a good idea. Of course, txt will always be the most reliable input format, so if you want to be absolutely, 100% certain that the alignment contains the text you want it to, convert your text to txt yourself and make sure it's kosher before running the aligner.

Note on docx import: this uses docx2txt, which is bundled with LF Aligner in all versions, and it should usually work well, extracting text even from corrupted docx files. Page headers, footers and footnotes are removed - I consider that a feature, not a bug. Hidden characters are conserved, so delete them first if you don't want them in your TM.
The same caveats apply as with .doc. 

Note on rtf import: this is done with Abiword. If you're on OS X or Linux, you'll need to install Abiword yourself. In Ubuntu, you'll find it in the software centre. Also, see http://www.abisource.com/download/index.phtml
Abiword is also the aligner's last line of defence against odd input files: if you specify the generic "t" filetype and the extension is not txt, doc or docx, Abiword is used to try and convert your file to txt. It should work with Abiword's own abw files, as well as docm, odt and a couple of other file formats. You can probably install some Abiword plugins and get support for even more weird and wonderful file formats.

Notes on pdf import:
Obviously, this won't work with pdf files that contain images of scanned documents - unless they happen to be special two-layer OCRed pdf files that contain the underlying text as well as the image.
Remember: don't expect perfection. The pdf format is horrible; extracting text reliably is simply not possible with any automated method. That's just the way pdf is, there is nothing you can do about it except thank Adobe and the document's author.
There are 4 options you can try with pdf, with each producing slightly different end results. There is no best way, what's best for a given file depends on the file itself.

1) Use "Save as text" in Acrobat Reader, then resave the txt file generated by Acrobat Reader in UTF-8 and run the aligner on the txt file in pdf (p) mode
2) Run the aligner directly on the pdf files with default settings
3) Run the aligner directly on the pdf files after changing the "Pdf conversion mode" option in the setup file to n
4) Copy-paste text out of the pdf into a txt and run the aligner on that in txt (t) mode

Generally, 1), i.e. exporting to txt format in Acrobat Reader works a bit better than feeding the pdf to the aligner directly if the file has non-linear text placement, such as text in columns or tables or the margins of the page. For this reason, exporting is always recommended for pdf files. The procedure is as follows: open the pdf in Adobe Acrobat Reader, click File/Save as text. Then open the resulting txt file with Notepad, choose File/Save as and resave with UTF-8 encoding. Then just use the "p" file type in the aligner. Do NOT run the aligner in "t" mode on exported pdf files!
The built-in converter (used in options 2 and 3 above) is mainly designed to be used if you have many files to align and exporting them one by one would be too time-consuming (i.e. it's mostly designed to be used in batch mode). You can configure its behaviour with the "Pdf conversion mode" setting in setup (the "y" setting works better with tables, it makes the txt files easier to review and does a better job of keeping separate segments separated, so "y" is the default even though it does a worse job with side notes and columns).
Overall, it is a bit worse with non-linear text than exporting from Acrobat Reader. It's absolutely fine for simple running text, though... Except that page headers and footers are left in the text because it's not really possible to automatically filter them out. That's another "feature" you can thank Adobe for.
You could also try copy-pasting from the pdf into a txt file, but once you have a pdf open in Acrobat Reader, you're better off just exporting.

If your originals are in some unsupported format, either save them in .doc or .docx or copy-paste their content into Notepad (or any other text editor) and save them as TXT with UTF-8 encoding (this is not Notepad's default so you explicitly have to set UTF-8 in the "Save as" dialog). See "Using Trados to extract/segment text" for tips on possible ways to handle .ppt and generally any format your CAT is compatible with.

Remove page numbers and page headers/footers from your txt files before running the aligner (this is usually only needed if the original was a pdf). Read up on Microsoft Word's wildcard search and replace to figure out how to remove headers/footers containing a running page number with one command: accurapid.com/journal/15msw.htm
This is important, as, if you leave them in, Hunalign will diligently pair up the nicely matching page headers/footers with each other and consequently mess up the alignment of the text in between - unless page breaks are applied in a uniform manner in the originals.


Setup:

You've probably noticed the file aligner_setup.txt. This file allows you to extensively customize LF Aligner's behaviour. Just open it and change the values in [] as you see fit.

If your txt (xml, etc.) file contains tags enclosed in <> and you want to get rid of them, change the extension to html and tell the script it's an html file. Everything enclosed in <> will be deleted except for <p>, <P>, <br> and <br /> which will be converted to line breaks (and thus become segment delimiters). To enforce segment breaks, insert <p> tags (line breaks are ignored in tagged files).

The script keeps backups of the original files. Other output files: aligned_XXX.txt is the tab delimited aligned file Hunalign produces, i.e. the main output file. (The 3rd column contains the source info, and the 4th column contains the match confidence value if you enable that.) The .xls has the same content, with reviewing instructions. XXX.tmx... well, no points for guessing that one.


Tips for reviewing alignment:

If you're a Windows user, the graphical editor is the default option as of version 4.0, and it is by far the most convenient one. Some instructions are available in Help/Usage, and a little more info is given in the readme in aligner/other_tools. When you are done, make sure you quit using File/Save exit, and NOT by closing the window.

For linux/mac users, instructions on how to do a review in Excel are on worksheet 2 of the xls file generated by the aligner. A macro is provided in aligner/scripts/MergeCells.xla to speed up the process.