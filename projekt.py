import pandas as pd

otwarcie="\\begin{reg}\n"
wstep="Jeżeli odpowiedzią na "
str3="\" to dla każdego obiektu Kierunek którego pole \""
strWynikPozytywny=" zwiększ wartość pola \"waga\" kierunku o jeden. "
strWynikNegatywny=" ustaw pole active na false. "
domkniecie="\n\\end{reg}"

def _checkbox_questions():
    pass

def cos():
    pass


def prepare(df,wynik,opcja,index,pole_wartosc,wstep,wybor):
    napis = []
    napis.append(otwarcie)
    napis.append(wstep)
    napis.append(" \"")
    napis.append(df.pytanie[index])
    napis.append("\" ")
    napis.append(wybor)
    napis.append(opcja)
    napis.append(str3)
    napis.append(df.klasa[index])
    napis.append(pole_wartosc)
    napis.append(wynik)
    napis.append(domkniecie)
    return "".join(napis)


def _main():
    df=pd.read_csv('rekordy.csv')
    pole_wartosc_tak = "\" ma wartość true"
    pole_wartosc_zlozona="\" ma wartość "
    strWynikNegatywny=" ustaw pole active na false. "
    wstep_tak = "Jeżeli odpowiedzią na "
    wstep_zlozony="Jeżeli w pytaniu "
    wybor_tak=" jest \""
    wybor_zlozony="użytkownik zaznaczył odpowiedź \""
    wybor_not_checked="użytkownik nie zaznaczył odpowiedzi \""
    with open("./wynik", mode="w") as wyj:
        for index, opcja1 in enumerate(df.opcja1):
            if opcja1=="tak":
                pole_wartosc=pole_wartosc_tak
                wstep=wstep_tak
                wybor=wybor_tak
            else:
                pole_wartosc=pole_wartosc_zlozona+"\""+str(opcja1)+"\""
                wstep=wstep_zlozony
                wybor=wybor_zlozony

            opcja=df.opcja1[index]
            wynik=strWynikPozytywny
            ost=prepare(df,wynik,opcja,index,pole_wartosc,wstep,wybor)+"\n"
            wyj.write(ost)
            #not checked
            if opcja1!="tak":

                wybor=wybor_not_checked
                wynik=strWynikNegatywny
                ost = prepare(df, wynik, opcja, index, pole_wartosc, wstep, wybor) + "\n"
                wyj.write(ost)
                wynik=strWynikPozytywny
            else:
                wynik = strWynikNegatywny
            #secound option
            opcja=df.opcja2[index]
            ost=prepare(df,wynik,opcja,index,pole_wartosc,wstep,wybor)
            wyj.write(ost)



_main()
