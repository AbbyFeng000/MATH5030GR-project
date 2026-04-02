# Contributing Guide

## Module ownership

- Student 1: repository structure, params, utils, interfaces, README setup
- Student 2: Heston simulation engine
- Student 3: realized variance and variance swap pricing
- Student 4: variance option pricing
- Student 5: control variate module
- Student 6: experiments, plots, and final integration

## Project rules

- Use the shared parameter classes from `src/heston_mc/params.py`
- Use the shared interface layer from `src/heston_mc/interfaces.py`
- Use **simple returns**, not log returns
- Keep naming consistent across all modules
- Put reusable code in `src/heston_mc/`
- Put tests in `tests/`
- Write clear commit messages
