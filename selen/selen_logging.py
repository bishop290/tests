# -*- coding: utf-8 -*-

import logging
from datetime import datetime


def log_save(selen_test:object, str_log:str, log_level:str):
    logging.basicConfig(filename=selen_test.logfile_fullpath, level=logging.INFO)

    log_str_tmpl = "{0}:: {1}".format(datetime.now(), str_log)

    if (log_level == "info"): logging.info(log_str_tmpl)
    elif (log_level == "debug"): logging.debug(log_str_tmpl)
    elif (log_level == "error"): logging.error(log_str_tmpl)
    

    
