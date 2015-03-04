## Sut i ddefnyddio LF Aligner

Mae hwn yn esiampl sy’n arddangos defnydd LF aligner. Y syniad yw, gan ddarllen y txt yma a’r allbwn yn y ffenest llinell gorchymyn ei hun, byddwch yn gallu testio’r sgript a chael syniad eithaf da ynglŷn a sut mae ei ddefnyddio, hyd yn oed heb fynd drwy’r readme llawn – sydd dal yn argymhelliad gan ei fod yn cynnwys esiampl byr o ddefnydd ymarferol.   
Darparir dwy ffeil enghreifftiol, sef fersiynau Saesneg a Sbaeneg o Gytundeb Maastricht wedi eu cymryd o ffeiliau pdf sydd ar gael yn http://bookshop.europa.eu/is-bin/INTERSHOP.enfinity/WFS/EU-Bookshop-Site/en_GB/-/EUR/ViewPublication-Start?PublicationKey=FXAC08115

Wnes i allforio y  pdfs gan ddefnyddio File/Cadw fel testun yn Acrobat reader, dileu y rhannau nad oedd eu heisiau ac yna ei ail gadw gyda amgodio UTF-8. Ni wnaethpwyd unrhyw rhag-brosesu, dim hyd yn oed tynnu penawdau tudalennau. Os wnewch chi agor y ffeiliau, byddwch yn gweld eu bod yn llanast: mae toriad llinell ar ôl pob gair. Ond nid yw hyn yn broblem; gyda’r gosodiadau cywir, bydd yr aliniwr yn cywiro hyn.  
Rhedeg yr aliniwr:
Cliciwch dwywaith ar aligner/LF_aligner_XXX. Dylai ffenest llinell orchymyn ymddangos, ac, ar ôl eiliad neu ddwy, gofyn i chi ddewis math o ffeil. (Os nad ydych chi ar Windows a dydych chi ddim yn gweld ffenest derfynell drwy glicio dwywaith ar ffeil yr aliniwr, agorwch ffenest derfynell gyda llaw, teipiwch y gair "perl" a bwlch, llusgwch a gollyngwch y ffeil yn y ffenest a gwasgwch enter). Wrth i’r ffeiliau enghreifftiol gael eu mewnforio o’r pdf, teipiwch "p" (heb y dyfynodau) er mwyn dewis y math o ffeil pdf a gwasgwch enter. Nodwch: mewn defnydd pob dydd, mae’n debyg byddwch angen y “t” cyffredin (ar gyfer ffeiliau "testun", h.y.. txt, doc, docx neu ffeiliau rtf) yn mwy aml na "p".

Iaith ffeil 1 - "en". Iaith ffeil 2 - "es".

Pori (Windows) neu llusgo a gollwng y ffeiliau mewnbwn.

Segmentu testun - "y". Dylai’r adroddiad ddangos bod y ddau destun wedi cael eu hollti mewn i 480 o frawddegau o’r ~40 paragraff gwreiddiol.

Dychwelyd - "n".

Nawr dylech weld adroddiad alinio. Mae’r dau rif (480 a 479) yn agos iawn at eu gilydd, sy’n arwydd da iawn. Fel arfer, gallwch ddisgwyl alinio dibynadwy iawn (ac felly cael dim ond dipyn bach o gywiro gyda llaw i’w wneud) os bydd y ddau rif o fewn nifer bach o % o’u gilydd.  Mater pwysig arall yw gwerth ansawdd, 0.876 yn fan hyn. Mae hynny hefyd yn dda iawn; mae unrhyw beth dros 0.5 yn addawol.

Cleanup – eich dewis chi, rwy’n dewis "y" bob tro.

Arolygu: "x". Bydd taenlen xls yn agor, bydd yn caniatáu i chi adolygu yr awto-aliniad. Gwelwch gyfarwyddiadau yn yr xls ei hun. Caewch yr xls a’r txt bydd hefyd wedi ei agor. 

Creu TMX - "y".

Cod iaith 1 - "EN-GB" Cod iaith 2 - "ES-ES"

Dyddiad – gadewch yn wag a gwasgwch Enter.

ID Creawdwr – gadewch yn wag a gwasgwch Enter.

Nodyn – gadewch yn wag a gwasgwch Enter.

Gwasgwch enter i adael yr aliniwr.

Nawr dylai fod gennych TMX o’r enw en_es.tmx yn y ffolder enghreifftiau (sample). Mewnforiwch hwn i mewn i TM newydd gan ddefnyddio arf CAT o’ch dewis. 

Nodwch: unwaith rydych wedi dysgu y materion sylfaenol, agorwch LF_aligner_setup.txt a cymerwch olwg ar y dewisiadau addasu a’r ffwythiannau ar gael yn y fan honno. 

## How to use LF Aligner

This is an example that illustrates the use of LF aligner. The idea is that by reading this txt and the output in the command line window itself, you can test the script and get a reasonably good idea of how to use it, even without going through the full readme - which is still recommended as it contains a lot more information than this short example of practical use.

Two sample files are provided, namely the English and Spanish versions of the Maastricht Treaty taken from pdf files available at http://bookshop.europa.eu/is-bin/INTERSHOP.enfinity/WFS/EU-Bookshop-Site/en_GB/-/EUR/ViewPublication-Start?PublicationKey=FXAC08115

I exported the pdfs using File/Save as text in Acrobat reader, deleted the unwanted parts and resaved in UTF-8 encoding. No other preprocessing was done, I didn't even bother removing the page headers. If you open the files, you can see they are a mess: there is a line break after every word. This is not a problem though; with the right settings, the aligner corrects this.

Running the aligner:

Double click on aligner/LF_aligner_XXX. A command line window should appear, and, after a good couple of seconds, prompt you to choose a file type. (If you're not on Windows and you get no terminal window by double clicking the aligner file, open a terminal window manually, type the word "perl" and a space, drag and drop the file in the window and press enter). 
As the sample files are exported from pdf, type "p" (without the quotes) to choose the pdf filetype and press enter.
Note: in everyday use, you'll probably need the generic "t" (for "text" files, i.e. txt, doc, docx or rtf files) more often than "p".

Language of file 1 - "en".
Language of file 2 - "es".

Browse (Windows) or drag and drop the input files.

Segment text - "y". The report should show that both texts were chopped up into about 480 sentences from the original ~40 paragraphs.

Revert - "n".

Now you should get an alignment report. The two numbers (480 and 479) are very close to each other, which is a very good sign. Usually, you can expect a very reliable automatic alignment (and thus have little or no manual correction to do) if the two numbers are within a couple of % of each other.
The other important bit is the quality value, 0.876 in this case. That's also very good; anything over 0.5 is promising.

Cleanup - as you wish, I always choose "y".

Review: "x". An xls spreadsheet will open, allowing you to review the autoalignment. See instructions in the xls itself.
Close the xls and the txt that will also be opened.

Create TMX - "y".

Language code 1 - "EN-GB"
Language code 2 - "ES-ES"

Date - leave blank and just press Enter.

Creator ID - leave blank and just press Enter.

Note - leave blank and just press Enter.

Press enter to quit the aligner.

Now you should have a TMX named en_es.tmx in the sample folder. Import it into a new TM with your CAT tool of choice as a test.

Note: once you have learned the basics, open LF_aligner_setup.txt and check the customization options and features available there.
