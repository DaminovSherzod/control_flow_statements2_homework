def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b and c<b:
        return b
    if b<c and a<c: 
        return c
    if c<a and b<a:
        return a    
print(main(1,6,9)) 