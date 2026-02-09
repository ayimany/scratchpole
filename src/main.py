import argparse
import subprocess
import data_interests

def main():
    command = ['prusa-slicer']

    parser = argparse.ArgumentParser(
        prog='scratchpole',
        description='Helps you scratch my pole',
        epilog='Happy slicing.',
    )

    parser.add_argument('file', metavar='FILE', type=str)
    parser.add_argument('--debug', type=int, default=0)
    parser.add_argument('-o', '--output', metavar='FILE', type=str, default='scratched-pole.gcode')
    parser.add_argument('--settings', metavar='FILE', type=str, nargs='*', required=True)

    args = parser.parse_args()

    for setting in args.settings:
        command.append('--load')
        command.append(setting)

    command.append('-g')
    command.append('-s')
    command.append('--output')
    command.append(args.output)
    command.append(args.file)

    # Run the PS command
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Parse the thang
    with open(args.output) as f:
        data = f.read()
        for interest in data_interests.Interest:
            value = data_interests.find_interest(interest, data)
            if value:
                print(f"{interest.info.label}: {value}")





if __name__ == '__main__':
    main()