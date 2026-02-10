import os
import subprocess


def build_command(args):
    command = ['prusa-slicer']

    for setting in args.settings:
        command.append('--load')
        command.append(setting)

    command.append('-g')
    command.append('-s')
    command.append('--output')
    command.append(args.gcode_output)
    command.append(args.file)

    return command

def run_command(command, debug: bool):
    # Run the PS command
    stdout = None if debug else subprocess.DEVNULL
    stderr = None if debug else subprocess.DEVNULL
    subprocess.run(command, stdout=stdout, stderr=stderr)

def read_gcode(filename):
    with open(filename) as f:
        return f.read()


def clean_gcode(filename):
    header_size = 4096  # 4KB for header comments
    footer_size = 65536 # 64KB for footer metadata

    with open(filename, 'rb') as f:
        f.seek(0, os.SEEK_END)
        file_size = f.tell()

        # Read header
        f.seek(0)
        header = f.read(min(file_size, header_size)).decode('utf-8', errors='ignore')

        # Read footer
        footer = ""
        if file_size > header_size:
            read_pos = max(header_size, file_size - footer_size)
            f.seek(read_pos)
            footer = f.read(file_size - read_pos).decode('utf-8', errors='ignore')

    lines = []
    for line in (header + footer).splitlines():
        if line.startswith(';'):
            lines.append(line)
    
    return "\n".join(lines)


