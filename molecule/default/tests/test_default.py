import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_gai_config_file(host):
    file = host.file("/etc/gai.conf")
    assert file.contains("::ffff:0:0/96 100")
