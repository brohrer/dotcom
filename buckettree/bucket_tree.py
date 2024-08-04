import sys

MAX_VAL = sys.float_info.max
MIN_VAL = sys.float_info.min


class BucketTree:
    def __init__(self, max_buckets=100):
        self.bucket = Bucket()

        self.max_buckets = int(max_buckets)
        if self.max_buckets < 0:
            raise ValueError(
                f"'BucketTree.max_buckets' ({self.max_buckets}) " +
                "needs to be non-negative."
            )



    # def bin(self, val):


class Bucket:
    def __init__(self, lo=MIN_VAL, hi=MAX_VAL, level=0):
        # The low and high limits of the range for this bucket.
        # The range is inclusive of the low value and exclusive of the high value.
        self.lo = float(lo)
        self.hi = float(hi)

        if self.hi <= self.lo:
            raise ValueError(
                f"'Bucket.hi' ({self.hi}) needs to be higher than 'Bucket.lo' ({self.lo})."
            )

        # The depth of the bucket tree at which this node sits.
        self.level = int(level)
        if self.level < 0:
            raise ValueError(f"'Bucket.level' ({self.level}) needs to be non-negative.")

