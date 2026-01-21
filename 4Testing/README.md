# --check and --diff
```
(venv) root@ubuntu03:~/scripting/lansible/4Testing#  ansible localhost -m ping -v
No config file found; using defaults
[DEPRECATION WARNING]: ANSIBLE_COLLECTIONS_PATHS option, does not fit var naming standard, use the singular form ANSIBLE_COLLECTIONS_PATH instead. This feature will be removed from ansible-core in version 2.19. Deprecation warnings can be disabled by setting deprecation_warnings=False
 in ansible.cfg.
[WARNING]: No inventory was parsed, only implicit localhost is available
localhost | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
(venv) root@ubuntu03:~/scripting/lansible/4Testing# ansible  localhost -m ping -vv
ansible [core 2.17.14]
  config file = None
  configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /root/scripting/lansible/venv/lib/python3.10/site-packages/ansible
  ansible collection location = /root/scripting/lansible/4Testing/collections
  executable location = /root/scripting/lansible/venv/bin/ansible
  python version = 3.10.12 (main, Jan  8 2026, 06:52:19) [GCC 11.4.0] (/root/scripting/lansible/venv/bin/python3)
  jinja version = 3.1.6
  libyaml = True
No config file found; using defaults
[DEPRECATION WARNING]: ANSIBLE_COLLECTIONS_PATHS option, does not fit var naming standard, use the singular form ANSIBLE_COLLECTIONS_PATH instead. This feature will be removed from ansible-core in version 2.19. Deprecation warnings can be disabled by setting deprecation_warnings=False
 in ansible.cfg.
[WARNING]: No inventory was parsed, only implicit localhost is available
Skipping callback 'default', as we already have a stdout callback.
Skipping callback 'minimal', as we already have a stdout callback.
Skipping callback 'oneline', as we already have a stdout callback.
localhost | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
(venv) root@ubuntu03:~/scripting/lansible/4Testing# localhost -m copy -a "content='Ishan Mahajan' dest=my_file"
localhost: command not found
(venv) root@ubuntu03:~/scripting/lansible/4Testing# ansible localhost -m copy -a "content='Ishan Mahajan' dest=my_file"
[DEPRECATION WARNING]: ANSIBLE_COLLECTIONS_PATHS option, does not fit var naming standard, use the singular form ANSIBLE_COLLECTIONS_PATH instead. This feature will be removed from ansible-core in version 2.19. Deprecation warnings can be disabled by setting deprecation_warnings=False
 in ansible.cfg.
[WARNING]: No inventory was parsed, only implicit localhost is available
localhost | CHANGED => {
    "changed": true,
    "checksum": "afa8eda363c62ab7fe66066a46064032e755e322",
    "dest": "./my_file",
    "gid": 0,
    "group": "root",
    "md5sum": "60475653c9d0d36f8dca13ec76d959f5",
    "mode": "0644",
    "owner": "root",
    "size": 13,
    "src": "/root/.ansible/tmp/ansible-tmp-1768996712.2749078-147050-28599531613343/.source",
    "state": "file",
    "uid": 0
}
(venv) root@ubuntu03:~/scripting/lansible/4Testing# ll
total 12
drwxr-xr-x 2 root root 4096 Jan 21 11:58 ./
drwxr-xr-x 8 root root 4096 Jan 21 11:48 ../
-rw-r--r-- 1 root root   13 Jan 21 11:58 my_file
(venv) root@ubuntu03:~/scripting/lansible/4Testing# cat my_file
Ishan Mahajan(venv) root@ubuntu03:~/scripting/lansible/4Testing#
(venv) root@ubuntu03:~/scripting/lansible/4Testing# ansible localhost -m copy -a "content='Ishan Mahajan' dest=my_file" --check --diff
[DEPRECATION WARNING]: ANSIBLE_COLLECTIONS_PATHS option, does not fit var naming standard, use the singular form ANSIBLE_COLLECTIONS_PATH instead. This feature will be removed from ansible-core in version 2.19. Deprecation warnings can be disabled by setting deprecation_warnings=False
 in ansible.cfg.
[WARNING]: No inventory was parsed, only implicit localhost is available

localhost | SUCCESS => {
    "changed": false,
    "checksum": "afa8eda363c62ab7fe66066a46064032e755e322",
    "dest": "my_file",
    "gid": 0,
    "group": "root",
    "mode": "0644",
    "owner": "root",
    "path": "my_file",
    "size": 13,
    "state": "file",
    "uid": 0
}
(venv) root@ubuntu03:~/scripting/lansible/4Testing# ansible localhost -m copy -a "content='Ishan Mahajan is working' dest=my_file" --check --diff
[DEPRECATION WARNING]: ANSIBLE_COLLECTIONS_PATHS option, does not fit var naming standard, use the singular form ANSIBLE_COLLECTIONS_PATH instead. This feature will be removed from ansible-core in version 2.19. Deprecation warnings can be disabled by setting deprecation_warnings=False
 in ansible.cfg.
[WARNING]: No inventory was parsed, only implicit localhost is available
--- before: my_file
+++ after: my_file
@@ -1 +1 @@
-Ishan Mahajan
\ No newline at end of file
+Ishan Mahajan is working
\ No newline at end of file

localhost | CHANGED => {
    "changed": true
}


```

