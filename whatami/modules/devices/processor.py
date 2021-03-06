"""Processor module."""
from .. import base
from .. import util


class Processor(base.Module):
    """Processor class."""

    def __init__(self):
        """Initialization."""
        super(Processor, self).__init__()
        self.order = 100
        self.cpus = self._get_cpu_total()
        self.model = self._get_model()

    def __str__(self):
        """Return string with the nubmer and type of processors."""
        return "%sx %s" % (self.cpus, self.model)

    @staticmethod
    def _get_cpu_total():
        """Report total number of processors."""
        cpuinfo = util.readfile('/proc/cpuinfo')
        return cpuinfo.count('processor')

    @staticmethod
    def _get_model():
        """Report total swap value."""
        cpuinfo = util.readfile('/proc/cpuinfo')
        return util.firstmatch(r'model name.*\s: (.+?)\n', cpuinfo)

    def to_json(self):
        """Return dictionary like item for JSON output."""
        return {
            "processor": {
                "qty": self.cpus,
                "model": self.model
            }
        }
