# Study Planner

Study Planner reads a CSV task list, orders the tasks by priority, assigns the available study time, and prints a plan for the evening.

## Requirements

- Python 3.12

Run commands from the `python-bootcamp` directory.

```text
python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26
```

## CSV format

The input CSV must have these four columns:

| Column | Meaning | Example |
| --- | --- | --- |
| `title` | Task name | `Assignment` |
| `importance` | Priority from 1 to 5 | `4` |
| `effort_h` | Estimated hours | `1.5` |
| `deadline` | Deadline in ISO date format | `2026-10-27` |

Example:

```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

## Command-line options

| Argument | Description |
| --- | --- |
| `csv` | Path to the input task CSV file. |
| `--hours H` | Required number of hours available for the plan. |
| `--today YYYY-MM-DD` | Optional reference date. Defaults to today. Use it for reproducible results. |
| `--strict` | Exit with code 1 if the task effort exceeds the available hours. |

## Example output

```text
Tonight (2.0 h):
1. Assignment - 1.5 h
2. DS exam - 0.5 h
```

## Errors and exit codes

The command exits with code `0` after a successful plan. It exits with code `1` when the CSV file is missing, empty, or contains invalid data. Errors are printed to standard error with the `error:` prefix.

When the combined task effort is greater than `--hours`, the default behavior prints a `warning:` and still returns a partial plan with exit code `0`. Add `--strict` to treat that condition as an error and return code `1`.

## Module flow

The program runs the following pipeline:

```text
parse_csv -> prioritise -> allocate -> render
```

`parse_csv` validates input rows, `prioritise` orders the tasks using the reference date, `allocate` limits the plan to the available hours, and `render` formats the numbered result.

## Tests

From the repository root, run:

```text
ruff check python-bootcamp
pytest -q python-bootcamp
```
