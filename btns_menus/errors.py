from typing import *


class PaginatorException(Exception):
    """
    Exceptions related to Paginator
    """

    pass


class ButtonException(Exception):
    """
    Exceptions related to Buttons
    """

    pass


class MenuException(Exception):
    """
    Exceptions related to DropMenus
    """

    pass


class MissingAdminPerms(ButtonException):
    def __init__(self):
        """
        Raises this exception if a user does not have admin perms
        """

        super().__init__("To interact with this button, you should be the Guild Owner !")


class MissingPerms(ButtonException):
    def __init__(self, perms: List[str]):
        """
        Raises this exception if a user does not have required perms

        Args:
            perms: list of missing permissions
        """

        error_ = f"To interact with this Button/Menu, you need {', '.join(perms)} perm(s)"
        super().__init__(error_)


class MissingRoles(ButtonException):
    def __init__(self, roles: List[str]):
        """
        Raises this exception if a user does not have required roles

        Args:
            roles: list of missing roles
        """
        error_ = f"To interact with this Button/Menu, you need {', '.join(roles)} role(s)"
        super().__init__(error_)


class MissingAnyRole(ButtonException):
    def __init__(self, roles: List[str]):
        """
        Raises this exception if a user does not have any one of the required roles

        Args:
            roles: list of missing roles
        """

        error_ = f"To interact with this Button/Menu, you need any one of the this {', '.join(roles)} role(s)"
        super().__init__(error_)


class InvalidInteractionUser(ButtonException):
    def __init__(self, current_user: str):
        """
        Raises this exception if a user is not same as interaction.user

        Args:
            current_user: user of the particular interaction
        """

        error_ = f"Only the {current_user} can access/use this Button/Menu"
        super().__init__(error_)


class NotInUsers(ButtonException):
    def __init__(self, users: List[str]):
        """
        Raises this exception if a user is not in any one of the given users

        Args:
            users: list of valid users
        """

        error_ = f"Only the {', '.join(users)} user(s) can access/use this Button/Menu"
        super().__init__(error_)
