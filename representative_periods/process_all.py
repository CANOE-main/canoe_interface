"""
Runs clustering and processes all databases to selected representative periods.
"""

import sys
import os
from matplotlib import pyplot as pp

# Add root directory to path to allow running standalone
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from representative_periods import database_processing_v4_0 as dbp_v4
from representative_periods import clustering
from representative_periods import utils

def reset_state():
    clustering.reset()
    dbp_v4.reset()

def run(run_clustering=True, input_path=None, output_path=None):
    # Reload config so changes made by the CANOE UI are picked up
    utils.reload_config()

    # Reset module state because we are no longer starting
    # a fresh Python subprocess for every run
    reset_state()

    if run_clustering:
        clustering.run()

    if input_path and output_path:
        dbp_v4.process_all(input_path, output_path)
    else:
        root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # process all sqlite files in the root
        processed_any = False
        for file in os.listdir(root_dir):
            if file.endswith(".sqlite"):
                input_file = os.path.join(root_dir, file)
                output_file = os.path.join(root_dir, file.replace(".sqlite", "_processed.sqlite"))
                if dbp_v4._get_schema_version_for_path(input_file) == 4:
                    print(f"Processing {input_file}...")
                    dbp_v4.process_database(database=None, input_path=input_file, output_path=output_file)
                    processed_any = True
        
        if not processed_any:
            # Fallback to the original v4_0 parameterless method if no valid v4 databases in root
            dbp_v4.process_all()

    print("All processing completed.")

    if utils.config.get("show_plots", False):
        print("Showing plots.")
        pp.show()

if __name__ == "__main__":
    run_clustering = True

    if len(sys.argv) > 1 and sys.argv[1] == "--no-cluster":
        run_clustering = False

    run(run_clustering)