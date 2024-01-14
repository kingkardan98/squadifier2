def suddividi_bambini(bambini, numero_squadre):
    # Inizializza le squadre
    squadre = [[] for _ in range(numero_squadre)]

    # Assegna iterativamente i bambini alle squadre in modo ciclico
    for i, bambino in enumerate(sorted(bambini, key=lambda x: (x['eta'], -peso_parrocchia_eta(x, squadre)))):
        squadre[i % numero_squadre].append(bambino)

    # Bilancia le squadre per età
    squadre = bilancia_squadre(squadre)

    return squadre

def bilancia_squadre(squadre):
    # Ordina le squadre in base alla differenza di età massima
    squadre_ordinate = sorted(squadre, key=lambda squadra: sbilanciamento_squadra(squadra))
    
    # Ridistribuisci i bambini in base alla differenza di età
    squadre_bilanciate = [[] for _ in range(len(squadre_ordinate))]
    for i, squadra_ordinata in enumerate(squadre_ordinate):
        for bambino in squadra_ordinata:
            squadre_bilanciate[i % len(squadre_ordinate)].append(bambino)

    return squadre_bilanciate

def sbilanciamento_squadra(squadra):
    # Calcola la differenza di età massima nella squadra
    eta_squadra = [bambino['eta'] for bambino in squadra]
    return max(eta_squadra) - min(eta_squadra)

def peso_parrocchia_eta(bambino, squadre):
    # Funzione per assegnare un peso alla parrocchia e all'età
    peso_parrocchia = 3 if bambino['parrocchia'] in [b['parrocchia'] for squadra in squadre for b in squadra] else 1
    peso_eta = 2 if bambino['eta'] in [b['eta'] for squadra in squadre for b in squadra] else 1
    return peso_parrocchia * peso_eta