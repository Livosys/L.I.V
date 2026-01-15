# Exempel: mappa tenant/roll -> tillåtna kategorier
ACL = {
    "default": ["IT", "Nätverk"],
    "hr": ["HR"]
}

def allowed(category_name, tenant="default"):
    return category_name in ACL.get(tenant, [])
