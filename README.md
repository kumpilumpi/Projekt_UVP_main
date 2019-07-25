# Projekt_UVP
## The ultimate game

## Ideja
Igro sem videl nekoč nekje na internetu, vendar se nespomnim več spletnega naslova oz. resničnega imena igre. Se iskreno zahvaljujem za idejo tistemu, ki se je tega spomnil.

## Pravila
Igra je v osnovi precej bolj zakomplicirana veerzija igre tri v vrsto. 
Igralca igrata v mrežo velikosti 9x9, ki je razdeljena na 9 manjših mrež velikosti 3x3 tako, da te manjše mreže tvorijo 9 različnih polj za igro tri v vrsto. Manjše mreže so razporejene tako, da tvorijo eno veliko mrežo za tri v vrsto. Igro zmagaš, ko osvojiš 3 male mreže, ki so na veliki mreži v vrsti.
Vsa stvar se malo zakomplicira s tem kam igralec lahko meče. Prvi igralec lahko naredi svojo potezo na katerokoli mesto v katerikoli mali mreži. Vse naslednje poteze pa se igra po naslednjem pravilu. Glede na relativno lokacijo zadnje poteze v malo mrežo je določena naslednja mala mreža. Tako naprimer, če se odigra poteza v levi zgornji kot male mreže, se naslednja poteza odigra v levo zgornjo malo mrežo. Če se odigra poteza nato v sredino leve zgornje male mreže se igra naslenje v sredino velike mreže. In tako naprej. Če pa je mala mreža v katero bi moral igrati naslednji igralec že zasedena, potlej se ponovno lahko igra v katerokoli malo mrežo na katerokoli mesto, seveda ne že zasedeno.

## Sintaksa
V igri igralec določi mesto svoje poteze s tremi števili 1 pove lokacijo male mreže, ki so razporejene in označene tako kot telefonska številčnica. Drugo število pove vrsto 1,2,3 in zadnje stolpec ponovno 1,2,3. Obe vrst in stolpec določata mesti v mali mreži.

## License
[MIT](https://choosealicense.com/licenses/mit/)
