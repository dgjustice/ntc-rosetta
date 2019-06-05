"""Helper for junos parsers"""
from typing import List


def resolve_vlan_ids(vlans: List, root) -> List[int]:
    """Resolve named vlans from /configuration/vlans/vlan path"""
    rv = list()
    for vlan in vlans:
        elem = root["dev_conf"].xpath(
            "//vlan[name/text()='{member}']/vlan-id".format(member=vlan.text)
        )
        if elem is not None:
            rv.append(int(elem[0].text))
    return rv
