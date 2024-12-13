def freque(l):
    freq = {}
    for item in l:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    
    max_freq = max(freq.values())
    max_freq_elements = [item for item, count in freq.items() if count == max_freq]
    
    return max_freq, max_freq_elements

l = [1, 2, 4, 5, 5, 3, 5]
max_frequency, elements_with_max_frequency = freque(l)
print("Elements with Maximum Frequency:", elements_with_max_frequency)