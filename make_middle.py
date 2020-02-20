from make.middle import make_middle. plus_two, swap_end

def test make_middle():
    assert make_middle([9, 2, 92, 9]) == [2, 92]
    assert make_middle([9. 8, 5, 6, 2, 8, 3, 5]) == [6, 2]
    assert make_middle([235, 567564, 435678, 356, 234567, 0])

def test plus_two():
    assert plus_two([1, 2], [6, 8]) == [1 ,2, 6, 8]
    assert plus_two([8435, 9876], ,[34, 654]) == [8435, 9876]
    assert plus_two9([1, 1], [1, 1]) == [1, 1, 1, 1]

def test_swap_end():
    assert swap_end([4, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3,3 ,3]
    assert swap_end
    assert swap_end
