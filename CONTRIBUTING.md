# Contributing Guide

## Module ownership

- Yixin Feng: repository structure, params, utils, interfaces, README setup
- Ha Pham: Heston simulation engine
- Yingyue Lai: realized variance and variance swap pricing
- Jiani Han: variance option pricing
- Lin Tian: control variate module
- Xingjian Tian: experiments, plots, and final integration

## Project rules

- Use the shared parameter classes from `src/heston_mc/params.py`
- Use the shared interface layer from `src/heston_mc/interfaces.py`
- Use **simple returns**, not log returns
- Keep naming consistent across all modules
- Put reusable code in `src/heston_mc/`
- Put tests in `tests/`
- Write clear commit messages
