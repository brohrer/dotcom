import sys
from bucket_tree.bucket_tree import BucketTree, Bucket


def test_bucket_initialization():
    bucket = Bucket(lo=-1.0, hi=1.0, level=2)
    assert type(bucket.lo) == float
    assert bucket.lo == -1.0
    assert type(bucket.hi) == float
    assert bucket.hi == 1.0
    assert type(bucket.level) == int
    assert bucket.level == 2


def test_bucket_bounds():
    caught = False
    try:
        bucket = Bucket(lo=10.0, hi=-10.0)
    except ValueError:
        caught = True
    assert caught

    caught = False
    try:
        bucket = Bucket(level=-3)
    except ValueError:
        caught = True
    assert caught


def test_bucket_tree_initialization():
    bt = BucketTree()
    assert bt.max_bins == 100
    assert bt.root.lo == sys.float_info.min
    assert bt.root.hi == sys.float_info.max
    assert bt.root.level == 0


def test_bucket_tree_bounds():
    caught = False
    try:
        bt = BucketTree(max_bins=-100)
    except ValueError:
        caught = True
    assert caught


# def test_bucket_tree_bins()
