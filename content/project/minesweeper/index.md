---
title: Minesweeper Solver
summary: Simple minesweeper solver in Python
tags:
- Just for fun

# Optional external URL for project (replaces project detail page).
external_link: ""

date: "2022-01-06"

image: 
caption: 
focal_point: Smart

links:
- icon: twitter
  icon_pack: fab
  name: Follow
  url: https://twitter.com/rhdzmota
  url_code: "https://github.com/RHDZMOTA/minesweeper"
  url_pdf: ""
  url_slides: ""
  url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: example
---

This simple python implementation is able to infer the solution from a minesweeper board. Consider the following board configuration:

![](https://imgs.xkcd.com/comics/mine_captcha.png)

We can respresent that board on the commandline by using a `[.]` notation. You should be able to get a solution by running:

```commandline
$ minesweeper --timeout 3 --grid """
[2] [?] [1] [?]
[?] [?] [3] [?]
[3] [?] [?] [?]
[?] [1] [?] [1]
"""

```

Expected output:

```text
[2] [ ] [1] [ ]
[*] [*] [3] [ ]
[3] [*] [ ] [*]
[ ] [1] [ ] [1]
```

## Installation

Install this application using pip directly referencing the dev branch from github:

```commandline
$ pip install git+https://github.com/rhdzmota/minesweeper.git@dev#subdirectory=minesweeper&egg=minesweeper
```

Alteratively, you can clone this repository and install the minesweeper package with:

```commandline
$ pip install -e minesweeper
```

Verify correct installation by running: `minesweeper --help` or `python -m minesweeper --help`

## CLI Usage

Provide a grid with the following cell types:

* `[ ]`: empty cell.
* `[?]`: non-visible cell.
* `[*]`: flagged cell.
* `[i]`: cell with a number hint between 1 to 8 (e.g., [3], [1]).

You can solve any board configuration by running the `--grid` command:

```commandline
$ minesweeper --timeout 3 --grid """
[3] [?] [2] [?]
[?] [?] [ ] [?]
"""

Expected output:

```text
[3] [*] [2] [ ]
[*] [*] [ ] [ ]
```

## Package Usage

Once installed, you can also use this application as a python library.

Create a simple board:

```python
from minesweeper.board import Grid, Cell

my_grid = Grid(
    values=[
        [Cell.num(2), Cell.unk(), Cell.num(1), Cell.unk()],
        [Cell.unk(), Cell.unk(), Cell.num(3), Cell.unk()],
        [Cell.num(3), Cell.unk(), Cell.unk(), Cell.unk()],
        [Cell.unk(), Cell.num(1), Cell.unk(), Cell.num(1)]
    ]
)

my_grid.show()
```

You can solve a grid by using the `Solver` class:

```python
from minesweeper.solver import Solver

solver = Solver(gird=my_grid)
solver.run(timeout=10)

if solver.finished():
  solution = solver.final_state
  solution.show()
```
