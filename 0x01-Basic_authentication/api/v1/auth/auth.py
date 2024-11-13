#!/user/bin/env python3
""" Authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth Class
    """
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """ Require auth
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        path = path.rstrip("/")
        return path not in [p.rstrip("/") for p in excluded_paths]

    def authorization_header(self, request=None) -> str:
        """ Authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User
        """
        return None
