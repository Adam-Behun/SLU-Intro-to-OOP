def isSubstring(pattern , original):
    
    start = 0
    end = 0
    while start < len(original):
        if original[start+end] != pattern[end]:
            start += 1
            end = 0
            continue
        end += 1
        if end == len(pattern):
            return start
    return -1
         
        


if isSubstring("of","class oooof 2020") > 0:
    print(True)
else:
    print(False)
