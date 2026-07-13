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

def run():

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

    run()