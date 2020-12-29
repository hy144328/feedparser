#!/usr/bin/env python3

import feedparser
from itertools import chain, permutations
import pytest

test_summary_args = ["content", "description", "summary"]

def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(permutations(s, r) for r in range(1, len(s)+1))

@pytest.mark.parametrize("a", list(powerset(test_summary_args)))
def test_summary(a):
    filename = "_".join(["tests/copy2summary/item"] + list(a)) + ".xml"
    with open(filename, 'r') as f:
        d = feedparser.parse(f.read())

    if "summary" in a:
        assert(d.entries[0].summary == "Example summary")
    elif "description" in a:
        assert(d.entries[0].summary == "Example description")
    elif "content" in a:
        assert(d.entries[0].summary == "Example content")
