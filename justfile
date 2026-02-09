process-settings := 'settings/process.ini'
filament-settings := 'settings/pla-fila.ini'

scratch number:
    python src/main.py --settings {{process-settings}} {{filament-settings}} -- inputs/{{number}}/in.stl