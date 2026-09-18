#!/usr/bin/env python3
import platform
import sys
from datetime import datetime, timezone

print("=== DevOps Automation Validation ===")
print(f"Timestamp UTC : {datetime.now(timezone.utc).isoformat()}")
print(f"Python        : {platform.python_version()}")
print(f"OS            : {platform.system()} {platform.release()}")

required_major = 3
if sys.version_info.major != required_major:
    print("STATUS        : FAIL - Python 3 is required")
    raise SystemExit(1)

print("STATUS        : PASS")
