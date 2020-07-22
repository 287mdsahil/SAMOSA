# SAMOSA
Sub-spaced Archived Multi Objective Simulated Annealing

```
usage: samosa [-h] [--n-iter N_ITER] [--max-temp MAX_TEMP] [--min-temp MIN_TEMP] problem_function n_objectives hard_limit soft_limit alpha

positional arguments:
  problem_function     Name of the problem function set to optimize
  n_objectives         Number of objective functions
  hard_limit           Hard limit
  soft_limit           Soft limit
  alpha                Alpha value

optional arguments:
  -h, --help           show this help message and exit
  --n-iter N_ITER      Number of iterations per temperature
  --max-temp MAX_TEMP  Maximum temperature
  --min-temp MIN_TEMP  Minimum temperature
```
