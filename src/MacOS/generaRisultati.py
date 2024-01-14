def generaRisultati(squadre):
    squadreFinite = [None for i in range(len(squadre))] # Inizializziamo l'array, così da non avere problemi di assegnazione dopo
    for i in range(len(squadre)):
        squadraPrint = []
        for el in squadre[i]:
            if 6 <= el['eta'] <= 8:
                squadraPrint.append("{}, {}".format(el['parrocchia'], '6-8 anni'))
            elif 9 <= el['eta'] <= 10:
                squadraPrint.append("{}, {}".format(el['parrocchia'], '9-10 anni'))
            elif 11 <= el['eta'] <= 12:
                squadraPrint.append("{}, {}".format(el['parrocchia'], '11-12 anni'))
            else:
                squadraPrint.append("{}, {}".format(el['parrocchia'], '13 anni'))
            
        # A questo punto è sufficiente usare la nuova lista squadreFinite
        # per contare gli elementi ripetuti.
        squadreFinite[i] = dict()
        for el in squadraPrint:
            if el in squadreFinite[i]:
                squadreFinite[i][el] += 1
            else:
                squadreFinite[i][el] = 1
        
    # In teoria così dovrebbe funzionare bene
    # VA BENE.
    testo = ''
    for i in range(len(squadreFinite)):
        testo += "Squadra {}:\n\n".format(i+1)
        for el in squadreFinite[i]:
            numero = squadreFinite[i][el]
            if numero == 1:
                testo += "\t1 bambino di {}\n".format(el)
            else:
                testo += "\t{} bambini di {}\n".format(numero, el)
        testo += '\n\n'
    return testo