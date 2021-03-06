'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Blackbox rmtoo test
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os
import time

from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, compare_results, \
    cleanup_std_log, delete_result_is_dir, extract_container_files, \
    check_file_results

mdir_orig = "tests/blackbox-test/bb001-test"
mdir = "tests/BlackboxTest/Bb001Test"

class TestBB001:

    def test_pos_001(self):
        "BB Basic with one requirement - reqs only from git"

        os.environ['TZ'] = 'Europe/Berlin'
        time.tzset()

        def myexit(n):
            pass

        os.environ["basedir"] = mdir_orig
        os.environ["rbasedir"] = mdir
        mout, merr = prepare_result_is_dir()
        main(["-j", "file://" + mdir + "/input/Config.json"],
             mout, merr, exitfun=myexit)
        cleanup_std_log(mout, merr)
        extract_container_files(["reqspricing.ods", ])
        check_file_results(mdir)
        delete_result_is_dir()
