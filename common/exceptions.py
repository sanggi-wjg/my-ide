import sys
import traceback


def brief_except():
    exc_type, exc_value, exc_tb = sys.exc_info()
    return "(Type) : {} | (Line) : {} | (Msg) : {}\n{}".format(exc_type.__name__, exc_tb.tb_lineno, exc_value, traceback.format_exc())
