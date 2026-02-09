# Scratch Pole
A straightforward CLI tool to obtain 3D object slice data using Prusa Slicer.

## Usage
Wait for implementation. The idea is:

```shell
scratchpole --export-to-file <filename> \
  --machine-settings <machine>.ini      \
  --process-settings <process>.ini      \
  --filament-settings <filament>.ini    \
  <your-file>
```

## Roadmap

- [] Send input file to PS
- [] Generate GCode with PS
- [] Parse GCode with PS
- [] Export data via TOML
- [] Profit?

## Why?
I am starting to run a 3D printing business and I got frustrated over many
days of trying to find the right automation tools. Hell, I even considered
hiring a SaaS service, and we're not here for that, are we?

I want to provide users with quality slice data. After a week of trying the
broken `bambu-studio` cli, convex hull analysis for geometric manipulation,
volume calculations and more, the Prusa Slicer cli has been my holy grail.

Now, I want to simplify this process as much as possible through a simple CLI.

## Scratch Pole?
Some cat scratch poles have ropes that wind around similar to layers in a 3D
print. That's the inspiration.