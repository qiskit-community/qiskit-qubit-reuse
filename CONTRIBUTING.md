# Contributing

We follow the same guidelines as [Qiskit](https://qiskit.org/documentation/contributing_to_qiskit.html). All contributions must also follow these guidelines:

## Bugs and feature requests:

Please use Github Issues for reporting bugs found within this plugin. The same goes for feature requests.

## Code Review

All new coded feature proposals should be done via Pull Requests. All sumbissions will require review by one of the mantainers.

## Code formatting:

This project uses [Black](https://pypi.org/project/black/) and [Ruff](https://beta.ruff.rs/docs/) for code formatting.
To install and use Black:

```sh
pip install black
```
For automated code formatting with black:
```sh
black qiskit_qubit_reuse
```
For code formatting review, use:
```sh
black --check qiskit_qubit_reuse
```

To install and use Ruff:
```sh
pip install ruff
ruff check .
```