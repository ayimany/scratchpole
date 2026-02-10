import logging
import os
from scratchpole.arguments import arguments
from scratchpole.data_interests import find_interest
from scratchpole.export import export_json, export_file
from scratchpole.prusa import build_command, run_command, clean_gcode


def main():
    command = build_command(arguments)
    run_command(command, arguments.debug)
    data = clean_gcode(arguments.gcode_output)

    if arguments.interests is None:
        logging.error('Please provide at least one interest')
        exit(1)

    interests = [find_interest(interest, data) for interest in arguments.interests]

    if arguments.export is not None:
        export_file(interests, arguments.export)

    if not arguments.silent:
        if arguments.pretty_print:
            for interest in interests:
                print(f"{interest.label}: {interest.value}")
        else:
            for interest in interests:
                print(f"{interest.key}: {interest.value}")

    # Cleanup
    if not arguments.dont_delete_gcode:
        os.remove(arguments.gcode_output)



if __name__ == '__main__':
    main()