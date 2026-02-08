pwd := `pwd`
bbl-cfg := "/home/ayimany/.config/BambuStudio/system/BBL"
bbl-filament := "/filament/Generic ABS.json"
bbl-machine := "/machine/Bambu Lab P1S 0.4 nozzle.json"
bbl-process := "/process/0.20mm Standard @BBL X1C.json"
slicer := 'bambu-studio'

rearrange-file number:
    mkdir -p example-outputs/{{number}}
    uv run main.py example-inputs/{{number}}/in.stl example-outputs/{{number}}/out.stl

rearrange-file-blender number:
    mkdir -p example-outputs/{{number}}
    blender -b -P main.py -- example-inputs/{{number}}/in.stl example-outputs/{{number}}/out.stl

# Bambu Requires Absolute Paths
export-input-with-bambu number:
    mkdir -p example-bambu-outputs/{{number}}
    xvfb-run -a -- {{slicer}} --debug 4 --load-filaments "{{bbl-cfg}}{{bbl-filament}}" --load-settings "{{bbl-cfg}}{{bbl-machine}};{{bbl-cfg}}{{bbl-process}}" {{pwd}}/example-inputs/{{number}}/in.stl --export-3mf {{pwd}}/example-bambu-outputs/{{number}}/out-normal.3mf

export-output-with-bambu number:
    mkdir -p example-bambu-outputs/{{number}}
    xvfb-run -a -- {{slicer}} --load-filaments "{{bbl-cfg}}{{bbl-filament}}" --load-settings "{{bbl-cfg}}{{bbl-machine}};{{bbl-cfg}}{{bbl-process}}" --export-slicedata . {{pwd}}/example-outputs/{{number}}/out.stl --export-3mf {{pwd}}/example-bambu-outputs/{{number}}/out-transformed.3mf

open-normal-with-bambu number:
    {{slicer}} "{{pwd}}/example-bambu-outputs/{{number}}/out-normal.3mf"

open-transformed-with-bambu number:
    {{slicer}} "{{pwd}}/example-bambu-outputs/{{number}}/out-transformed.3mf"

run-pipeline-no-transform number:
    just rearrange-file {{number}} export-input-with-bambu {{number}} open-normal-with-bambu {{number}}

run-pipeline number:
    just rearrange-file {{number}} export-output-with-bambu {{number}} open-transformed-with-bambu {{number}}