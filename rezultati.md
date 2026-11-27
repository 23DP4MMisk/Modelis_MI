# Rezultāti

## 1. Kas ir šie dati un no kurienes tie nāk?
Dati ir "Heart Disease" datu kopas Cleveland daļa no UCI Machine Learning Repository
(https://archive.ics.uci.edu/dataset/45/heart+disease). Katra rinda ir viens pacients,
kolonnas ir medicīniski rādītāji (vecums, dzimums, holesterīns, asinsspiediens, pulss u.c.).
Sākumā bija 303 rindas un 14 kolonnas.

## 2. Kas ar datiem bija nepareizi un ko es izdarīju?
- Kolonnās ca un thal trūkstošās vērtības bija ierakstītas kā "?", tāpēc šīs kolonnas
  nolasījās kā teksts, nevis skaitļi.
- Rindas sākumā: 303. Dublikāti: 0 (pārbaudīju, neviena nebija).
- Izmestas 4 rindas, jo trūka ca vērtības, un 2 rindas, jo trūka thal vērtības.
  Izmetu tās, nevis aizpildīju, jo to ir tikai 6 no 303.
- Rindas beigās: 297.
- Mērķa kolonnu num (0-4) pārveidoju par 0/1 (0 = nav slimības, 1 = ir slimība).

## 3. Ko modelis prognozē un cik labi?
Modelis (Random Forest) prognozē, vai pacientam ir sirds slimība, pēc 13 medicīniskiem rādītājiem.
Precizitāte testā: 0,867 (52 no 60 pareizi), bāzes līnija: 0,533, starpība: +0,333 (apmēram +33 procentpunkti).
Bāzes līnija ir modelis, kas vienmēr prognozē biežāko klasi (0 = nav slimības).

Starpība ir liela, un visticamāk tā nav nejaušība: ar 60 testa rindām precizitātes nenoteiktība
ir aptuveni ±9 procentpunkti (aptuvenais 95% intervāls 0,78–0,95), un bāzes līnija 0,533 šajā
intervālā neietilpst. Tomēr tests ir mazs, un viena kļūda maina precizitāti par ~1,7 procentpunktiem,
tāpēc precīzs skaitlis nav. Turklāt rezultāts ir no viena dalījuma (random_state=42), un citā dalījumā skaitļi var atšķirties.

## 4. Divas svarīgākās kolonnas
Svarīgākās kolonnas: thallija_tests (0,135) un sāpju_tips (0,134).
thallija_tests ir thallija testa rezultāts (3 = normāls, 6 = fiksēts defekts, 7 = atgriezenisks defekts),
sāpju_tips ir krūšu sāpju tips. Abas ir loģiskas: thallija tests tieši rāda sirds muskuļa asinsapgādi,
un sāpju tips ir klasisks slimības simptoms.
Piezīme: asinsvadu_skaits nav starp divām svarīgākajām, tas ir 5. vietā (0,096). Svarīgums rāda, ko modelis
izmantoja prognozēs, nevis to, ka kolonna izraisa slimību.

## 5. Viena kļūdaina rinda
```
    vecums  dzimums  sāpju_tips  asinsspiediens  holesterīns  cukurs_tukšā_dūšā  ekg_rezultāts  maks_pulss  sāpes_slodzē  st_depresija  st_slīpums  asinsvadu_skaits  thallija_tests  patiesā_slimība  modeļa_prognoze
66     60.0      1.0         3.0           140.0        185.0                0.0            2.0       155.0           0.0           3.0         2.0                0.0             3.0              1.0              0.0
```
Patiesā vērtība: 1 (ir slimība), modelis nosauca: 0 (nav slimības).

Šī ir kļūda, kas ir bīstamākā: slimība palika nepamanīta. Pacients izskatījās vesels pēc
galvenajām kolonnām: thallija_tests = 3 (normāls) un asinsvadu_skaits = 0. Datu kopā 79% veselo pacientu ir thallija_tests = 3,
un 81% veselo ir asinsvadu_skaits = 0. Taču st_depresija = 3,0 (ST depresija pēc slodzes) ir neparasti augsta
vērtība: starp veseliem pacientiem tāda ir tikai 2%, starp slimiem 26%. Modelis, iespējams,
nepietiekami svēra šo rādītāju.

## 6. Ko ar šo modeli NEDRĪKST darīt?
Modeli nedrīkst izmantot reālai pacientu diagnostikai (piemēram, lai klīnikā izlemtu,
vai cilvēkam ir sirds slimība), jo apmācīts uz 237 pacientiem un testēts uz 60 no 297 rindām
(visi no vienas klīnikas), un kļūdas gadījumā slimību var palaist garām. Šajā testā 5 no 8 kļūdām
ir tieši šāds gadījums: slims pacients prognozēts kā vesels.

## Pašvērtējums
Izdevās: datu tīrīšana ir pārbaudāma (303 − 6 = 297), un modeļa rezultāts ir salīdzināts ar
vienkāršu bāzes līniju, nevis vērtēts vien pēc precizitātes.
Neizdevās: tests ir tikai 60 rindas, tāpēc precizitāte ir nestabila.
Nākamreiz: izmantotu cross-validation, pārbaudītu slimo pacientu atpazīšanu (recall) atsevišķi, nevis
tikai kopējo precizitāti, un thal un cp kā kategoriskus mainīgos, nevis skaitļus.
