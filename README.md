# lansible


- 1CreateProject : Simple playbook
- 2ROLES: Create ROLE
  ```
  ansible-galaxy role init base
  ```

    For collections
    ```
    ansible-galaxy collection install ansible.posix
    ```
- 3collections: Collections
  ```
  ansible-galaxy list
  ansible-galaxy role list
  ansible-galaxy collection list
(venv) root@ubuntu03:~/scripting/lansible/2ROLES# cd ~/.ansible/collections/ansible_collections/
ansible/                    ansible.posix-2.1.0.info/   community/                  community.mysql-4.0.1.info/
(venv) root@ubuntu03:~/scripting/lansible/2ROLES# cd ~/.ansible/collections/ansible_collections/

(venv) root@ubuntu03:~/scripting/lansible/3collections# ansible-galaxy collection install theurbanpenguin.utils
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Downloading https://galaxy.ansible.com/api/v3/plugin/ansible/content/published/collections/artifacts/theurbanpenguin-utils-0.0
.2.tar.gz to /root/.ansible/tmp/ansible-local-98522o2esoepb/tmpqj0u6z19/theurbanpenguin-utils-0.0.2-447b1_ag
Installing 'theurbanpenguin.utils:0.0.2' to '/root/.ansible/collections/ansible_collections/theurbanpenguin/utils'
theurbanpenguin.utils:0.0.2 was installed successfully
(venv) root@ubuntu03:~/scripting/lansible/3collections# ansible-galaxy collection list

# /root/.ansible/collections/ansible_collections
Collection                               Version
---------------------------------------- -------
ansible.posix                            2.1.0
community.mysql                          4.0.1
theurbanpenguin.utils                    0.0.2


(venv) root@ubuntu03:~/scripting/lansible/3collections# ansible localhost -bm theurbanpenguin.utils.manage_hosts -a "hostname=cf ip='1.1.1.1' state=present"
[WARNING]: No inventory was parsed, only implicit localhost is available
localhost | CHANGED => {
    "changed": true,
    "message": "Hostname cf added with IP 1.1.1.1."
}
(venv) root@ubuntu03:~/scripting/lansible/3collections# ansible localhost -bm theurbanpenguin.utils.manage_hosts -a "hostname=cf ip='1.1.1.1' state=present"
[WARNING]: No inventory was parsed, only implicit localhost is available
localhost | SUCCESS => {
    "changed": false,
    "message": "IP / Hostname pair exist. No changes made."
}
(venv) root@ubuntu03:~/scripting/lansible/3collections# ping cf
PING cf (1.1.1.1) 56(84) bytes of data.
64 bytes from cf (1.1.1.1): icmp_seq=1 ttl=128 time=20.2 ms
64 bytes from cf (1.1.1.1): icmp_seq=2 ttl=128 time=20.7 ms
^C
--- cf ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1008ms
rtt min/avg/max/mdev = 20.206/20.474/20.743/0.268 ms
(venv) root@ubuntu03:~/scripting/lansible/3collections# ansible localhost -bm theurbanpenguin.utils.manage_hosts -a "hostname=cf ip='1.1.1.1' state=absent"
[WARNING]: No inventory was parsed, only implicit localhost is available
localhost | CHANGED => {
    "changed": true,
    "message": "Hostname cf removed."
}
(venv) root@ubuntu03:~/scripting/lansible/3collections# ping cf
ping: cf: No address associated with hostname
(venv) root@ubuntu03:~/scripting/lansible/3collections# ansible-galaxy collection init bob.test
- Collection bob.test was created successfully


# After implementing ansible.cfg 
(venv) root@ubuntu03:~/scripting/lansible/3collections# ansible-config  dump --only-changed
COLLECTIONS_PATHS(/root/scripting/lansible/3collections/ansible.cfg) = ['/root/scripting/lansible/3collections/collections']
CONFIG_FILE() = /root/scripting/lansible/3collections/ansible.cfg
DEFAULT_HOST_LIST(/root/scripting/lansible/3collections/ansible.cfg) = ['/root/scripting/lansible/3collections/inventory/host>
DEFAULT_REMOTE_USER(/root/scripting/lansible/3collections/ansible.cfg) = im65
DEFAULT_ROLES_PATH(/root/scripting/lansible/3collections/ansible.cfg) = ['/root/scripting/lansible/3collections/roles']
HOST_KEY_CHECKING(/root/scripting/lansible/3collections/ansible.cfg) = False

(venv) root@ubuntu03:~/scripting/lansible/3collections# cd collections/ansible_collections/bob/test/
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections/ansible_collections/bob/test# ll
total 32
drwxr-xr-x 6 root root 4096 Jan 21 10:05 ./
drwxr-xr-x 3 root root 4096 Jan 21 10:04 ../
drwxr-xr-x 2 root root 4096 Jan 21 10:05 docs/
-rw-r--r-- 1 root root 3058 Jan 21 10:05 galaxy.yml
drwxr-xr-x 2 root root 4096 Jan 21 10:05 meta/
drwxr-xr-x 3 root root 4096 Jan 21 10:35 plugins/
-rw-r--r-- 1 root root   67 Jan 21 10:05 README.md
drwxr-xr-x 2 root root 4096 Jan 21 10:05 roles/
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections/ansible_collections/bob/test# ansible-galaxy collection build
[DEPRECATION WARNING]: ANSIBLE_COLLECTIONS_PATHS option, does not fit var naming standard, use the singular form
ANSIBLE_COLLECTIONS_PATH instead. This feature will be removed from ansible-core in version 2.19. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
Created collection for bob.test at /root/scripting/lansible/3collections/collections/ansible_collections/bob/test/bob-test-1.0.0.tar.gz
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections/ansible_collections/bob/test# ls
bob-test-1.0.0.tar.gz  docs  galaxy.yml  meta  plugins  README.md  roles
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections/ansible_collections/bob/test# ansible-galaxy collection install bob-test-1.0.0.tar.gz
[DEPRECATION WARNING]: ANSIBLE_COLLECTIONS_PATHS option, does not fit var naming standard, use the singular form
ANSIBLE_COLLECTIONS_PATH instead. This feature will be removed from ansible-core in version 2.19. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Installing 'bob.test:1.0.0' to '/root/scripting/lansible/3collections/collections/ansible_collections/bob/test/collections/ansible_collections/bob/test'
bob.test:1.0.0 was installed successfully
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections/ansible_collections/bob/test# ansible-galaxy collection list


# 1. grab token from https://galaxy.ansible.com/ to publish
# 2.  to download the collections
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections# cd ..
(venv) root@ubuntu03:~/scripting/lansible/3collections# ansible-galaxy collection download theurbanpenguin.utils
[DEPRECATION WARNING]: ANSIBLE_COLLECTIONS_PATHS option, does not fit var naming standard, use the singular form
ANSIBLE_COLLECTIONS_PATH instead. This feature will be removed from ansible-core in version 2.19. Deprecation warnings can be
 disabled by setting deprecation_warnings=False in ansible.cfg.
Process download dependency map
Starting collection download process to '/root/scripting/lansible/3collections/collections'
Downloading https://galaxy.ansible.com/api/v3/plugin/ansible/content/published/collections/artifacts/theurbanpenguin-utils-0.0.2.tar.gz to /root/.ansible/tmp/ansible-local-136106a5sajrze/tmpc2md9jt_/theurbanpenguin-utils-0.0.2-cfdxjeh2
Downloading collection 'theurbanpenguin.utils:0.0.2' to '/root/scripting/lansible/3collections/collections'
Collection 'theurbanpenguin.utils:0.0.2' was downloaded successfully
Writing requirements.yml file of downloaded collections to '/root/scripting/lansible/3collections/collections/requirements.yml'
# 3. Perform the changes 
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections# ls
ansible_collections  requirements.yml  theurbanpenguin-utils-0.0.2.tar.gz
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections# mkdir working
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections# cd working/
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections/working# tar -xf ../theurbanpenguin-utils-0.0.2.tar.gz
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections/working# ls
docs  FILES.json  MANIFEST.json  meta  plugins  README.md  roles
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections/working# vim galaxy.yml
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections/working#   ansible-galaxy collection build
[DEPRECATION WARNING]: ANSIBLE_COLLECTIONS_PATHS option, does not fit var naming standard, use the singular form
ANSIBLE_COLLECTIONS_PATH instead. This feature will be removed from ansible-core in version 2.19. Deprecation warnings can be
 disabled by setting deprecation_warnings=False in ansible.cfg.
Created collection for theurbanpengin.test at /root/scripting/lansible/3collections/collections/working/theurbanpengin-test-1.1.0.tar.gz
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections/working# cd ..
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections# ls
ansible_collections  requirements.yml  theurbanpenguin-utils-0.0.2.tar.gz  working
(venv) root@ubuntu03:~/scripting/lansible/3collections/collections# tree working/
working/
├── docs
├── FILES.json
├── galaxy.yml
├── MANIFEST.json
├── meta
│   └── runtime.yml
├── plugins
│   ├── modules
│   │   └── manage_hosts.py
│   └── README.md
├── README.md
├── roles
└── theurbanpengin-test-1.1.0.tar.gz

5 directories, 8 files
# 4. After performing changes and building tar ball update the ansible.cfg
(venv) root@ubuntu03:~/scripting/lansible/3collections# cat ansible.cfg
[defaults]
inventory = ./inventory/hosts
remote_user = im65
host_key_checking = False
roles_path = roles
collections_path = ./collections

[galaxy]
server_list = galaxy

[galaxy_server.galaxy]
url = https://galaxy.ansible.com/
token = 69.......31
# 5. publish the collections
ansible-galaxy collection publish collections/working/theurbanpengin-test-1.1.0.tar.gz

# 6. Install new version 
ansible-galaxy collection install --upgrade theurbanpengin.Utils

  ```

- 4Testing: Playbook testing

