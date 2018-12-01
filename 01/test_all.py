import pytest
from part_02 import find_freq

data = [
    ([1, -1], 0),
    ([3, 3, 4, -2, -4], 10),
    ([-6, 3, 8, 5, -6], 5),
    ([7, 7, -2, -7, -4], 14),  
    ]

ids = [str(i) for i in range(1, len(data)+1)]

@pytest.fixture(params=data, ids=ids)
def sample(request):
    return request.param


def test_all(sample):
    seq, target = sample
    solution = find_freq(seq)
    assert solution == target


if __name__ == '__main__':
    pytest.main()
