<<<<<<< HEAD
"""
Runs clustering and processes all databased to selected representative periods
"""

import database_processing
import database_processing_v3
import database_processing_v3_1
import database_processing_v4_0
import clustering
import utils
from matplotlib import pyplot as pp

import sys

def run(run_clustering=True):

    if run_clustering:
        clustering.run() # cluster periods
    database_processing.process_all() # process Temoa 2 databases
    database_processing_v3.process_all() # process Temoa 3 databases
    database_processing_v3_1.process_all() # process Temoa 3.1 databases
    database_processing_v4_0.process_all() # process Temoa 4.0 databases

    print("All processing completed.")

    if utils.config['show_plots']:
        print("Showing plots.")
        pp.show()



if __name__ == "__main__":
    
    run_clustering = True
    if len(sys.argv) > 1 and sys.argv[1] == "--no-cluster":
        run_clustering = False

=======
"""
Runs clustering and processes all databases to selected representative periods.
"""

from . import database_processing
from . import database_processing_v3
from . import database_processing_v3_1
from . import database_processing_v4_0
from . import clustering
from . import utils

from matplotlib import pyplot as pp
import sys


def reset_state():
    clustering.reset()

    database_processing.reset()
    database_processing_v3.reset()
    database_processing_v3_1.reset()
    database_processing_v4_0.reset()


def run(run_clustering=True, input_path=None, output_path=None):
    # Reload config so changes made by the CANOE UI are picked up
    utils.reload_config()

    # Reset module state because we are no longer starting
    # a fresh Python subprocess for every run
    reset_state()

    if run_clustering:
        clustering.run()

    if input_path and output_path:
        for mod in [database_processing, database_processing_v3, database_processing_v3_1, database_processing_v4_0]:
            if mod.process_all(input_path, output_path):
                break
    else:
        database_processing.process_all()
        database_processing_v3.process_all()
        database_processing_v3_1.process_all()
        database_processing_v4_0.process_all()

    print("All processing completed.")

    if utils.config.get("show_plots", False):
        print("Showing plots.")
        pp.show()


if __name__ == "__main__":
    run_clustering = True

    if len(sys.argv) > 1 and sys.argv[1] == "--no-cluster":
        run_clustering = False

>>>>>>> 6c98caf79506f1ce6072d3299227126978eb6e30
    run(run_clustering)