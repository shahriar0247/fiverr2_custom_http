import re

def search_strings(str_list, search_query):
    regex = re.compile(search_query)
    result = []
    for string in str_list:
        match = regex.match(string)
        if match is not None:
            result+=[match.group()]
    return result

strList= ['obj_1_mesh',
          'obj_2_mesh',
          'obj_TMP',
          'mesh_1_TMP',
          'mesh_2_TMP',
          'meshTMP']
