import logging
import re
from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True)
class InterestInfo:
    id: str
    label: str
    regex: str


class Interest(Enum):
    FILAMENT_USED_MM                 = InterestInfo('filament_used_mm', 'Filament used (mm)', r'; filament used \[mm] = (.*)')
    FILAMENT_USED_CM3                = InterestInfo('filament_used_cm3', 'Filament used (cm^3)', r'; filament used \[cm3] = (.*)')
    FILAMENT_USED_G                  = InterestInfo('filament_used_g', 'Filament used (g)', r'; filament used \[g] = (.*)')
    FILAMENT_COST_CASH               = InterestInfo('filament_cost_cash', 'Filament cost ($)', r'; filament cost = (.*)')
    FILAMENT_USED_TOTAL_G            = InterestInfo('filament_used_total_g', 'Filament used (Total, g)', r'; total filament used \[g] = (.*)')
    FILAMENT_COST_TOTAL_CASH         = InterestInfo('filament_cost_total_cash', 'Filament cost (Total, $)', r'; total filament cost = (.*)')
    FILAMENT_USED_WIPE_TOWER         = InterestInfo('filament_used_wipe_tower', 'Filament used (In wipe tower, g)', r'; total filament used for wipe tower \[g] = (.*)')
    PRINTING_TIME_ESTIMATED_NORMAL   = InterestInfo('printing_time_estimated_normal', 'Printing time (Estimated, Normal mode)', r'; estimated printing time \(normal mode\) = (.*)')
    PRINTING_TIME_ESTIMATED_SILENT   = InterestInfo('printing_time_estimated_silent', 'Printing time (Estimated, Silent mode)', r'; estimated printing time \(silent mode\) = (.*)')
    PRINTING_TIME_FIRST_LAYER_NORMAL = InterestInfo('printing_time_first_layer_normal', 'Printing time (First layer, Normal mode)', r'; estimated first layer printing time \(normal mode\) = (.*)')
    PRINTING_TIME_FIRST_LAYER_SILENT = InterestInfo('printing_time_first_layer_silent', 'Printing time (First layer, Silent mode)', r'; estimated first layer printing time \(silent mode\) = (.*)')

    @property
    def info(self) -> InterestInfo:
        return self.value


def find_interest(interest: Interest, gcode: str):
    match = re.search(interest.info.regex, gcode)
    if match:
        return match.group(1)
    
    logging.warning(f'Could not find interest {interest.name} in gcode')
    return None

