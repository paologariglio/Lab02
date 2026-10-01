from csv import reader
def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    # TODO
    try:
        with open(file_path,"r",encoding="utf-8") as infile:
            csv_reader = reader(infile)
            album = { }
            for riga in csv_reader:
                if riga[0] == "codice":
                    continue
                else:
                    codice = riga[0]
                    titolo = riga[1]
                    autore = riga[2]
                    mese = int(riga[3])
                    anno = riga[4]
                    if anno not in album:
                        album[anno] = { }
                    album[anno][codice] = [titolo, autore, mese]
        return album
    except FileNotFoundError:
        print("Il file path non esiste")
        return None

def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    # TODO
    mese = int(mese)
    if not (1 <= mese <=12):
        return None
    for anno_esistente in album:
        if codice in album[anno_esistente]:
            return None
    try:
        with open(file_path,"a",encoding="utf-8") as outfile:
            nuova_riga = (f"{ codice},{ titolo},{autore},{mese},{anno}")
            outfile.write(nuova_riga)
    except FileNotFoundError:
        return None
    #aggiornamento della struttura dati in caso di anno non presente
    if anno not in album:
        album[anno] = { }
    foto_aggiunta = [titolo,autore,mese]
    album[anno][codice] = foto_aggiunta
    return foto_aggiunta



def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""
    # TODO
    for anno in album:
        foto = album[anno]
        if codice in foto:
            dati = foto[codice]
            titolo = dati[0]
            autore = dati[1]
            mese = dati[2]
            return f"{codice}, {titolo}, {autore}, {mese}, {anno}"
    return None

def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    # TODO
    anno_str = str(anno)
    if anno_str not in album:
        return None
    foto_anno = album[anno_str]
    titoli = []
    for codice in foto_anno:
        dati = foto_anno[codice]
        titolo = dati[0]
        titoli.append(titolo)
    titoli.sort()
    return titoli

def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