# debug
```
venv) root@ubuntu03:~/scripting/lansible/4Testing# ansible localhost -m debug -a "msg='Ishan Mahajan is working'"
[DEPRECATION WARNING]: ANSIBLE_COLLECTIONS_PATHS option, does not fit var naming standard, use the singular form ANSIBLE_COLLECTIONS_PATH instead. This feature will be removed from ansible-core in version 2.19. Deprecation warnings can be disabled by setting deprecation_warnings=False
 in ansible.cfg.
[WARNING]: No inventory was parsed, only implicit localhost is available
localhost | SUCCESS => {
    "msg": "Ishan Mahajan is working"
}
(venv) root@ubuntu03:~/scripting/lansible/4Testing# ansible-playbook os.yml
[DEPRECATION WARNING]: ANSIBLE_COLLECTIONS_PATHS option, does not fit var naming standard, use the singular form ANSIBLE_COLLECTIONS_PATH instead. This feature will be removed from ansible-core in version 2.19. Deprecation warnings can be disabled by setting deprecation_warnings=False  in ansible.cfg.
[WARNING]: Unable to parse /root/scripting/lansible/4Testing/inventory/hosts as an inventory source
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Install Web Server Across Distributions] ***********************************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************************************************************************************************
ok: [localhost]

TASK [Display OS] ***********************************************************************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "The OS is: Debian"
}

TASK [Install package with yum] **************************************************************************************************************************************************************************************************************************************************************
skipping: [localhost]

TASK [Install package with apt] **************************************************************************************************************************************************************************************************************************************************************
ok: [localhost]

PLAY RECAP *************************************************************************************************************************************************************************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0


```

# molecule 
It is used for unittesting of roles

```
yum install -y molecule
pip install molecule
```

#### Molecule drivers 

1. delegate
   1. default driver 
   2. out of the box uses localhost
   3. can be delegated to cloud-environment
2. podman/docker
   1. molecule provisions containers for testing environment.
3. vagrant 
   1. same as podman/docker but full VM environment.

