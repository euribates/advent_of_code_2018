import pytest
import tools

def test_use_double_list():
    dl = tools.DL()
    for i in range(4):
        dl.append(i)
    assert [n.value for n in dl] == [0, 1, 2, 3]


samples = [
    dict(input='dabAcCaCBAcCcaDA', output='dabCBAcaDA'),
    dict(input='a', output='a'),
    dict(input='aabAAB', output='aabAAB'),
    dict(input='abBA', output=''),
    dict(input='abAB', output='abAB'),
    dict(input='aA', output=''),
    dict(input='aAXXzA', output='XXzA'),
    dict(input='RAXXzZ', output='RAXX'),
    dict(input='RAXXzZQWER', output='RAXXQWER'),
    dict(input='MRraAxXXxzZqQWweERrU', output='MU'),
    ]
ids = ['{}->{}'.format(d['input'], d['output']) for d in samples]


@pytest.fixture(params=samples, ids=ids)
def sample(request):
    return request.param


def test_react(sample):
    sequence = sample['input']
    target = sample['output']
    dl = tools.DL(sequence)
    num_changes = -1
    while num_changes != 0:
        num_changes = 0
        for n in dl:
            num_changes += dl.react(n)
    assert str(dl) == target
    assert len(dl) == len(target)
