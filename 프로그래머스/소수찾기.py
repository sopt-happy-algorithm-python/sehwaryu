Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(n):
    nums = [i for i in range(n+1)]
    for i in range(2, n+1):
        if not nums[i]:
            continue
        for j in range(i*i, n+1, i):
            nums[j] = 0
    return len([nums[i] for i in range(2, n+1) if nums[i]])

>>> 
