import logging
import logging.handlers
import sys
from pathlib import Path

import arrow

# Logger Configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream_formatter = logging.Formatter("%(asctime)s : %(funcName)s : %(levelname)s  : %(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_formatter)

# Add Stream Logger
logger.addHandler(stream_handler)

class ScriptEventLog:
    
    def __init__(self, log_dir_path: str = str(Path.cwd()), log_dir_name: str = "Logs", log_file_name: str = "ScriptLog",
                log_file_ext: str = ".log", *, use_file_rotation: bool = True):

        logger.debug(f"Script Events Log Directory Path: '{log_dir_path}'")
        logger.debug(f"Script Events Log Directory Name: '{log_dir_name}'")
        logger.debug(f"Script Events Log File Name: '{log_file_name}'")
        logger.debug(f"Script Events Log File Extension: '{log_file_ext}'")

        logger.debug(f"Use File Rotation: '{use_file_rotation}'")

        logger.debug("Configuring Log File Handler, to write script events to File")

        # Config Switches
        self.use_file_rotation = use_file_rotation

        # Directory
        self.log_dir_path = Path(log_dir_path)
        self.log_dir_name = log_dir_name
        self.log_dir_path = self._get_log_dir_path()

        # File    
        self.log_file_name = log_file_name
        self.log_file_ext = log_file_ext
        self.dated_log_file_name = self._generate_log_file_name()
        self.log_file_path = self.log_dir_path.joinpath(self.dated_log_file_name)

        self._setup_log_filehandler()

    def _get_log_dir_path(self):
        expected_log_dir_path = self.log_dir_path.joinpath(self.log_dir_name)

        try:
            if expected_log_dir_path.exists() == False:
                logger.info(f"Creating Log Directory at '{expected_log_dir_path}'")
                expected_log_dir_path.mkdir(parents=True, exist_ok=True)
            
            logger.debug(f"Using '{expected_log_dir_path}' as the log directory for the script")
            
            return expected_log_dir_path

        except Exception:
            logger.exception(f"Error While creating Log directory at {expected_log_dir_path}")
            logger.error(f"A directory named '{self.log_dir_name}' has to be present at the script location '{self.log_dir_path}', for writing logs.")
            logger.error("Exiting the Script")
            sys.exit()

    def _generate_log_file_name(self):
        if self.use_file_rotation == True:
            return f"{self.log_file_name}{self.log_file_ext}"
        else:
            return f"{self.log_file_name}_{arrow.now().format('YYYYMMDD')}{self.log_file_ext}"
            # return f"{self.log_file_name}_test{self.log_file_ext}"

    def _setup_log_filehandler(self):

        if self.use_file_rotation == True:
            file_handler = logging.handlers.RotatingFileHandler(filename=self.log_file_path, maxBytes=1048576, backupCount=5)
        else:
            file_handler = logging.FileHandler(filename=self.log_file_path)

        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter("%(asctime)s : %(funcName)s : %(levelname)s  : %(message)s")
        file_handler.setFormatter(file_formatter)

        logger.addHandler(file_handler)

        logger.debug(f"Log File Handler Successfully Configured, Writing Logs to File: '{self.log_file_path}'.")
        logger.info("") # Writing Blank line as the first line, to file
        logger.info("### Script Started ###")


if __name__ == "__main__":
    script_log_obj = ScriptEventLog()
