# SSprojekts
**Mašīnu meklēšanas automatizācija, izmantojot mājaslapu ss.com un python. Autori: M. Kondratjuks, V. Kuplovs-Oginskis **
 
**Kā parādījās ideja **
Marekam vienmēr ļoti interesēja automašīnas, katru reizi kad viņam ķļuva garlaicīgi, viņš gāja uz ss.com un skatījās sev dažādas mašīnas, izvēlējās kura patīk visvairāk un ir visizdevīgākā. Vitoldam gan mašīnas tik ļoti neinteresēja, bet viņš bija iepazinies ar cilvēku, kuram viss bizness ir veidots uz mašīnu pirkšanas un pārdošanas, viņš gribēja iemācīt Vitoldam pelnīt tāpat. Taču katru dienu pavadīt daudz laika meklējot izdevīgus piedāvājumus nešķita pievilcīgi. Mums abiem parādījās doma par to, ka mašīnu meklēšanu var automatizēt.  
 
**Darba process 
**Sākumam bija jāievieto visas nepieciešamās bibliotēkas, kuras būs izmantotas kodā, ar laiku to kļuva arvien vairāk, tās visas var atrast sarakstā zemāk. Lai atvieglotu dzīvi, mūsu bilingvālajā valstī ir dota iespēja izvēlēties starp divām valodām-angļu un latviešu. Tālāk lietotājam ir dota izvēle, viņam jāievada vēlamā mašīnas marka, budžets, mašīnas izlaides gadi, ātrumkārbas veids un degvielas tips. Savāktie dati tiek ievietoti ss.com mājaslapā un sākas mašīnu atlase. Kad ir redzams saraksts no filtrētajām mašīnām, to modelis,cena, nobraukums un izlaides gads ir savākti. Izveidojas CSV fails, kurā ir izveidots saraksts no iegūtajiem datiem. Tajā pašā laikā, savāktie dati tiek apstrādāti. Sākas vidējo mērvienību aprēķins iegūtajā sarakstā - vidējā cena, vidējais nobraukums - tad arī iegūts vidējais koeficients. Lietotājam uz ekrāna parādās mašīnas numurs ar savu izrēķināto koeficientu, kā arī tas tiek salīdzināts ar kopējo vidējo koeficientu un parādās uzraksts, vai mašīna ir relatīvi dārga, vai relatīvi lēta. Beigu beigās tiek izanalizēti visi varianti un programma izdod visizdevīgāko mašīnu šajā sarakstā.  
Ps. Vidējā cena tiek aprēķināta = visu cenu summa / automašīnu skaits 
Vidējais nobraukums = visu nobraukumu summa / automašīnu skaits 
Vidējais koeficients = Vidējais nobraukums / Vidējā cena 
Atsevišķa auto koeficients = nobraukums / cena 
Diemžēl, ne viss darbojās tā, kā mēs sākumā iecerējām, tāpēc daudzas lietas projekta veidošanas gaitā bija jāmaina. Gribam izteikt pateicību S. Jurenokai un A. Jurenokam par sniegto palīdzību un padomiem. 
 
**Apraksts 
**Lietotājs palaiž programmu, tad ievada sev tīkamo mašīnas marku, tās modeli un mašīnas izlaiduma gadu, savu budžetu, ātrumkārbas veidu un degvielas tipu. Visi dati tiek ievietoti ss.com. Pēc atlases ir iegūts saraksts ar mašīnām, kuras vēlāk programma izanalizē un izdod visizdevīgāko variantu. 
 
**Uzdevums 
**Izveidot sistēmu un automatizēt visizdevīgāko mašīnu meklēšanu, iekļaujot maksimāli daudz dažādu filtru. Izmantojot mājaslapu ss.com atlasīt mašīnas ar iegūtajiem filtriem. Aprēķināt un izanalizējot mašīnu sludinājumus, izdot lietotājam visizdevīgāko variantu no visiem. Parādīt arī pārējos variantus un cik tie ir izdevīgi, vai neizdevīgi, salīdzinot ar kopējo vidējo koeficientu. 
 
 
 
**Bibliotēkas 
**Mēs izmantojām šādas bibliotēkas: 
1.  Selenium 
Ar tā palīdzību mēs varējām strādāt ar vietni ss.com un no turienes ņemt mums vajadzīgo informāciju par automašīnām. 
2. time 
Ar to mēs varam nedaudz aizkavēt laiku, lai programma paspētu izpildīt visas savas funkcijas, kā arī, lai lietotājs varētu redzēt, kas notiek. 
3. requests 
Izmantojam, lai atvērtu mājaslapu. 
4. bs4 
To izmantojām, lai savāktu nepieciešamo informāciju no HTML vietnēm. 
5. re 
Atvieglo darbu, kompilējot regulāras izteiksmes. 
6. pandas 
Tas bija nepieciešams priekš Csv faila, izveidot sarakstu, kurš veidojas atkarībā no izvēlētajiem parametriem un tiek ņemts no mājaslapas. 
7. csv 
Mēs izveidojām atsevišķu failu, kur atrodas saraksts ar mašīnām un to parametriem. 
 
**Piezīme 
**Lai kods darbotos, fails SSprojekts.py jāielādē datorā, no GitHub codespace to palaist nevarēs, jo ir izmantota selenium bibliotēka, kura neparedz sevī koda izveidi web editoros. Drošības pēc arī ielādējiet lūdzu output.csv, dažreiz bez šī faila programma mistisku iemeslu dēļ nedarbojas.

