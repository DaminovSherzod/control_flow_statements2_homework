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
    if a<b:
        print(b)
    if b<c: 
        print(c)
    if c<a:
        print(a)    
    return a<b, b<c, c<a
print(main(9,6,5)) 