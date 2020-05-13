
from glob import glob
import os

import numpy as np

from motion import get_motion_parameters
from utils import check_folder
population = np.zeros((Config.pop_size, 15))
population[:, 0] = [x for x in range(Config.pop_size)]
