# Configurazione - come testare il codice
Ho scelto Python per la sua velocità e perchè pensavo fosse anche il modo migliore per permettere a voi di testare il codice,
installando pochi pacchetti:

- Installare l'ultima versione di Python: la 3.8 https://www.python.org/downloads/
- Installare Flask (per la Fase 3), con pip risulta molto veloce : https://flask.palletsprojects.com/en/1.1.x/installation/

# pratical_project
Il codice è suddiviso in 2 cartelle, una per la prima ed una per le ultime due (che condividono il modello Student, presente nella directory models)

## Fase 1 - directory fase_1
Eseguire il file main_fibonacci.py
Partendo da 1, lo script cercherà il primo numero della successione di Fibonacci che a abbia 1000 cifre stampandolo a video

## Fase 2 - directory fasi_2_3
Eseguire il file main.py
Lo script crea un oggetto di Student, definito come classe in Student.py e stampato a video con le sue proprietà
Di seguito stampa a video l'età dello studente e la media dei voti

Il testo della Fase 2 chiedeva di creare la property 'grades' di Student (una stringa), ed il metodo avg_grade per calcolare la media dei voti
Non sapendo se avg_grade dovesse intendere la property 'grades' come una stringa di voti, suddivisi da un separatore,
oppure prendere in input un array di interi
ho implementato due metodi per risolvere entrambe le ipotesi

avg_grade utilizza un array di interi passati come input
avg_grade2 utilizza la property 'grades' dell'oggetto Student interpretandola come una stringa di interi separati da virgole

## Fase 3 - directory fasi_2_3
Da postman
