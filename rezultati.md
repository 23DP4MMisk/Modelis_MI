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
Precizitāte testā: <X>, bāzes līnija: <Y>, starpība: <Z>.
<Pateikt, vai starpība ir būtiska. Atcerēties, ka tests ir tikai 60 rindas, tāpēc viena
kļūda maina precizitāti par ~1,7 procentpunktiem.>

## 4. Divas svarīgākās kolonnas
Svarīgākās kolonnas: <kolonna 1> un <kolonna 2>.
<Vai tas ir loģiski? Piemēram, thal (asinsrites defekts) un ca (sašaurināto asinsvadu skaits)
tieši raksturo sirds asinsvadu stāvokli, tāpēc tas ir loģiski. Pārrakstīt savā vārdā pēc
sava rezultāta.>

## 5. Viena kļūdaina rinda
<Ielīmēt rindu no izvades.>
Patiesā vērtība: <...>, modelis nosauca: <...>.
<Paskaidrot, kāpēc kļūdījās: piemēram, rādītāji bija pierobežā, pacients izskatījās
"vesels" pēc svarīgākajām kolonnām, tāpat kā tipiski veselie pacienti u.tml.>

## 6. Ko ar šo modeli NEDRĪKST darīt?
Modeli nedrīkst izmantot reālai pacientu diagnostikai (piemēram, lai klīnikā izlemtu,
vai cilvēkam ir sirds slimība), jo apmācīts tikai uz 297 cilvēkiem no vienas klīnikas,
testēts uz 60 rindām, un kļūdas gadījumā slimību var palaist garām.

## Pašvērtējums
<Trīs teikumi: kas izdevās. Kas neizdevās. Ko nākamreiz darītu citādi.>