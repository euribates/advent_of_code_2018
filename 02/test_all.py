#!/usr/binenv python3

import pytest
import part_01
import part_02


def test_abddef():
    assert part_01.count_for('abcdef', 2) == 0
    assert part_01.count_for('abcdef', 3) == 0


def test_bababc():
    """bababc contains two a and three b, so it counts for both."""
    assert part_01.count_for('bababc', 2) == 1
    assert part_01.count_for('bababc', 3) == 1


def test_abbcde():
    """abbcde contains two b, but no letter appears exactly three times.
    """
    assert part_01.count_for('abbcde', 2) == 1
    assert part_01.count_for('abbcde', 3) == 0


def test_abcccd():
    """abcccd contains three c, but no letter appears exactly two times.
    """
    assert part_01.count_for('abcccd', 2) == 0
    assert part_01.count_for('abcccd', 3) == 1


def test_aabcdd():    
    """aabcdd contains two a and two d, but it only counts once.
    """
    assert part_01.count_for('abbcdd', 2) == 1
    assert part_01.count_for('aabcdd', 3) == 0


def test_abcdee():
    """abcdee contains two e.
    """
    assert part_01.count_for('abcdee', 2) == 1
    assert part_01.count_for('abcdee', 3) == 0


def test_ababab():
    """ababab contains three a and three b, but it only counts once.
    """
    assert part_01.count_for('ababab', 2) == 0
    assert part_01.count_for('ababab', 3) == 1
        

part2_examples = [
    (('abcde', 'axcye'), (False, -1)),
    (('fghij', 'fguij '), (True, 2)),
    ]

part2_descriptions = [
    "The IDs abcde and axcye are close, but they differ by two characters",
    "the IDs fghij and fguij differ by exactly one character, the third",
    ]


@pytest.fixture(params=part2_examples, ids=part2_descriptions)
def part2(request):
    return request.param


def test_find_one_diff(part2):
    ((seq_a, seq_b), (flag, index)) = part2
    result = part_02.find_one_diff(seq_a, seq_b)
    assert result[0] is flag
    assert result[1] == index


    """
    (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example 
"""

if __name__ == '__main__':
    pytest.main()
