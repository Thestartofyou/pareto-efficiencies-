def is_pareto_efficient(points):
    """
    Check if a set of points is Pareto efficient.
    
    Parameters:
    points (list of tuples): List of points, where each point is represented as a tuple of coordinates.
    
    Returns:
    list: List of indices of Pareto efficient points.
    """
    pareto_front = []
    for i, (x1, y1) in enumerate(points):
        is_pareto = True
        for j, (x2, y2) in enumerate(points):
            if i != j and x2 >= x1 and y2 >= y1:
                is_pareto = False
                break
        if is_pareto:
            pareto_front.append(i)
    return pareto_front

# Example usage
points = [(3, 6), (2, 7), (5, 4), (4, 5), (3, 3)]
pareto_front = is_pareto_efficient(points)
print("Pareto efficient points indices:", pareto_front)
print("Pareto efficient points:")
for i in pareto_front:
    print(points[i])
