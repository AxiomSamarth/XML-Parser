def find_child(root,nodes):
    if len(root)!=0:
        if len(root.attrib)!=0:
            for key in root.attrib.keys():
                if root.tag + "_" + key not in nodes:
                    nodes.append(root.tag + "_" + key)
        else:
            if root.tag not in nodes:
                nodes.append(root.tag)
        for child in root:
            find_child(child,nodes)
    else:
        if len(root.attrib)!=0:
            for key in root.attrib.keys():
                if root.tag + "_" + key not in nodes:
                    nodes.append(root.tag + "_" + key)
        else:
            if root.tag not in nodes:
                nodes.append(root.tag)