import os
import sys
from platformdirs import PlatformDirs

def is_bundled() -> bool:
    """Check if we're running as a bundled executable"""
    return getattr(sys, 'frozen', False)

# Set up directories based on whether we're running as exe or not
if is_bundled():
    # Running as compiled executable - use platform-specific dirs
    dirs = PlatformDirs("CANOE", "RSSSelector")
    CONFIG_DIR = dirs.user_config_path
    LOG_DIR = dirs.user_log_path
else:
    # Running as Python script - use local dirs
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_DIR = os.path.join(BASE_DIR, "input")
    LOG_DIR = os.path.join(BASE_DIR, "logs")

# Ensure directories exist
os.makedirs(CONFIG_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# File paths
CONFIG_FILE: str = os.path.join(CONFIG_DIR, "config.json")
"""File location for saved configuration of UI options"""