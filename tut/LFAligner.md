# LF Aligner

## Cyflwyniad
Bwriedir LF Aligner at ddefnydd cyfieithwyr sydd eisiau creu atgofion cyfieithu o 
gyfieithiadau a grëwyd heb arf CAT neu o unrhyw destun arall sydd ar gael mewn 
dwy neu fwy iaith. Ysgrifennwyd y rhaglen er mwyn gwneud yr algorithm alinio brawddegau 
awtomatig, Hunalign, ([gwelwch http://mokk.bme.hu/resources/hunalign](http://mokk.bme.hu/resources/hunalign)) 
yn haws i’w defnyddio. 

Mae gan LF Aligner hefyd nodweddion a’u dyluniwyd ar gyfer adeiladu corpora ar raddfa mawr, 
gan gynnwys y gallu i drin setiau data enfawr, hidlo data integredig, modd swp, 
segmentu awtomatig a gweithredu heb gymorth. 

Mae gan yr aliniwr hefyd nodweddion eraill fel creu ffeiliau TMX a llwytho rheolau yr 
Undeb Ewropeaidd neu unrhyw wefan HTML i lawr ar gyfer alinio.

Mae LF aligner yn defnyddio algorithm clyfar i benderfynu pa frawddeg sy’n mynd 
gyda pa un, trwy ddibynnu ar hyd y frawddeg, geiriadur a tipyn o hud a lledrith. 

Pendraw y peth yw nad oes angen arnoch baru segmentau gyda llaw, dim ond golygu y 
parau gwnaethpwyd gan y rhaglen a gwneud unrhyw gywiriadau angenrheidiol. Y rhan fwyaf 
o’r amser byddwch yn cael cyfieithiad peirianyddol gellir ei defnyddio heb unrhyw 
fewnbwn dynol. Mae paru awtomatig Hunalign yn dibynnu yn llwyr ar ansawdd y deunydd 
ffynhonnell (p’un ai ydych chi wedi tynnu penawdau a throednodiadau ac ati) a p’un 
ai mae ganddo eiriadur da neu beidio, ond mae canrannau yn y nawdegau uchel yn gyffredin 
(mae data geiriadur da ar gyfer 800 cyfuniad o fwy na 32 iaith yn dod wedi ei becynnu 
gyda’r aliniwr. Gallwch wirio yn y log i weld os yw’r data geiriadur yma wedi’i ddefnyddio 
ar gyfer eich aliniad). 

Y prif allbwn yw TMX, ond nid oes rhaid defnyddio meddalwedd sy’n gweithio gyda TMX, 
gall yr aliniwr gynhyrchu ffeiliau XLS ar eich rhan. Cynhyrchir ffeiliau tab delimited 
pob tro hefyd, addas ar gyfer defnydd gyda Apsis Xbench neu brosesu gyda arfau eraill.

Mae LF Aligner hefyd yn cynnig rheolaeth lawn dros yr holl broses: yn y TMX, gallwch osod 
y dyddiad a’r amser, codau iaith, ID creawdwr, ychwanegu nodiadau at bob segment ac ati, 
ac mae gennych ddewisiadau addasu eang ar gyfer ffwythiannau eraill hefyd. Jest agorwch 
aligner_setup.txt er mwyn gweld y prif ddewisiadau gosod.

Mae’r readme hwn yn eithaf hir... os ydych chi eisiau dechrau arni yn gyflym heb ddarllen yr 
holl beth, gallwch wneud hyn drwy ddilyn y camau disgrifir yn sample/howto.txt, ond mae’n 
debyg y dylech ddod yn ôl at y readme hwn rywbryd, yn enwedig os ydych chi yn cael 
trafferth â rhywbeth.  

## DEFNYDD 
Mae’r ffolder o’r enw “sample” yn cynnwys pâr o ffeiliau enghreifftiol a txt gyda 
chyfarwyddiadau ar sut i ddefnyddio’r sgript. Gallwch ddilyn y cyfarwyddiadau yma 
er mwyn gweld yr aliniwr yn gweithio a dysgu y materion sylfaenol, ac wedyn dod 
yn ôl at y readme yma am fwy o wybodaeth.

Gall y ffeiliau mewnbwn fod yn txt, doc, docx, odt, rtf, tmx, HTML, pdf a rhai 
fformatau eraill. Gwnewch yn siŵr eich bod chi’n defnyddio amgodio UTF ar eich 
ffeiliau txt bob tro. 

Gwelwch fanylion ar baratoi ffeiliau mewnbwn yn bellach ymlaen isod.

Does dim angen gosod y rhaglen o gwbl, dim ond clicio dwywaith ar LF_aligner_XXX 
er mwyn dechrau’r rhaglen. Bydd ffenest raffigol neu llinell orchymyn yn agor, 
a bydd prompt yn gofyn am eich mewnbwn yn ôl yr angen. 

(Nodyn: gall y broses ddechrau am y tro cyntaf fod yn araf iawn yn Windows. Jest 
agorwch tan fod y prompt cyntaf yn ymddangos; bydd yn ymddangos ar ôl saib, a bydd 
pethau yn cyflymu o hynny allan).

Darllenwch y promptiau, teipiwch a chliciwch pan gofynnir i chi wneud hynny a gwasgwch 
Enter neu cliciwch Next. Bydd unrhyw negeseuon gwall yn cael eu dangos yn yr un ffenest. 
Os aeth rhywbeth yn anghywir, darllenwch y negeseuon gwall yn ofalus, gwiriwch y log yn 
y ffolder sgriptiau, a wedyn rhedwch y rhaglen eto os nad oes gennych unrhyw syniad 
pam aeth pethau o’i le. Er mwyn tynnu y rhaglen, dilëwch ffolder yr aliniwr. Nid yw 
LF Aligner yn gwneud unrhyw newidiadau i’r gofrestrfa na unrhyw osodiadau system eraill, 
felly dim ond y ffolder sy’n cynnwys yr aliniwr sydd. 

Mae’n cyngor da iawn creu ffolder newydd ar gyfer pob project alinio newydd, sydd yn 
cynnwys dim ond y dwy ffeil bydd yn cael eu alinio, neu mae’n bosib y gall hen ffeiliau 
gael eu trosysgrifo ac ati. Gall eich ffolder project fod unrhyw le ar eich cyfrifiadur. 

(Nodyn: ar Windows, gwnewch yn sicr mai nodau ASCII yn unig byddwch yn eu defnyddio ar 
gyfer enwau ffeiliau a ffolderi!) os byddwch yn defnyddio nodweddion gwe (er mwyn llwytho 
i lawr ac alinio deddfwriaeth yr UE ac ati), bydd eich ffeiliau yn cael eu llwytho i lawr 
i ffolder y rhaglen.    

### Nodyn ar pob fformat dogfen mewnbwn: 
mae gan mewnforio unrhyw ddogfen “rich text”, h.y. unrhyw
beth ond am txt a (gobeithio) tmx y potensial i fod yn ‘lossy’ (h.y y gall rai o nodweddion y 
ffeil wreiddiol gael eu colli). Er enghraifft, os yw eich pdf, html, doc, docx, rtf neu unrhyw 
ffeil arall yn cynnwys tablau, mae’n debygol y bydden nhw yn dod allan yn anghywir. Mae’n well 
delio gyda tablau a llaw, h.y. dylech symud pob cell i linell ar wahân ar gyfer y canlyniadau 
gorau. Mae’r rhan fwyaf o elfennau sy’n ymddangos mewn testun a redir yn gweithio yn dda, ond 
dim addewidion, yn enwedig o ran pdf. Gall hypergysylltiadau, symbolau arbennig, troednodiadau, 
penynnau ac yn gyffredinol pob dim heblaw am redeg testun gyda “nodau arferol” arwain at ganlyniad 
nad oeddech yn ei ddisgwyl. Ffeiliau mewnbwn txt bydd wastad y fformat mwyaf saff, felly defnyddiwch 
txt pob tro lle mae’n bosib gwneud hyn.   

### Nodyn ar fewnforio dogfennau: 
gwneir hyn gyda Antiword, sy’n gweithio yn eithaf da, er nad ydyw wedi 
ei destio llawer. Nid yw pennau na throednodiadau yn cael eu cadw, ond bydd testun cudd yn. 
Ychwanegir troednodiadau at diwedd y ddogfen. Cynrychiolir lluniau gan [pic], a bydd yr aliniwr 
yn dileu hyn os mae ar linell ar ben ei hun. Ar Windows, dylai trosi dogfennau weithio yn syth, 
jest dechreuwch LF Aligner a gollyngwch eich ffeiliau doc i mewn. Mae’r fersiwn Windows o Antiword 
angen y ffeil C:\antiword\UTF-8.txt, felly fe grëir hwn gan yr aliniwr. Dyma’r unig ffeil mae’r aliniwr 
yn creu neu yn addasu tu allan i’w ffolder ei hun. 

(Nodyn: anwybyddwch y negeseuon sy’n dweud “ni allaf ffeindio enw eich cyfeiriadur CARTREF”, nid ydynt yn bwysig.)

### Nodyn ar mewnforio docx: 
mae hyn yn defnyddio docx2txt, a’i becynnir gyda LF Aliniwr ym mhob fersiwn, ac mae’n 
gweithio yn eithaf da, ac yn echdynnu testun hyd yn oed o ffeiliau docx llwgr. 

Tynnir penynnau tudalen, troedynnau, troednodiadau – gellir ystyried hyn yn nodwedd ddefnyddiol, a nid yn wall. 
Caiff nodau cudd eu cadw, felly dilëwch nhw yn gyntaf os nad ydych chi eu heisiau yn eich peiriant cyfieithu. 
Mae’r cyngor yma hefyd yn wir ar gyfer ffeiliau .doc. 

### Nodyn ar fewnforio rtf: 
gwneir hyn gyda Abiword. Os ydych yn defnyddio OS X neu Linux, bydd angen i chi osod 
Abiword eich hun. Yn Ubuntu, gallwch ei ddarganfod yn y ganolfan feddalwedd. Hefyd, 
gwelwch [http://www.abisource.com/download/index.phtml](http://www.abisource.com/download/index.phtml). 
Abiword yw amddiffyniad gorau yr aliniwr yn erbyn ffeiliau mewnbwn rhyfedd: os wnewch chi yn enwi y math ffeil 
cyffredin “t” ac mae estyniad eich ffeil yn rhywbeth gwahanol i txt, doc neu docx, defnyddir Abiword er mwyn 
ceisio trosi eich ffeil mewn i un txt. Dylai hyn weithio gyda ffeiliau abw Abiword ei hunan, yn ogystal a docm, 
odt a mwy o fformatau ffeiliau eraill sy’n bodoli. Mae’n bosib y byddech yn gallu gosod rhai o ategion Abiworld 
a derbyn cymorth ar gyfer hyd yn oed mwy o fformatau egsotig. 

### Nodiadau ar fewnforio pdf: 
Yn amlwg, ni fydd y broses yma yn gweithio gyda ffeiliau pdf sy’n cynnwys delweddau 
sydd wedi eu sganio o ddogfennau – heblaw eu bod nhw’n digwydd bod yn ffeiliau pdf OCRed dwy haen sy’n cynnwys 
y testun waelodol yn ogystal a’r ddelwedd. Mae’r fformat pdf yn un lletchwith; mae echdynnu testun mewn modd 
dibynadwy yn amhosib gyda unrhyw ddull awtomatig. Dyna’r broblem gyda pdf, a does prin dim gallwch wneud am hyn. 
Mae 4 opsiwn gallech drio gyda’r pdf, gyda phob un yn cynnig canlyniad diwedd ychydig yn wahanol. 
Does dim un ffordd sydd well, mae’r dull gorau ar gyfer unrhyw ffeil yn dibynnu ar natur y ffeil ei hun. 

 1.	Defnyddiwch “cadw fel testun” yn Acrobat Reader, wedyn ail gadwch y ffeil txt a gynhyrchwyd gan Acrobar Reader mewn UTF-8 a rhedwch yr aliniwr ar y ffeil testun mewn modd pdf (p)  
 2.	Rhedwch yr aliniwr yn uniongyrchol ar y ffeiliau pdf gyda’r gosodiadau rhagosodedig 
 3.	Rhedwch yr aliniwr yn uniongyrchol ar y ffeiliau pdf ar ôl newid yr opsiwn “modd trosi pdf” yn y ffeil osodiadau i n
 4.	Copïwch a gludwch destun o’r pdf i mewn i txt a rhedwch yr aliniwr arno yn modd txt (t)
 
Yn gyffredinol, mae (1) h.y. mewnforio i fformat txt yn Acrobat Reader yn gweithio rhywfaint yn well na cheisio
bwydo y pdf yn uniongyrchol i’r aliniwr os oes gan y ffeil leoliad testun aflinol, megis testun mewn colofnau neu 
dablau neu ar ymylon y dudalen. Oherwydd hyn, cynghorir mewnforio bob tro ar gyfer ffeiliau pdf. Mae’r weithdrefn 
fel a ganlyn: agorwch y pdf yn Adobe Acrobat Reader, liciwch File/Cadw fel testun. Yna agorwch y ffeil ganlynol 
gyda Notepad, dewiswch  Ffeil/Cadw fel ac ail-gadwch gyda amgodio UTF-8. Yna defnyddiwch y math ffeil “p” yn yr 
aliniwr. Peidiwch a rhedeg yr aliniwr yn y modd “t” ar ffeiliau pdf wedi eu allforio! Mae’r nodwedd trosi 
sy’n rhan o’r rhaglen (a ddefnyddiwyd yn  opsiynau 2 a 3 uchod) wedi ei ddylunio ar gyfer sefyllfaoedd lle 
mae gennych nifer fawr o ffeiliau i’w alinio a lle byddai eu allforio yn cymryd gormod o amser (h.y. mae wedi 
ei greu ar gyfer modd swp). Gallwch addasu ei ymddygiad drwy’r gosodiad “modd trosi pdf” yn y dudalen gysodi 
((mae’r gosodiad “y” yn gweithio yn well gyda thablau, ac mae’n gwneud ffeiliau txt yn haws i’w adolygu ac mae’n 
well am gadw’r segmentau sydd ar wahân, ar wahân, felly  “y” yw’r dewis rhagosodedig er ei fod yn gwneud 
jobyn gwaeth gyda nodiadau ochr a colofnau). Ar y cyfan, mae tipyn yn waeth gyda testun aflinol na allforio o 
Acrobat Reader. Mae’n hollol dderbyniol ar gyfer rhedeg testun, er fod penynnau a troedynnau yn cael eu gadael 
yn y testun am dad yw hi wir yn bosib eu hidlo allan yn awtomatig. Byddai hefyd yn bosib copïo a gludo o’r pdf 
i mewn i ffeil destun, ond unwaith bod gennych ffeil pdf wedi ei hagor yn Acrobat Reader, byddai’n well i chi 
jest ei fewnforio.   

Os yw eich ffeiliau gwreiddiol mewn fformat heb gefnogaeth, gallwch unai eu cadw nhw mewn .doc neu .docx neu copïo a 
gludo eu cynnwys i mewn i Notepad (neu unrhyw olygydd testun arall) a’u cadw nhw fel TXT gyda amgodio UTF-8 
(nid gosodiad rhagosodedig Notepad yw hyn, felly mae’n rhaid i chi osod UTF-8 yn y dialog “Cadw Fel”. 
Gwelwch "Defnyddio Trados er mwyn/echdynnu segmentu testun" ar gyfer cymorth ynglŷn a sut mae defnyddio .ppt ac 
unrhyw fformat yn gyffredinol mae eich CAT yn gyfarwydd ag ef. 

Tynnwch rifau tudalen a penynnau a troedynnau o’ch ffeiliau txt cyn rhedeg yr aliniwr (mae angen hyn fel arfer 
dim ond os oedd y gwreiddiol yn pdf). Darllenwch mwy ynglŷn a nodwedd chwilio a disodli wildcat Microsoft Word 
i weld sut mae tynnu penynnau a troedynnau sy’n cynnwys rhifau tudalen sy’n rhedeg gan ddefnyddio un gorchymyn: 
[accurapid.com/journal/15msw.htm](http://accurapid.com/journal/15msw.htm). Mae hyn yn bwysig, oherwydd os byddwch 
yn gadael rhain i mewn, bydd hunalign yn paru y penynnau a throedynnau sy’n matsio gyda’u gilydd, fydd yn gwneud 
llanast o aliniad y testunau sydd rhyngddyn nhw – heblaw bod toriadau tudalen yn cael eu gosod mewn dull unffurf 
yn y dogfennau gwreiddiol. 

### Cysodi:
Mae’n debyg eich bod chi wedi sylwi ar y ffeil aligner_setup.txt. Mae’r ffeil yma yn caniatáu i chi addasu ymddygiad 
LF Aligner. Agorwch y ffeil a newidiwch y gwerthoedd yn y [] fel y mynnwch. 

Os yw eich ffeil txt (xml ac ati) yn cynnwys tagiau wedi eu amgáu ac rydych chi eisiau cael gwared arnyn nhw, newidiwch
yr estyniad i html a dywedwch wrth y sgript ei fod yn ffeil html. Caiff pob dim oddi mewn ei ddileu heblaw am , , bydd 
yn cael eu trosi yn doriadau llinellau (ac felly yn troi i mewn i amffinyddion segmentau). Er mwyn gorfodi toriadau 
segmentau, gosodwch tagiau (anwybyddir toriadau llinell mewn ffeiliau sydd wedi eu tagio). 

Mae’r sgript yn cadw ffeiliau wrth gefn o’r ffeiliau gwreiddiol. 

### Ffeiliau allbwn eraill: 
aligned_XXX.txt yw’r ffeil wedi’i alinio wedi ei amffinio gan dabiau y mae Hunalign yn ei 
gynhyrchu, h.y. y prif ffeil allbwn. (Bydd y drydedd golofn yn cynnwys y wybodaeth ffynhonnell, a’r bedwaredd 
golofn yn cynnwys y gwerth hyder cydweddu os byddwch chi’n galluogi hwnnw). Mae gan .xls yr un cynnwys, yn ogystal 
a cyfarwyddiadau adolygu. Dylai XXX.tmx fod yn amlwg.

### Cymorth ar gyfer adolygu yr aliniad
Os mai defnyddiwr Windows ydych chi, dylai’r golygydd raffigol fod y dewis rhagosodedig o fersiwn 4.0. ymlaen, a 
dyma’r dewis mwyaf hwylus o bellffordd. Mae rhai cyfarwyddiadau ar gael yn Help/Usage, ac mae mwy o wybodaeth ar 
gael yn y readme yn aligner/other_tools. 

Pan rydych wedi gorffen, gwnewch yn sicr eich bod chi’n gadael y rhaglen gan ddefnyddio File/Save exit, a nid 
drwy gau y ffenest. 

Ar gyfer defnyddwyr Linux/a Mac, mae cyfarwyddiadau ar sut i adolygiad yn Excel ar daenlen 2 o’r ffeil xls a 
gynhyrchwyd gan yr aliniwr. Darparir macro yn aligner/scripts/MergeCells.xla er mwyn cyflymu y broses.

