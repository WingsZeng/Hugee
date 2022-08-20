import sublime
import sublime_plugin
import subprocess
from enum import IntEnum
from typing import Optional, List
from .settings import settings


class Status(IntEnum):
    """
    This class describes a command result status.
    """
    SUCCESS             = 0
    FAILED              = 1
    NOT_INSTALLED       = 2
    UNKNOWN             = -1


class Result(object):
    """
    This class describes a command result.
    """
    def __init__(self,
                 status: Status,
                 output: str,
                 e: Optional[Exception] = None) -> None:
        """
        Constructs a new instance.

        :param      status:  The result status
        :type       status:  Status
        :param      output:  The command output, including error out
        :type       output:  str
        :param      e:       If command did not execve successfully,
                             throw an exception
        :type       e:       Exception or None
        """
        self.status = status
        self.output = output
        self.e = e


def run(cmd: List[str]) -> Result:
    """
    Run a hugo command

    :param      cmd:  The command
    :type       cmd:  list of strings

    :returns:   Command Result
    :rtype:     Result
    """
    try:
        out = subprocess.check_output(cmd, cwd=settings.get('site_path'), universal_newlines=True, stderr=subprocess.STDOUT)
        return Result(Status.SUCCESS, out)
    except FileNotFoundError as e:
        return Result(Status.NOT_INSTALLED, 'Hugo not installed', e)
    except subprocess.CalledProcessError as e:
        return Result(Status.FAILED, e.output, e)
    except Exception as e:
        return Result(Status.UNKNOWN, str(e), e)
