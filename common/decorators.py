import functools
import logging
from typing import Callable, Tuple

from django.http import JsonResponse

from common.exceptions import brief_except
from common.utils import valid_dir


def catch_error(catch_exceptions: Tuple):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            try:
                return func(request, *args, **kwargs)
            except catch_exceptions as e:
                logging.critical(brief_except())

        return wrapper

    return decorator


def catch_rest_api_error(catch_exceptions: Tuple):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            try:
                return func(request, *args, **kwargs)
            except catch_exceptions as e:
                logging.error(brief_except())
                return JsonResponse({ })

        return wrapper

    return decorator

# def validate_dir_root(dirpath: str):
#     def decorator(func: Callable):
#         @functools.wraps(func)
#         def wrapper(request, *args, **kwargs):
#             try:
#                 valid_dir(dirpath)
#                 return func(request, *args, **kwargs)
#             except Exception as e:
#                 logging.error(brief_except())
#
#         return wrapper
#
#     return decorator
