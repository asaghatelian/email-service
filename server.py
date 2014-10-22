#!/usr/bin/env python
import os
from Email import Email

Email.config.update(
    DEBUG = False,
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    Email.run(host='0.0.0.0', port=port)