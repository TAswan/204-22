from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# These two lines make sure a faster SAT solver is used.
from nnf import config
config.sat_backend = "kissat"

from constructors import *

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BasicPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"


# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
@proposition(E)
class FancyPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

# Call your variables whatever you want
a = BasicPropositions("a")
b = BasicPropositions("b")   
c = BasicPropositions("c")
d = BasicPropositions("d")
e = BasicPropositions("e")
# At least one of these will be true
x = FancyPropositions("x")
y = FancyPropositions("y")
z = FancyPropositions("z")


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    # Add custom constraints by creating formulas with the variables you created. 
    E.add_constraint((a | b) & ~x)
    # Implication
    E.add_constraint(y >> z)
    # Negate a formula
    E.add_constraint(~(x & y))
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    constraint.add_exactly_one(E, a, b, c)

    return E

# def tetromino_theory():

time_20 = Time(20)
row_cleared = Row_Cleared()

def build_theory():
    # ----------TETROMINO CONSTRAINTS----------
    # --------------------------------------------------
    # Alpha: a tetromino cannot exceed the boundaries
    # --------------------------------------------------

    # line
    for y in range(20):
        constraint.add_exactly_one(E, [Anchor(x, y) & Tetromino(0) & Rotation(0) for x in range(10)] +
                                      [Anchor(x, y) & Tetromino(0) & Rotation(1) for x in range(1, 7)] +
                                      [Anchor(x, y) & Tetromino(0) & Rotation(2) for x in range(10)] +
                                      [Anchor(x, y) & Tetromino(0) & Rotation(3) for x in range(1, 7)])

    # square
    for y in range(20):
        constraint.add_exactly_one(E, [Anchor(x, y) & Tetromino(1) & Rotation(0) for x in range(9)] +
                                      [Anchor(x, y) & Tetromino(1) & Rotation(1) for x in range(9)] +
                                      [Anchor(x, y) & Tetromino(1) & Rotation(2) for x in range(9)] +
                                      [Anchor(x, y) & Tetromino(1) & Rotation(3) for x in range(9)])
    
    # J
    for y in range(20):
        constraint.add_exactly_one(E, [Anchor(x, y) & Tetromino(2) & Rotation(0) for x in range(1, 9)] +
                                      [Anchor(x, y) & Tetromino(2) & Rotation(1) for x in range(1, 10)] +
                                      [Anchor(x, y) & Tetromino(2) & Rotation(2) for x in range(1, 9)] +
                                      [Anchor(x, y) & Tetromino(2) & Rotation(3) for x in range(0, 9)])
    
    # L
    for y in range(20):
        constraint.add_exactly_one(E, [Anchor(x, y) & Tetromino(2) & Rotation(0) for x in range(1, 9)] +
                                      [Anchor(x, y) & Tetromino(2) & Rotation(1) for x in range(1, 10)] +
                                      [Anchor(x, y) & Tetromino(2) & Rotation(2) for x in range(1, 9)] +
                                      [Anchor(x, y) & Tetromino(2) & Rotation(3) for x in range(0, 9)])
    
    # S
    for y in range(20):
        constraint.add_exactly_one(E, [Anchor(x, y) & Tetromino(2) & Rotation(0) for x in range(1, 9)] +
                                      [Anchor(x, y) & Tetromino(2) & Rotation(1) for x in range(1, 10)] +
                                      [Anchor(x, y) & Tetromino(2) & Rotation(2) for x in range(1, 9)] +
                                      [Anchor(x, y) & Tetromino(2) & Rotation(3) for x in range(1, 10)])
    
    # T
    for y in range(20):
        constraint.add_exactly_one(E, [Anchor(x, y) & Tetromino(5) & Rotation(0) for x in range(1, 9)] +
                                      [Anchor(x, y) & Tetromino(5) & Rotation(1) for x in range(1, 10)] +
                                      [Anchor(x, y) & Tetromino(5) & Rotation(2) for x in range(1, 9)] +
                                      [Anchor(x, y) & Tetromino(5) & Rotation(3) for x in range(0, 9)])
    
    # Z
    for y in range(20):
        constraint.add_exactly_one(E, [Anchor(x, y) & Tetromino(2) & Rotation(0) for x in range(1, 9)] +
                                      [Anchor(x, y) & Tetromino(2) & Rotation(1) for x in range(1, 10)] +
                                      [Anchor(x, y) & Tetromino(2) & Rotation(2) for x in range(1, 9)] +
                                      [Anchor(x, y) & Tetromino(2) & Rotation(3) for x in range(1, 10)])
    
    # --------------------------------------------------
    # Beta: a tetromino cannot overlap with occupied cells
    # --------------------------------------------------


    # --------------------------------------------------
    # Gamma: a tetromino can rotate
    # --------------------------------------------------



    # --------------------------------------------------
    # Delta: a tetromino can shift
    # --------------------------------------------------



    # ----------TIME CONSTRAINTS----------
    # --------------------------------------------------
    # Time cannot go above 20 ticks
    # --------------------------------------------------



    # --------------------------------------------------
    # A successful Gamma or Delta will increase time by 1
    # --------------------------------------------------



    # --------------------------------------------------
    # If a tetromino doesn’t make a Gamma or Delta move then the tetromino will drop by 1 y coordinate, 
    # and time will move 1 step as long as no piece is below it, otherwise it will stay in place and the 
    # last row clearance check will occur.
    # --------------------------------------------------

    E.add_constraint(time_20 >> ~row_cleared)

    E.add_constraint()

if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
