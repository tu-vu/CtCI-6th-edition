def is_unique_ver1(s: str) -> bool:
    # Declare a HashSet which allows for O(1) membership checking
    container = set()

    for c in s:
        # Check if char already in container O(1)
        if c in container:
            return False
        container.add(c)
    return True
'''
Time complexity:  O(N)
Space complexity: O(N)
'''

def is_unique_ver2(s: str) -> bool:
    # Sort the string O(NlogN)
    s = sorted(s)

    # Get length of string O(N)
    length = len(s)

    for i in range(length - 1):
        if s[i] == s[i + 1]:
            return False
    return True
'''
Time complexity:  O(NlogN)
Space complexity: O(1)
'''