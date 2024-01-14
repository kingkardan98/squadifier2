from datetime import date

def scriviWindows(squadNum, testo):
    filename = 'squadre{}_{}.txt'.format(squadNum, date.today())
    with open(filename, 'a+') as file:
        file.write(testo)
    return filename