# Squadifier2 - Software per creare squadre
Questo progetto nasce dal bisogno del mio gruppo diocesano di AC di creare delle squadre per le feste con i bambini.
È stato scritto in Python, utilizzando PyQt5 come libreria grafica, e Qt Designer come interfaccia per il design della finestra.
Il codice sorgente è completamente modificabile, per quanto delle build per Widnows e MacOS siano già fornite (cartella `builds`).

## Prerequisiti
Le build sono autosufficienti. Nel caso in cui si volesse "giocare" con il codice sorgente, installare la versione più recente di Python e utilizzare il comando:

```bash
pip install -r requirements.txt
```
per assicurarsi di avere tutti i moduli necessari per interagire con gli script di Python.

Per modificare il layout e/o elementi della finestra di dialogo, aprire il file `squadifier2.ui` (all'interno della cartella `src/Windows` o `src/MacOS`, a seconda del sistema operativo) in un editor di Qt (come Qt Designer). Per aggiornare il file principale usare il comando

```bash
pyuic5 -x squadifier2.ui -o squadifier2.py
```
per aggiornare il file `squadifier2.py` con il nuovo layout.<br />

<span style="color: red"><b>ATTENZIONE:</b></span> questa operazione sovrascrive qualsiasi tipo di inserzioni manuali, utilizzare a proprio rischio e pericolo.

## Windows
L'eseguibile è utilizzabile così com'è, e il file con le squadre verrà generato nella stessa directory dell'eseguibile. Si trova nella cartella `builds/Windows/dist`.

Nel caso in cui si modifichi il codice sorgente, eliminare le cartelle `src/Windows/build` e `src/Windows/dist` (se presenti), poi, aprendo il terminale nella cartella del codice sorgente, usare questi comandi (in un terminale aperto nella cartella `src/Windows`):
```bash
pip install pyinstaller
```
per installare il modulo `pyinstaller`, che converte script python in app eseguibili per Windows. [Link documentazione pyinstaller](https://pyinstaller.org/en/stable/)

```bash
pyinstaller squadifier2.py --noconsole --icon="../../icon.ico" --onefile
```
per rigenerare l'eseguibile. Le flag `noconsole` e `onefile` assicurano la creazione, rispettivamente, di un eseguibile che non si avvii con la console di comando, e che contenga tutti i .dll al suo interno,
così da rendere la UX un po' più godibile.


## MacOS
L'app è utilizzabile così com'è, e il file con le squadre verrà generato nella stessa directory dell'app. Si trova nella cartella `builds/MacOS/dist`.

Nel caso in cui si modifichi il codice sorgente, eliminare le cartelle `src/MacOS/build` e `src/MacOS/dist`, poi, aprendo il terminale nella cartella del codice sorgente, usare questi comandi (in un terminale aperto nella cartella `src/MacOS`):
```bash
pip install py2app
```
per installare il modulo `py2app`, che converte script python in app eseguibili per MacOS. [Link documentazione py2app](https://py2app.readthedocs.io/en/latest/)

```bash
py2applet --make-setup squadifier2.py
```
per rigenerare il file di setup, e

```bash
python setup.py py2app -A
```
per rigenerare le build. L'app si trova nella cartella `dist`.

Per assicurarsi che l'icona venga utilizzata come icona dell'app, aprire `setup.py` e aggiungere le seguenti linee di codice:

```python
OPTIONS = {
    'iconfile':'icon.png',
    'plist': {'CFBundleShortVersionString':'0.1.0',}
}
```

al posto della variabile `OPTIONS` già presente.