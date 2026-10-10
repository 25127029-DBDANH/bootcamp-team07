"""Module translating string palindrome and reversal from C++ to Python."""
def reverse_string(s: str) -> str:
    """
    Reverse a string.
    Differences from C++:
    - In C++, std::string is mutable and can be reversed in-place with std::reverse().
    - In Python, str is immutable, so slicing s[::-1] creates and returns a new reversed string.
    """
    return s[::-1]
def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.
    Case-sensitive, empty string is considered a palindrome.
    Differences from C++:
    - Instead of using two-pointer loops or std::equal with rbegin(),
      Python allows concise equality checking: s == s[::-1].
    """
    return s == reverse_string(s)