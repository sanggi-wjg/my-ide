class DockersAppException(Exception):
    pass

class DockersModuleException(DockersAppException):
    pass

class DockerfileIsNotExist(DockersModuleException):
    pass

class DockerImageIsNotExist(DockersModuleException):
    pass

class DockerImageDuplicateExist(DockersModuleException):
    pass

def brief_except():
    import sys
    import traceback
    exc_type, exc_value, exc_tb = sys.exc_info()
    return "(Type) : {} | (Line) : {} | (Msg) : {}\n{}".format(exc_type.__name__, exc_tb.tb_lineno, exc_value, traceback.format_exc())
