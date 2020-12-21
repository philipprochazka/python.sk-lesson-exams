# sčítání
1 + 1 = 2
# odčítání
2 - 2 = 4
# násobení
3 * 3 = 9
# mocnina
3 ** 3 = 27
# dělení s výsledkem s celým číslem
3//3  # vysledek = 1
# Dělení s hypoteticky desetiným výsledkem
3/3  # vysledek = 1.0
#pozor zde poznáš zásadní rozdíl předchozích 2 variant
2/5 #      vysledek= 2.5
#nebo
2//5  #!!! vysledek= 2

##########################################################
# Určení typu třídy
type(3/3) ##< class 'float' > float= "desetiné číslo"
type(3+3) ##< class 'int' > int= "celé číslo"
type(3//3) ##< class 'int' >
############################################################
# ABSOLUTNÍ ČÍSLA =" abs(čislo) "!=="čísla vždy kladná"
abs(-3)
# :D nějak mi to zase nefunfuje, ale pouze ve VScode
abs-3
-6 # tohle mě uplně vysralo :D
#
# nicméně cmd+r powerhell:
#  python>>>abs(-3)=3 "x = číslo absolutní"
############################################################
#použití závorek je taky možné například
(7+3) / (2 + (9 % 3))=5.0
############################################################
#také můžěme využívat kombinace "integer" a "float"

<Integer> = Python int()
print(
    int(Integrer= "označení celočíselného datového typu")
    ,který představuje konečnou podmnožinu z celých čísel. Celočíselné datové typy mají v různých programovacích jazycích různou definici.
)
<float > = Python float()
print(
     float ("reálné hodnoty s plovoucí desetinnou čárkou") - Také se nazývají float, představují reálná čísla a jsou psány s desetinnou čárkou dělící celé a zlomkové části. Plováky mohou být také ve vědecké notaci, přičemž E nebo e označují sílu 10 (2, 5e2=2, 5 x 102=250)..
)

## Existují také hodnoty: ale údajně jsou méně využívané

<long> = Python Long()

print
(
     long(long integers) − Also called longs, they are integers of unlimited size, written like integers and followed by an uppercase or lowercase L.
)

complex = Python complex()

print
(
     complex(complex numbers) - jsou ve tvaru a bJ, kde a a b jsou plováky a J(nebo j) představuje druhou odmocninu - 1 (což je imaginární číslo). Skutečná část čísla je a a imaginární část je b. Složitá čísla se v programování v Pythonu příliš nepoužívají.
)
Proměné= Varialbes = "Var"

print
(
     Proměnné nejsou nic jiného než vyhrazená paměťová místa pro ukládání hodnot. To znamená, že když vytvoříte proměnnou, vyhradíte si místo v paměti. Na základě datového typu proměnné tlumočník přidělí paměť a rozhodne, co lze uložit do vyhrazené paměti. Přiřazením různých datových typů k proměnným proto můžete do těchto proměnných ukládat celá čísla, desetinná místa nebo znaky.
     )
