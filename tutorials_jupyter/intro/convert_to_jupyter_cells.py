'''
This script converts a tutorial to support jupyter cells and adds a "open in colab" batch
'''

# System imports
import argparse
from pathlib import Path

# 3rd party imports

# local imports

# end file header
__author__      = 'Adrian Lubitz'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_folder", help="Path to the folder which holds the tutorial", type=str)
    parser.add_argument(
        "output_folder", help="Path to where to save the jupyter cell extendet tutorials to.", type=str)
    parser.add_argument(
        "github_user", help="user or organization that holds the mne-python repo(normally this is mne-tools - but for forks this can vary)", type=str)
    args = parser.parse_args()