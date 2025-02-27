```
  /$$$$$$                                   /$$
 /$$__  $$                                 |__/
| $$  \__/     /$$$$$$  /$$$$$$$   /$$$$$$$ /$$
| $$$$ /$$$$$$|____  $$| $$__  $$ /$$_____/| $$
| $$_/|______/ /$$$$$$$| $$  \ $$|  $$$$$$ | $$
| $$          /$$__  $$| $$  | $$ \____  $$| $$
| $$         |  $$$$$$$| $$  | $$ /$$$$$$$/| $$
|__/          \_______/|__/  |__/|_______/ |__/
```                       

# About

`f-ansi` is the  `f-utils` lib that does something.
- website: [futils.org/libs/f-ansi](https://futils.org/libs/f-ansi)
- contact: [futils@gmx.ie](mailto:futils@gmx.ie)
- discord: [coolab](https://discord.gg/waANUyCUGE)

# Structure

```
f_ansi/
  |-- __init__.py .............. import main.py
  |-- main.py .................. import modules
  `-- mods/
       |-- color/ .............. define Color class
       |-- keys/ ............... define Keys class
       |-- is_.py .............. define Is class
       `-- err_.py ............. define error classes       
```

# Install

The installation is from the branches `main` and `dev` of this repository.

- With `pip`:
```bash
# main branch
/path/to/venv/bin/pip install git+https://github.com/f-utils/f-ansi
# dev branch
/path/to/venv/bin/pip install git+https://github.com/f-utils/f-ansi/tree/dev
```

For other installation methods, see [futils.org/install](https://futils.org/docs/libs/install).

# Usage

The lib provides the class `Ansi`. We suggest to import it as:

```python
from f_ansi import Ansi
```

For more details, see [futils.org/libs/f-ansi](https://futils.org/libs/f-ansi).

# Contributing

- Open issues in [f-utils/.issues](https://github.com/f-utils/.issues).
- Join our [Discord](https://discord.gg/waANUyCUGE) server.
- See [CONTRIBUTING](https://github.com/f-utils/.github/blob/main/CONTRIBUTING.md).

# License

This lib is [licensed](./LICENSE) under `BSD 3-Clause`.
