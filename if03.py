def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<=b and b<=c and a<=c:
        return b
    if a<=c and c<=b and a<=b:
        return c
    if c<=a and a<=b and c<=b:
        return a   
    if b<=c and c<=a and b<=a:
        return c    
    if b<=a and a<=c and b<=c:
        return a    
    if c<=b and b<=a and c<=a:
        return b      
print(main(3,1,2))        