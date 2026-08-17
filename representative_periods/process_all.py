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

    run(run_clustering)