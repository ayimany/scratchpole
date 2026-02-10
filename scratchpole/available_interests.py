from dataclasses import dataclass
from typing import Dict, Any

@dataclass(frozen=True)
class Interest:
    label: str
    regex: str

def get_nested_interests() -> Dict[str, Any]:
    nested = {}
    for key, interest in interests.items():
        parts = key.split('.')
        current = nested
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = interest
    return nested

interests = {
    'filament.used.mm': Interest('Filament used (mm)', r'; filament used \[mm] = (.*)'),
    'filament.used.cm3': Interest('Filament used (cm^3)', r'; filament used \[cm3] = (.*)'),
    'filament.used.g': Interest('Filament used (g)', r'; filament used \[g] = (.*)'),
    'filament.used.cost': Interest('Filament cost ($)', r'; filament cost = (.*)'),
    'filament.used.wipe_tower': Interest('Filament used (In wipe tower, g)', r'; total filament used for wipe tower \[g] = (.*)'),
    'filament.used.total_g': Interest('Filament used (Total, g)', r'; total filament used \[g] = (.*)'),
    'filament.used.total_cost': Interest('Filament cost (Total, $)', '; total filament cost = (.*)'),

    'time.normal.estimated': Interest('Printing time (Estimated, Normal mode)', r'; estimated printing time \(normal mode\) = (.*)'),
    'time.silent.estimated': Interest('Printing time (Estimated, Silent mode)', r'; estimated printing time \(silent mode\) = (.*)'),
    'time.normal.first_layer': Interest('Printing time (First layer, Normal mode)', r'; estimated first layer printing time \(normal mode\) = (.*)'),
    'time.silent.first_layer': Interest('Printing time (First layer, Silent mode)', r'; estimated first layer printing time \(silent mode\) = (.*)'),
}