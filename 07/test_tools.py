#!/usr/bin/env python3

import tools
import pytest


@pytest.fixture
def task_a(request):
    tools.Task.reset()
    return tools.Task.get('A')


def test_task(task_a):
    assert not task_a.finished
    assert task_a.name == 'A'
    assert task_a.is_ready()


def test_run_task(task_a):
    w = tools.Worker(offset=0)
    w.run(task_a)
    assert not w.free
    assert not task_a.finished
    w.click()
    assert w.free
    assert task_a.finished


def test_run_task_with_offset(task_a):
    w = tools.Worker(offset=10)
    w.run(task_a)
    assert not w.free
    assert not task_a.finished
    for _ in range(10):  # 10 offset + 1 from A
        w.click()
    assert not w.free
    assert not task_a.finished
    w.click()  # The last click
    assert w.free
    assert task_a.finished


def test_run_task_uncompleted(task_a):
    w = tools.Worker(offset=10)
    w.run(task_a)
    assert not w.free
    assert not task_a.finished
    for _ in range(5):
        w.click()
    assert not w.free
    assert not task_a.finished


def test_scheduler_simple():
    tools.Task.reset()
    a = tools.Task.get('A')
    b = tools.Task.get('B')
    sch = tools.Scheduler(num_workers=2, offset=0)
    sch.add(a)
    sch.add(b)
    assert len(sch.queue) == 2
    assert len(sch.available_workers()) == 2
    assert not a.finished
    assert not b.finished
    sch.run()
    assert len(sch.queue) == 0
    assert len(sch.available_workers()) == 0
    assert not a.finished
    assert not b.finished
    sch.run()
    assert len(sch.queue) == 0
    assert len(sch.available_workers()) == 1
    assert a.finished
    assert not b.finished
    sch.run()
    assert len(sch.queue) == 0
    assert len(sch.available_workers()) == 2
    assert a.finished
    assert b.finished


def test_scheduler_with_dependency():
    tools.Task.reset()
    a = tools.Task.get('A')
    b = tools.Task.get('B')
    c = tools.Task.get('C')
    c.requires.add(b)
    sch = tools.Scheduler(num_workers=2, offset=0)
    sch.add(a)
    sch.add(b)
    sch.add(c)
    for i in range(7):
        sch.run()
    assert a.finished
    assert b.finished
    assert c.finished
    assert len(sch.queue) == 0
    assert len(sch.available_workers()) == 2


if __name__ == '__main__':
    pytest.main()
