#
"""
"""
import os
import yaml
from typing import Dict, List

class ConfigClient:
    """Configuration client responsible to build provided
    configurations from configuration folder.
    """

    def __init__(self, 
        paths: List = None):

        self.cfiles = list()
        for p in paths:
            self.cfiles += [os.path.join(p, f) 
                for f in os.listdir(p)]
    
    def build(self) -> Dict:
        """Build the configuration dictionary based on the
        provided yaml files inside config folder.
        """
        self.cfg = dict()
        for f in self.cfiles:
            fname = f.split("/")[-1] 
            key = fname.split(".")[0]
            stream = open(f, 'r')
            if ~(key in self.cfg.keys()):
                self.cfg[key] = yaml.load(stream, 
                    Loader=yaml.FullLoader)
            else:
                self.cfg[key].update(yaml.load(
                    stream, Loader=yaml.FullLoader))

        return self.cfg