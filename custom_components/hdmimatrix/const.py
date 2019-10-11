"""Constants for hdmimatrix."""
# Base component constants
DOMAIN = "hdmimatrix"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
PLATFORMS = ["binary_sensor", "sensor", "switch"]
REQUIRED_FILES = [
    ".translations/en.json",
    "binary_sensor.py",
    "const.py",
    "config_flow.py",
    "manifest.json",
    "sensor.py",
    "switch.py",
]
ISSUE_URL = "https://github.com/troykelly/homeassistant-generic-hdmimatrix/issues"
ATTRIBUTION = "Data from this is provided by hdmimatrix."

# Icons
ICON = "mdi:video-input-hdmi"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Configuration
CONF_BINARY_SENSOR = "binary_sensor"
CONF_SENSOR = "sensor"
CONF_SWITCH = "switch"
CONF_ENABLED = "enabled"
CONF_NAME = "name"
CONF_HOSTNAME = "hostname"
CONF_PORT = "port"

# Defaults
DEFAULT_NAME = DOMAIN
DEFAULT_PORT = 8000
