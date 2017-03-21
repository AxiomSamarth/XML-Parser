def find_child_contents(root, li):
    if len(root)!=0:
        if len(root.attrib)!=0:
            for key in root.attrib.keys():
                if ',' in root.attrib[key]:
                    '''content = root.attrib[key][:root.attrib[key].index(',')]
                    content = str(content)+" and "+str(root.attrib[key][1+root.attrib[key].index(','):])
                    li.append(content)'''

                    root.attrib[key] = list(root.attrib[key])
                    root.attrib[key] = [i for i in root.attrib[key] if i!=',']
                    root.attrib[key] = ('').join(root.attrib[key])
                    li.append(root.attrib[key].strip())

                else:
                    li.append(root.attrib[key].strip())
        else:
                if ',' in root.text:
                    content = root.text[:root.text.index(',')]
                    content = str(content)+" and "+str(root.text[1+root.text.index(','):])
                    li.append(content.strip())
                else:
                    li.append(root.text.strip())
        for child in root:
            find_child_contents(child,li)
    else:
        if len(root.attrib)!=0:
            for key in root.attrib.keys():
                if ',' in root.attrib[key]:
                    '''content = root.attrib[key][:root.attrib[key].index(',')]
                    content = str(content)+" and "+str(root.attrib[key][1+root.attrib[key].index(','):])
                    li.append(content)'''
                    root.attrib[key] = list(root.attrib[key])
                    root.attrib[key] = [i for i in root.attrib[key] if i!=',']
                    root.attrib[key] = ('').join(root.attrib[key])
                    li.append(root.attrib[key].strip())
                else:
                    li.append(root.attrib[key].strip())
        else:
                #print root.tag
                try:
                    if ',' in root.text:
                        content = root.text[:root.text.index(',')]
                        content = str(content)+" and "+str(root.text[1+root.text.index(','):])
                        li.append(content.strip())
                    else:
                        li.append(root.text.strip())
                except Exception as e:
                    pass