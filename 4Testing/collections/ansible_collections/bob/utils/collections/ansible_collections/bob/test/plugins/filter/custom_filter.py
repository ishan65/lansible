from ansible.errors import AnsibleFilterError


class FilterModule:
    """
    A class defining a custom Ansible filter plugin.

    This plugin provides a filter that converts a given string to uppercase.
    """

    def filters(self):
        """
        Returns a mapping of filter names to filter methods.

        :return: A dictionary with filter names as keys and the corresponding
                 filter functions as values.
        :rtype: dict
        """
        return {
            "upper_case": self.to_upper,
        }

    def to_upper(self, value):
        """
        Converts the given string to uppercase.

        :param value: The input string to be converted.
        :type value: str
        :return: The input string converted to uppercase.
        :rtype: str
        :raises AnsibleFilterError: If the input value is not a string.
        """
        if not isinstance(value, str):
            raise AnsibleFilterError("upper_case expects a string")
        return value.upper()
