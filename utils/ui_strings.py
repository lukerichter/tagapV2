# Button Labels
button_text_submit_date = "✔"
button_text_save_file = "Speichern"
button_text_open_file = "Öffnen"
button_text_pattern = "Vorlage speichern"

# Textbox messages
first_message = ("Willkommen zum TAG-Auswertungsprogramm \n"
                 "Um die Auswertung zu starten, laden Sie bitte eine CSV-Datei mit den Rohdaten hoch. \n"
                 "Dazu klicken Sie auf 'Öffnen' und wählen die entsprechende Datei aus. \n")

date_message = ("Bitte geben Sie das Testdatum ein und klicken Sie zum Bestätigen auf den Haken daneben. \n"
                "Das Datum sollte das Format TT.MM.JJJJ haben. \n"
                "Beispiel: 25.12.2023 oder 25.12.23\n")

date_error_message = ("Das eingegebene Datum ist ungültig! \n"
                      "Bitte geben Sie das Datum im Format TT.MM.JJJJ ein. \n"
                      "Beispiel: 25.12.2023 oder 25.12.23\n")

download_message = ("Alles klar! \n"
                    "Klicken Sie auf 'Speichern', um die Ergebnisse als CSV-Datei zu speichern. \n"
                    "Warten sie bitte, bis der Vorgang abgeschlossen ist, bevor Sie das Programm beenden. \n")

download_success_message = ("Die Datei wurde erfolgreich gespeichert! \n"
                            "Sie können das Programm nun schließen. \n")

pattern_message = "Die Vorlage wurde erfolgreich gespeichert! \n"

def error_head_message(number):
    return f"Es wurde{'n' if number != 1 else ''} {number} Fehler in der Tabelle gefunden.\n"
