# gai

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/gai) [![Build Status](https://img.shields.io/drone/build/rolehippie/gai/master?logo=drone)](https://cloud.drone.io/rolehippie/gai) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/gai)](https://github.com/rolehippie/gai/blob/master/LICENSE) 

Ansible role to configure gai preferences. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

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

* None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
