#!/usr/bin/env python3

def _zero_pos_neg_sort(seq):
    return sorted(seq, key=lambda x: (0 if x == 0 else 1 if x > 0 else 2, x))

def join_lists(l1, l2):
    return _zero_pos_neg_sort(set(l1).union(l2))

def match_lists(l1, l2):
    return sorted(set(l1).intersection(l2))

def diff_lists(l1, l2):
    return _zero_pos_neg_sort(set(l1).symmetric_difference(l2))

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))
