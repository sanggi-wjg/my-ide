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


