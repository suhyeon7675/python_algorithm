import numpy as np

def solution(score):
    mm = [np.mean(s) for s in score]
    return [sorted(mm, reverse=True).index(m)+1 for m in mm]