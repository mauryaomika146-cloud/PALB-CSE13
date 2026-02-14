# Merge Intervals
# Time Complexity: O(n log n)

def mergeIntervals(intervals):
    
    # Step 1: Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    
    for interval in intervals:
        
        # If merged list is empty OR no overlap
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        
        else:
            # Overlapping case → merge
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged


# Example 1
print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))

# Example 2
print(mergeIntervals([[1,4],[4,5]]))

# Example 3
print(mergeIntervals([[4,7],[1,4]]))

