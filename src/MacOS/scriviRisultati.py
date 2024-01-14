from datetime import datetime

def scriviMacOS(squadNum, testo):
    filename = '../../../squadre{}_{}.txt'.format(squadNum, datetime.today())
    with open(filename, 'a+') as file:
        file.write(testo)
    return filename