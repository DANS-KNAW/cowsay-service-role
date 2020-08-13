cowsay-service-role
===================
Installs the Cowsay HTTP service. A toy example of an external Ansible role.

Requirements
------------
None

Role Variables
--------------

    cowsay_service:
        port: 5000 # Listen port for service

Dependencies
------------
Noe

Example Playbook
----------------

    - hosts: all
      become: yes
      roles:
         - role: cowsay-service-role
           cowsay_service:
                port: 5001

License
-------
Apache 2.0
