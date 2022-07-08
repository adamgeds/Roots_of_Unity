import cmath

# Takes in a complex number z and a real number n.
# Returns the nth roots of unity of z in a list roots[].
def get_roots_of_unity(z, n):
    z = z
    r_nth_root = (cmath.polar(z)[0]) ** (1/n) # Nth root of |z|
    theta = cmath.polar(z)[1] # Arg(z)
    roots = []

    for i in range(n):
        roots.append(r_nth_root * complex(cmath.cos((theta + 2*cmath.pi*i)/n), cmath.sin((theta + 2*cmath.pi*i)/n)))

    return roots

def main():
    print(get_roots_of_unity(complex(2, 3), 5))
 
if __name__ == '__main__':
    main()
