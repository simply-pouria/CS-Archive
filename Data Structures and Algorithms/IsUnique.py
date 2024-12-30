def unique_elements(arr):
    # Create an empty hash set
    seen = set()
    for x in arr:
        if x in seen:
            return False
        seen.add(x)
    return True


s = input()
s = s.split()
s = map(int, s)
if unique_elements(s):
    print('unique')
else:
    print('not unique')





