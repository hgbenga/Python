arista_vlan.yml
==========================================

---

- name: Create Arista VLANs
  hosts: arista

  tasks:
    - name: Configure EXECUTIVE VLAN
      eos_vlan: name=EXECUTIVE vlanid=401
            eapi_username={{ eapi_username }}
            eapi_password={{ eapi_password }}
            eapi_hostname={{ eapi_hostname }}
            eapi_port={{ eapi_port }}

    - name: Configure IT VLAN
      eos_vlan: name=IT vlanid=402
            eapi_username={{ eapi_username }}
            eapi_password={{ eapi_password }}
            eapi_hostname={{ eapi_hostname }}
            eapi_port={{ eapi_port }}


    - name: Configure SALES VLAN
      eos_vlan: name=SALES vlanid=403
            eapi_username={{ eapi_username }}
            eapi_password={{ eapi_password }}
            eapi_hostname={{ eapi_hostname }}
            eapi_port={{ eapi_port }}


    - name: Setting Primary Interface Ethernet7 description as In USE
      eos_interface: name=Ethernet7 description="*** IN USE ***"
            eapi_username={{ eapi_username }}
            eapi_password={{ eapi_password }}
            eapi_hostname={{ eapi_hostname }}
            eapi_port={{ eapi_port }}


    - name: Set Ethernet7 to trunk mode and allow VLAN401,402,403
      eos_switchport: name=Ethernet7 mode=trunk trunk_allowed_vlans=401,402,403 trunk_native_vlan=1
            eapi_username={{ eapi_username }}
            eapi_password={{ eapi_password }}
            eapi_hostname={{ eapi_hostname }}
            eapi_port={{ eapi_port }}
            
            
            
  arista_coomand.yml
  ===================================
  
  ---

- name: Arista Ansible testing
  hosts: arista

  tasks:
    - name: Testing command (not idempotent)
      eos_command: commands="write memory"
        eapi_username={{ eapi_username }}
                eapi_password={{ eapi_password }}
                eapi_hostname={{ eapi_hostname }}
                eapi_port={{ eapi_port }}
      register: cmd_out
    - debug: var=cmd_out


arista_cleanup.yml
=======================================

---

- name: Arista Ansible testing
  hosts: arista

  tasks:
    - name: Testing command (not idempotent)
      eos_command: commands="write memory"
        eapi_username={{ eapi_username }}
                eapi_password={{ eapi_password }}
                eapi_hostname={{ eapi_hostname }}
                eapi_port={{ eapi_port }}
      register: cmd_out
    - debug: var=cmd_out
(applied_python)[ohassan@ip-172-30-0-134 ARISTA]$ cat arista_cleanup.yml
---

- name: Arista Cleanup
  hosts: arista

  tasks:
    - name: Configure Ethernet7 for access mode, VLAN1
      eos_switchport: name=Ethernet7 mode=access access_vlan=1 trunk_allowed_vlans=all trunk_native_vlan=1
            eapi_username={{ eapi_username }}
            eapi_password={{ eapi_password }}
            eapi_hostname={{ eapi_hostname }}
            eapi_port={{ eapi_port }}

    - name: Setting Ethernet7 description
      eos_interface: name=Ethernet7 admin=enable null_as_default=true
            eapi_username={{ eapi_username }}
            eapi_password={{ eapi_password }}
            eapi_hostname={{ eapi_hostname }}
            eapi_port={{ eapi_port }}

    - name: Remove VLANs
      eos_vlan: name={{ item.name }} vlanid={{ item.vlanid }} state=unconfigured
            eapi_username={{ eapi_username }}
            eapi_password={{ eapi_password }}
            eapi_hostname={{ eapi_hostname }}
            eapi_port={{ eapi_port }}
      with_items:
         - {name: EXECUTIVE, vlanid: 401}
         - {name: IT, vlanid: 402}
         - {name: SALES, vlanid: 403}

