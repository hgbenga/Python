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
