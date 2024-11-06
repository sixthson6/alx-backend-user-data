#!/usr/bin/env python3
"""Log messages obfuscated"""

from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """log messages obfuscated"""
    for field in fields:
        match = re.sub(rf'{field}=.+?{separator}',
                       f'{field}={redaction}{separator}', message)
    return match
