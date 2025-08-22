class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def insert_term(self, coeff, power):
        new_node = Node(coeff, power)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        if not current:
            print("0")
            return
        while current:
            print(f"{current.coeff}x^{current.power}", end=" + " if current.next else "")
            current = current.next
        print()

def add_polynomials(p1, p2):
    result = Polynomial()
    a = p1.head
    b = p2.head

    while a and b:
        if a.power == b.power:
            result.insert_term(a.coeff + b.coeff, a.power)
            a = a.next
            b = b.next
        elif a.power > b.power:
            result.insert_term(a.coeff, a.power)
            a = a.next
        else:
            result.insert_term(b.coeff, b.power)
            b = b.next

    while a:
        result.insert_term(a.coeff, a.power)
        a = a.next

    while b:
        result.insert_term(b.coeff, b.power)
        b = b.next

    return result

def get_polynomial_input(n):
    poly = Polynomial()
    print(f"Enter {n} terms as 'coefficient power':")
    for _ in range(n):
        coeff, power = map(int, input().split())
        poly.insert_term(coeff, power)
    return poly


n1 = int(input("Enter number of terms in first polynomial: "))
poly1 = get_polynomial_input(n1)


n2 = int(input("Enter number of terms in second polynomial: "))
poly2 = get_polynomial_input(n2)


print("\nPolynomial 1:")
poly1.display()

print("Polynomial 2:")
poly2.display()

result = add_polynomials(poly1, poly2)
print("Resultant Polynomial:")
result.display()
