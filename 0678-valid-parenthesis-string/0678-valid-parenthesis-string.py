class Solution:
    def checkValidString(self, s: str) -> bool:

        def _check_valid_string(s, pool:set):
            _count = 0
            for char in s:
                _count += 1 if char in pool else -1
                if _count < 0:
                    return False
            return True

        return _check_valid_string(s, {'(', '*'}) and _check_valid_string(s[::-1], {')', '*'})
