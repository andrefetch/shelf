# shelf

A minimal CLI note and bookmark manager, stores notes locally as JSON.

## Installation

```bash
git clone https://github.com/andrefetch/shelf
cd shelf
pip install -e .
```

## Usage

```bash
shelf add "note title" "note body" --tags tag1 tag2
shelf list
shelf remove <id>
```

## Data

Notes are saved to `~/.shelf_data.json`.
