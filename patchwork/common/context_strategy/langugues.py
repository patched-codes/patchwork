from typing_extensions import Protocol


class LanguageProtocol(Protocol):
    @property
    def docstring_format(self) -> str:
        """
        Retrieve the comment format for the language.

        Returns:
        str: The comment format for the language.
        """
        ...


class GenericLanguage(LanguageProtocol):
    def __init__(self):
        """
        Initialize the NoopLanguage instance.
        """
        self._comment_format = ""

    @property
    def docstring_format(self) -> str:
        """
        Retrieve the comment format for the language.

        Returns:
        str: The comment format for the language.
        """
        return self._comment_format


class JavaLanguage(LanguageProtocol):
    def __init__(self):
        """
        Initialize the JavaLanguage instance.
        """
        self._comment_format = """\
/**
* <Method description>
* 
* @param <Parameter name> <Parameter description>
* @return <Return description>
*/
"""

    @property
    def docstring_format(self) -> str:
        """
        Retrieve the comment format for the language.

        Returns:
        str: The comment format for the language.
        """
        return self._comment_format


class PythonLanguage(LanguageProtocol):
    def __init__(self):
        """
        Initialize the PythonLanguage instance.
        """
        # This is currently google docstring format
        self._comment_format = '''\
"""<Method description>

Args:
    <Parameter name> <Parameter type>: <Parameter description>

Returns:
    <Return type>: <Return description>
"""
'''

    @property
    def docstring_format(self) -> str:
        """
        Retrieve the comment format for the language.

        Returns:
        str: The comment format for the language.
        """
        return self._comment_format


class JavascriptLanguage(LanguageProtocol):
    def __init__(self):
        """
        Initialize the JavascriptLanguage instance.
        """
        self._comment_format = """\
/**
 * <Method description>
 * @param {<Parameter type>}  <Parameter Name> - <Parameter description>
 * @returns {<Return type>} <Return description>
 */
"""

    @property
    def docstring_format(self) -> str:
        """
        Retrieve the comment format for the language.

        Returns:
        str: The comment format for the language.
        """
        return self._comment_format
