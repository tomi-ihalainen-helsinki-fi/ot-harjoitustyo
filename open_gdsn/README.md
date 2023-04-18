# OpenGDSN

GS1 Global Data Synchronisation Network (GS1 GDSN) data transfer, view and edit tool.

## Documentation

* [Requirement Specification](./documentation/requirements_specification.md)
* [Work Hours](./documentation/work_hours.md)
* [Changelog](./documentation/changelog.md)


## Commands

### Installation

Install dependencies with command:

```bash
poetry install
```

### Start the application -- TODO

```bash
poetry run invoke start
```

### Tests and code coverage

Run tests and generate HTML report in _htmlcov_ directory:

```bash
poetry run invoke coverage-report
```

### Lint

```bash
poetry run invoke lint
```

### Format code

```bash
poetry run invoke format
```