```
cd ~/.ansible/collections/anible_collections
ansible-galaxy collection init bob.utils
cd bob/utils
mkdir extensions
cd extensions
molecule init scenario
molecule test

(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions# molecule init scenario
INFO     default ➜ init: Initializing new scenario default...

PLAY [Create a new molecule scenario] ******************************************

TASK [Check if destination folder exists] **************************************
changed: [localhost]

TASK [Check if destination folder is empty] ************************************
ok: [localhost]

TASK [Fail if destination folder is not empty] *********************************
skipping: [localhost]

TASK [Expand templates] ********************************************************
changed: [localhost] => (item=molecule/default/destroy.yml)
changed: [localhost] => (item=molecule/default/verify.yml)
changed: [localhost] => (item=molecule/default/molecule.yml)
changed: [localhost] => (item=molecule/default/create.yml)
changed: [localhost] => (item=molecule/default/converge.yml)

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     default ➜ init: Initialized scenario in /root/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions/molecule/default successfully.
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions# tree
.
└── molecule
    └── default
        ├── converge.yml
        ├── create.yml
        ├── destroy.yml
        ├── molecule.yml
        └── verify.yml

2 directories, 5 files
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions#
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions# which python
/root/scripting/lansible/venv/bin/python
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions# molecule reset
INFO     default ➜ discovery: scenario test matrix:
INFO     default ➜ prerun: Performing prerun with role_name_check=0...
WARNING  Another version of 'ansible.posix' 1.6.2 was found installed in /root/scripting/lansible/venv/lib/python3.10/site-packages/ansible_collections, only the first one will be used, 2.1.0 (/root/.ansible/collections/ansible_collections).
WARNING  Another version of 'community.mysql' 3.11.0 was found installed in /root/scripting/lansible/venv/lib/python3.10/site-packages/ansible_collections, only the first one will be used, 4.0.1 (/root/.ansible/collections/ansible_collections).
INFO     default ➜ reset: Removing /root/.ansible/tmp/molecule.IO93.default
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions#

# create role for testing
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions# cd ..
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils# cd ..
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob# ls
utils
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob# cd utils/
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils# cd roles/
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/roles# ll
total 8
drwxr-xr-x 2 root root 4096 Jan 21 12:23 ./
drwxr-xr-x 8 root root 4096 Jan 21 12:28 ../
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/roles# ansible-galaxy  role init my_role
- Role my_role was created successfully

venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions# ls
molecule
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions# tree
.
└── molecule
    └── default
        ├── converge.yml
        ├── create.yml
        ├── destroy.yml
        ├── molecule.yml
        └── verify.yml

2 directories, 5 files



(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils# molecule  test                                                                                          [78/392]
INFO     Collection 'bob.utils' detected.
INFO     Scenarios will be used from 'extensions/molecule'
INFO     default ➜ discovery: scenario test matrix: dependency, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     default ➜ prerun: Performing prerun with role_name_check=0...
WARNING  Another version of 'ansible.posix' 1.6.2 was found installed in /root/scripting/lansible/venv/lib/python3.10/site-packages/ansible_collections, only the first one will be used, 2.1.0 (/root/.ansibl
e/collections/ansible_collections).
WARNING  Another version of 'community.mysql' 3.11.0 was found installed in /root/scripting/lansible/venv/lib/python3.10/site-packages/ansible_collections, only the first one will be used, 4.0.1 (/root/.ans
ible/collections/ansible_collections).
INFO     default ➜ dependency: Executing
WARNING  default ➜ dependency: Missing roles requirements file: requirements.yml
WARNING  default ➜ dependency: Missing collections requirements file: requirements.yml
WARNING  default ➜ dependency: Executed: 2 missing (Remove from test_sequence to suppress)
INFO     default ➜ cleanup: Executing
WARNING  default ➜ cleanup: Executed: Missing playbook (Remove from test_sequence to suppress)
INFO     default ➜ destroy: Executing
Using /root/.ansible/tmp/molecule.b9iX.default/ansible.cfg as config file
[WARNING]: Unable to parse /path/to/inventory.yml as an inventory source

PLAY [Destroy] *****************************************************************

TASK [Populate instance config] ************************************************
ok: [localhost] => {"ansible_facts": {"instance_conf": {}}, "changed": false}

TASK [Dump instance config] ****************************************************
skipping: [localhost] => {"changed": false, "false_condition": "server.changed | default(false) | bool", "skip_reason": "Conditional result was False"}

PLAY RECAP *********************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     default ➜ destroy: Executed: Successful
INFO     default ➜ syntax: Executing
Using /root/.ansible/tmp/molecule.b9iX.default/ansible.cfg as config file
[WARNING]: Unable to parse /path/to/inventory.yml as an inventory source

playbook: /root/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions/molecule/default/converge.yml
INFO     default ➜ syntax: Executed: Successful
INFO     default ➜ create: Executing
Using /root/.ansible/tmp/molecule.b9iX.default/ansible.cfg as config file
[WARNING]: Unable to parse /path/to/inventory.yml as an inventory source

PLAY [Create] ******************************************************************

TASK [Populate instance config dict] *******************************************
skipping: [localhost] => {"changed": false, "false_condition": "server.changed | default(false) | bool", "skip_reason": "Conditional result was False"}

TASK [Convert instance config dict to a list] **********************************
skipping: [localhost] => {"changed": false, "false_condition": "server.changed | default(false) | bool", "skip_reason": "Conditional result was False"}

TASK [Dump instance config] ****************************************************
skipping: [localhost] => {"changed": false, "false_condition": "server.changed | default(false) | bool", "skip_reason": "Conditional result was False"}

PLAY RECAP *********************************************************************
localhost                  : ok=0    changed=0    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0

INFO     default ➜ create: Executed: Successful                                                                                                                                                       [23/392]
INFO     default ➜ prepare: Executing
WARNING  default ➜ prepare: Executed: Missing playbook (Remove from test_sequence to suppress)
INFO     default ➜ converge: Executing
Using /root/.ansible/tmp/molecule.b9iX.default/ansible.cfg as config file
[WARNING]: Unable to parse /path/to/inventory.yml as an inventory source

PLAY [Converge] ****************************************************************

TASK [bob.utils.my_role : A test tasks] ****************************************
ok: [instance] => {
    "msg": "This is testing molecule of this role"
}

TASK [Apply role under test] ***************************************************
ok: [instance] => {
    "msg": "Thsi is a test"
}

PLAY RECAP *********************************************************************
instance                   : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     default ➜ converge: Executed: Successful
INFO     default ➜ idempotence: Executing
Using /root/.ansible/tmp/molecule.b9iX.default/ansible.cfg as config file
[WARNING]: Unable to parse /path/to/inventory.yml as an inventory source

PLAY [Converge] ****************************************************************

TASK [bob.utils.my_role : A test tasks] ****************************************
ok: [instance] => {
    "msg": "This is testing molecule of this role"
}

TASK [Apply role under test] ***************************************************
ok: [instance] => {
    "msg": "Thsi is a test"
}

PLAY RECAP *********************************************************************
instance                   : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     default ➜ idempotence: Executed: Successful
INFO     default ➜ side_effect: Executing
WARNING  default ➜ side_effect: Executed: Missing playbook (Remove from test_sequence to suppress)
INFO     default ➜ verify: Executing
Using /root/.ansible/tmp/molecule.b9iX.default/ansible.cfg as config file
[WARNING]: Unable to parse /path/to/inventory.yml as an inventory source

PLAY [Verify] ******************************************************************

TASK [Assert something] ********************************************************
ok: [instance] => {
    "changed": false,
    "msg": "All assertions passed"
}

PLAY [Converge] ****************************************************************

TASK [bob.utils.my_role : A test tasks] ****************************************
ok: [instance] => {
    "msg": "This is testing molecule of this role"
}

TASK [Apply role under test] ***************************************************
ok: [instance] => {
    "msg": "Thsi is a test"
}

PLAY RECAP *********************************************************************
instance                   : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     default ➜ idempotence: Executed: Successful
INFO     default ➜ side_effect: Executing
WARNING  default ➜ side_effect: Executed: Missing playbook (Remove from test_sequence to suppress)
INFO     default ➜ verify: Executing
Using /root/.ansible/tmp/molecule.b9iX.default/ansible.cfg as config file
[WARNING]: Unable to parse /path/to/inventory.yml as an inventory source

PLAY [Verify] ******************************************************************

TASK [Assert something] ********************************************************
ok: [instance] => {
    "changed": false,
    "msg": "All assertions passed"
}

PLAY RECAP *********************************************************************
instance                   : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     default ➜ verify: Executed: Successful
INFO     default ➜ cleanup: Executing
WARNING  default ➜ cleanup: Executed: Missing playbook (Remove from test_sequence to suppress)
INFO     default ➜ destroy: Executing
Using /root/.ansible/tmp/molecule.b9iX.default/ansible.cfg as config file
[WARNING]: Unable to parse /path/to/inventory.yml as an inventory source

PLAY [Destroy] *****************************************************************

TASK [Populate instance config] ************************************************
ok: [localhost] => {"ansible_facts": {"instance_conf": {}}, "changed": false}

TASK [Dump instance config] ****************************************************
skipping: [localhost] => {"changed": false, "false_condition": "server.changed | default(false) | bool", "skip_reason": "Conditional result was False"}

PLAY RECAP *********************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     default ➜ destroy: Executed: Successful
INFO     default ➜ scenario: Pruning extra files from scenario ephemeral directory
WARNING  Molecule executed 1 scenario (1 missing files)


(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions# molecule  converge
INFO     default ➜ discovery: scenario test matrix: dependency, create, prepare, converge
INFO     default ➜ prerun: Performing prerun with role_name_check=0...
WARNING  Another version of 'ansible.posix' 1.6.2 was found installed in /root/scripting/lansible/venv/lib/python3.10/site-packages/ansible_collections, only the first one will be used, 2.1.0 (/root/.ansible/collections/ansible_collections).
WARNING  Another version of 'community.mysql' 3.11.0 was found installed in /root/scripting/lansible/venv/lib/python3.10/site-packages/ansible_collections, only the first one will be used, 4.0.1 (/root/.ansible/collections/ansible_collections).
INFO     default ➜ dependency: Executing
WARNING  default ➜ dependency: Missing roles requirements file: requirements.yml
WARNING  default ➜ dependency: Missing collections requirements file: requirements.yml
WARNING  default ➜ dependency: Executed: 2 missing (Remove from converge_sequence to suppress)
INFO     default ➜ create: Executing
Using /root/.ansible/tmp/molecule.IO93.default/ansible.cfg as config file
[WARNING]: Unable to parse /path/to/inventory.yml as an inventory source

PLAY [Create] ******************************************************************

TASK [Populate instance config dict] *******************************************
skipping: [localhost] => {"changed": false, "false_condition": "server.changed | default(false) | bool", "skip_reason": "Conditional result was False"}

TASK [Convert instance config dict to a list] **********************************
skipping: [localhost] => {"changed": false, "false_condition": "server.changed | default(false) | bool", "skip_reason": "Conditional result was False"}

TASK [Dump instance config] ****************************************************
skipping: [localhost] => {"changed": false, "false_condition": "server.changed | default(false) | bool", "skip_reason": "Conditional result was False"}

PLAY RECAP *********************************************************************
localhost                  : ok=0    changed=0    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0

INFO     default ➜ create: Executed: Successful
INFO     default ➜ prepare: Executing
WARNING  default ➜ prepare: Executed: Missing playbook (Remove from converge_sequence to suppress)
INFO     default ➜ converge: Executing
Using /root/.ansible/tmp/molecule.IO93.default/ansible.cfg as config file
[WARNING]: Unable to parse /path/to/inventory.yml as an inventory source
ERROR! the role 'bob.utils.my_role' was not found in /root/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions/molecule/default/roles:/root/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/root/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions/molecule/default

The error appears to be in '/root/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions/molecule/default/converge.yml': line 12, column 7, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

  roles:
    - bob.utils.my_role
      ^ here
CRITICAL Ansible return code was 1, command was: ansible-playbook --inventory /root/.ansible/tmp/molecule.IO93.default/inventory --skip-tags molecule-notest,notest --diff --force-handlers --inventory=/path/to/inventory.yml /root/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions/molecule/default/converge.yml
ERROR    default ➜ converge: Executed: Failed
ERROR    Ansible return code was 1, command was: ansible-playbook --inventory /root/.ansible/tmp/molecule.IO93.default/inventory --skip-tags molecule-notest,notest --diff --force-handlers --inventory=/path/to/inventory.yml /root/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions/molecule/default/converge.yml
(venv) root@ubuntu03:~/scripting/lansible/4Testing/collections/ansible_collections/bob/utils/extensions#
```