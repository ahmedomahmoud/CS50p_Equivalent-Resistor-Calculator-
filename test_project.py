from project import check_in , series , parallel

def test_check_in():
    assert check_in(["1","2","3","4"])==False
    assert check_in([])==False
    assert check_in(["A","b","2","3"])==False
    assert check_in(["1","2","30"])==True

def test_parallel():
    assert parallel([[1,2,1],[2,3,1],[2,4,2],[3,4,2],[3,4,2]])==[[1,2,1],[2,3,1],[2,4,2],[3,4,1]]
    assert parallel([[1,2,2],[1,2,2],[2,3,2],[3,4,4],[3,4,4]])==[[2,3,2],[3,4,2],[1,2,1]]

def test_series():
    assert series([[1,2,1],[2,3,1],[2,4,2],[3,4,1]])==[[1,2,1],[2,4,2],[2,4,2]]
    assert series([[2,3,2],[3,4,2],[1,2,1]])==[[1,4,5]]