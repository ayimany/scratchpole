run:
    uv run main.py example-inputs/nmc-server-cover.stl example-outputs/nmc-server-cover.stl

export-with-bambu:
    xvfb-run -a bambu-studio --load-filaments "/home/ayimany/.config/BambuStudio/system/BBL/filament/Generic ABS.json" --load-settings "/home/ayimany/.config/BambuStudio/system/BBL/machine/Bambu Lab P1S 0.4 nozzle.json;/home/ayimany/.config/BambuStudio/system/BBL/process/0.20mm Standard @BBL X1C.json" --export-slicedata . (pwd)/example-inputs/nmc-server-cover.stl --export-3mf (pwd)/example-bambu-outputs/out.3mf

open-with-bambu:
    bambu-studio (pwd)/example-bambu-outputs/out.3mf