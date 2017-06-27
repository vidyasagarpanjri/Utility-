import pefile

def display_all_imports(filename):
    exe = pefile.PE(filename)
    #for dd in exe.OPTIONAL_HEADER.DATA_DIRECTORY:
    for dd in exe.DIRECTORY_ENTRY_IMPORT:
        print dd.dll
        for im in dd.imports:
            print "\t",im.name
    return exe
