# gai

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&amp;logoColor=white)](https://github.com/rolehippie/gai)
[![General Workflow](https://github.com/rolehippie/gai/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/gai/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/gai/actions/workflows/readme.yml/badge.svg)](https://github.com/rolehippie/gai/actions/workflows/readme.yml)
[![Galaxy Workflow](https://github.com/rolehippie/gai/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/gai/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/gai)](https://github.com/rolehippie/gai/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.gai-blue)](https://galaxy.ansible.com/rolehippie/gai)

Ansible role to configure gai preferences.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Default Variables](#default-variables)
  - [gai_precendence](#gai_precendence)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Default Variables

### gai_precendence

List of precendence values

#### Default value

```YAML
gai_precendence:
  - ::ffff:0:0/96 100
```

## Discovered Tags

**_gai_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
