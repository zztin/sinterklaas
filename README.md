# Sinterklaas Gift Assignment Tool

This Python tool helps organize a Sinterklaas style gift exchange. Each participant is assigned three receivers, and the script writes a separate txt file for every giver. The tool includes checks to ensure that no one receives too many gifts and that no one gives to themselves.

## Features
- Random assignment of gift receivers
- The users can define how many receivers each givers give gifts
- Output written as individual txt files named after each giver so that the person executing would not get to know the names
- Simple command line interface

## Installation
1. Open "Terminal", go to a directory where you want to store this tool.
2. Clone the repository and make sure you have Python 3 installed.

```bash
git clone <your repo url>
cd <repo folder>
```

## Example Usage
```
python sinterklaas.py --k 3 --outdir ./final/ --names Alice Bob Claudio Dieter Evert Finn
```
- Use ```python sinterklaas.py --help``` for more details.

```
Gift assignment generator

options:
  -h, --help            show this help message and exit
  --names NAMES [NAMES ...]
                        List of participant names
  --k K                 How many gifts each person gives
  --outdir OUTDIR       Output directory
```
