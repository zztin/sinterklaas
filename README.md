# Sinterklaas Gift Assignment Tool

This Python tool helps organize a Sinterklaas style gift exchange. Each participant is assigned three receivers, and the script writes a separate txt file for every giver. The tool includes checks to ensure that no one receives too many gifts and that no one gives to themselves.

## Features
- Random assignment of gift receivers
- Each giver gets exactly three names
- Output written as individual txt files named after each giver
- Validation to ensure correct counts
- Self giving check
- Simple command line interface

## Installation
Clone the repository and make sure you have Python 3 installed.

```bash
git clone <your repo url>
cd <repo folder>
```

## Usage
```python sinterklaas_final.py --k <number of gifts each person receives> --outdir ./final/ --names <A list of names separated with space>  --check```

