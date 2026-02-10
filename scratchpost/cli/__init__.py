import logging
import os
from scratchpost import (
    arguments,
    extract_interests,
    export_file,
    build_command,
    run_command,
    clean_gcode
)


def main():
    command = build_command(arguments)
    run_command(command, arguments.debug)
    data = clean_gcode(arguments.gcode_output)

    extracted = extract_interests(data, arguments.interests, arguments.time_format)

    if arguments.export is not None:
        export_file(extracted, arguments.export)

    if not arguments.silent:
        if arguments.pretty_print:
            for interest in extracted:
                print(f"{interest.label}: {interest.value}")
        else:
            for interest in extracted:
                print(f"{interest.key}: {interest.value}")

    # Cleanup
    if not arguments.dont_delete_gcode:
        os.remove(arguments.gcode_output)


if __name__ == '__main__':
    main()
