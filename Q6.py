import unittest

def two_sum(lst, target):
    index = {}
    length = len(lst)
    for i in range(length):
        res = target - lst[i]
        if res in index:
            return [index[res], i]
        index[lst[i]] = i
    return -1 


# 測試模組，判斷函式是否順利執行，若都通過檢測會在最後印出"OK"，失敗則會顯示「實際輸出」與「預期輸出」的差別並印出Failed。
class TestStringMethods(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2 ,4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

if __name__ == '__main__':
    unittest.main()