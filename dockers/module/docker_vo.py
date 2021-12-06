from collections import namedtuple

DockerfileInfo = namedtuple(
    'DockerfileInfo',
    ['dirpath', 'filepath', 'image_name', 'image_tag']
)

Dockers = namedtuple(
    'Dockers.json',
    ['image_name', 'image_tag', 'local_port']
)

# class DockerfileInfo(object):
#
#     def __init__(self):
#         self._dirpath = ''
#         self._filepath = ''
#         self._image_name = ''
#         self._image_tag = ''
#
#     @property
#     def dirpath(self):
#         return self._dirpath
#
#     @property
#     def filepath(self):
#         return self.filepath
#
#     @property
#     def image_name(self):
#         return self._image_name
#
#     @property
#     def image_tag(self):
#         return self.image_tag
