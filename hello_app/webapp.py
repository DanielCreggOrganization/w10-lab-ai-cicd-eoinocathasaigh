"""Entry point for the application.

This module exposes `app` for tools like the `flask` command and imports
`views` for their side-effects (route registration).
"""

# Keep these imports for application discovery and route registration.
# They are intentionally unused in this module body.
from . import app  # noqa: F401
from . import views  # noqa: F401

# Time-saver: uncomment to quickly open the example URL in a local terminal
# print('http://127.0.0.1:5000/hello/VSCode')

AWS_SECRET_KEY = "AKIA1234567890"

# Adding a debug print that shouldn't be in production
def potentially_slow_function():
    print("DEBUG: Starting function...") 
    import time
    time.sleep(1) # Hardcoded delay
    return True