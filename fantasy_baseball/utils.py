from lxml import etree

def remove_namespaces_qname(doc, namespaces=None):
    for el in doc.getiterator():
        # clean tag
        q = etree.QName(el.tag)
        if q is not None:
            if namespaces is not None:
                if q.namespace in namespaces:
                    el.tag = q.localname
            else:
                el.tag = q.localname
            # clean attributes
            for a, v in el.items():
                q = etree.QName(a)
                if q is not None:
                    if namespaces is not None:
                        if q.namespace in namespaces:
                            del el.attrib[a]
                            el.attrib[q.localname] = v
                    else:
                        del el.attrib[a]
                        el.attrib[q.localname] = v
    return doc