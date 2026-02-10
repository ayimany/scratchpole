import logging
import re
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

from scratchpole.available_interests import interests, Interest, get_nested_interests


def parse_prusa_time(time_str: str) -> int:
    days = 0
    hours = 0
    minutes = 0
    seconds = 0

    d_match = re.search(r'(\d+)d', time_str)
    if d_match:
        days = int(d_match.group(1))

    h_match = re.search(r'(\d+)h', time_str)
    if h_match:
        hours = int(h_match.group(1))

    m_match = re.search(r'(\d+)m', time_str)
    if m_match:
        minutes = int(m_match.group(1))

    s_match = re.search(r'(\d+)s', time_str)
    if s_match:
        seconds = int(s_match.group(1))

    return days * 86400 + hours * 3600 + minutes * 60 + seconds


def format_time(seconds: int, target_format: str) -> str:
    if target_format == 'seconds':
        return str(seconds)
    elif target_format == 'minutes':
        return f"{seconds / 60:.2f}"
    elif target_format == 'hours':
        return f"{seconds / 3600:.2f}"
    return str(seconds)


@dataclass(frozen=True)
class ExtractedInterest:
    key: str
    label: str
    value: str

def find_interest(key: str, gcode: str, time_format: str = 'full') -> Optional[ExtractedInterest]:
    if key not in interests.keys():
        logging.warning(f'Could not find interest {key}')
        return None

    interest = interests[key]

    match = re.search(interest.regex, gcode)
    if match:
        value = match.group(1)
        if key.startswith('time.') and time_format != 'full':
            seconds = parse_prusa_time(value)
            value = format_time(seconds, time_format)

        return ExtractedInterest(
            key,
            interest.label,
            value
        )

    logging.warning(f'Could not find interest {key} within the parsed gcode')
    return None


def extract_interests(gcode: str, requested_keys: List[str] = None, time_format: str = 'full') -> List[ExtractedInterest]:
    """Extracts a list of interests from the gcode."""
    if requested_keys is None:
        requested_keys = list(interests.keys())
    
    results = []
    for key in requested_keys:
        interest = find_interest(key, gcode, time_format)
        if interest:
            results.append(interest)
    return results

