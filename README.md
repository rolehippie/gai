# gai

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/gai/status.svg)](https://cloud.drone.io/rolehippie/gai)

Ansible role to configure gai

## Table of content

* [Default Variables](#default-variables)
  * [gai_precendence](#gai_precendence)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### gai_precendence

List of precendence values

#### Default value

```YAML
gai_precendence:
  - ::ffff:0:0/96 100
```

## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
