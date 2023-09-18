from typing import List
def getFrequencies(v: List[int]) -> List[int]: 
    d={}
    res=[0, 0]
    for ele in v:
        d[ele]=d.get(ele, 0)+1
    # Find the maximum frequency
    max_freq = max(d.values())
    # Find the minimum frequency
    min_freq = min(d.values())
    # Find elements corresponding to maximum and minimum frequencies
    max_freq_elements = [ele for ele, freq in d.items() if freq == max_freq]
    min_freq_elements = [ele for ele, freq in d.items() if freq == min_freq]
    #return minimum of both the two frequency list
    return [min(max_freq_elements),min(min_freq_elements)]