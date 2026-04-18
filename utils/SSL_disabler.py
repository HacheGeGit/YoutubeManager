import certifi
import ssl

def disable_SSL():
    ssl._create_default_https_context = ssl._create_unverified_context
    ssl._create_default_https_context(cafile=certifi.where())