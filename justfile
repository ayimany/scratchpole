process-settings := 'settings/process.ini'
filament-settings := 'settings/pla-fila.ini'

scratch number:
    python scratchpost/cli/__init__.py --settings settings/process.ini settings/pla-fila.ini -i filament.used.g filament.used.cost time.normal.estimated --gcode-output a.gcode --time-format hours -- inputs/{{number}}/in.stl

install:
    pipx install . --force
