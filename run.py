from bauhaus import Encoding, proposition, constraint, Or, And
from bauhaus.utils import count_solutions, likelihood

# These two lines make sure a faster SAT solver is used.
from nnf import config

config.sat_backend = "kissat"

from constructors import *
from tetrominos import TETROMINOS

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

row_cleared = Row_Cleared()

# tetrominos = {key: [] for key in TETROMINOS.keys()}
# for x in range(10):
#     for y in range(20):
#         for t in range(19):
#             for tetromino in TETROMINOS.keys():
#                 for rotation in range(4):
#                     tetrominos[tetromino].append(Tetromino((x, y), tetromino, rotation, t))

line = Tetromino((0, 4), "line", 0, 0)
square = Tetromino((0, 4), "square", 0, 0)
j = Tetromino((0, 4), "J", 0, 0)
l = Tetromino((0, 4), "L", 0, 0)
s = Tetromino((0, 4), "S", 0, 0)
t = Tetromino((0, 4), "T", 0, 0)
z = Tetromino((0, 4), "Z", 0, 0)

def find_row_candidates(board):
    """
       takes in a board and adds constraints based on what Tetrominos can possibly clear a row

       Args:
           board(Board) : the board to check

       Returns:
           None: Mutates the encoding.
       """
    # holes that can be filled by tetrominos
    hole_constraints = {
        1: [line, j, l, s, t, z],
        2: [square, j, l, s, t, z],
        3: [t, j, l],
        4: [line]
    }

    holes = set()
    rows = []
    for row in board:
        rows.append(row)
        gap = True
        # how many open spaces in a row
        holes_in_row = sum(1 for value in row if not value)
        # if theres gaps in the row, we can't clear it, so skip
        if sum(True in row) > holes_in_row or holes_in_row > 4:
            gap = True
            rows.remove(row)
        if not gap:
            holes.append(holes_in_row)

    # row is already cleared
    if 0 in holes:
        E.add_constraint(row_cleared)
        return
    # all are eliminated at first
    eliminated = set(line, square, j, l, s, t, z)

    for hole_count in holes:
        if hole_count in hole_constraints:
            # get the allowed tetrominos for this hole count
            possible_tetrominos = hole_constraints[hole_count]
            for tetromino in possible_tetrominos:
                # remove the tetromino from the eliminated set
                eliminated.remove(tetromino)
    # if the tetromino is eliminated, it can't clear any rows
    for tetromino in eliminated:
        E.add_constraint(tetromino >> ~row_cleared)
    return rows


def build_theory():
    # ----------BOARD CONSTRAINTS----------

    # If any row as all cells filled, then the row is cleared
    rows = []
    for y in range(20):
        cells = []
        for x in range(10):
            cells.append(Cell(x, y))
        rows.append(And(cells))
    E.add_constraint(Or(rows) >> row_cleared)

    # ----------TETROMINO CONSTRAINTS----------

    # A tetromino can only be of one type
    # TODO possibly remove
    constraint.add_exactly_one(E, line, square, j, l, s, t, z)  # Can be moved to decorator

    # A tetromino cannot exceed the boundaries
    # Logic: For all time, every row is allowed one (legal) x value for a Tetromino's anchor, i.e., a Tetromino cannot occupy more than one x value in a given row
    # TODO verify add exactly one
    for t in range(20):
        for y in range(20):
            # line
            constraint.add_exactly_one(E, [Tetromino((x, y), "line", 0, t) for x in range(10)] +
                                          [Tetromino((x, y), "line", 1, t) for x in range(1, 7)] +
                                          [Tetromino((x, y), "line", 2, t) for x in range(10)] +
                                          [Tetromino((x, y), "line", 3, t) for x in range(1, 7)])

            # square
            constraint.add_exactly_one(E, [Tetromino((x, y), "square", 0, t) for x in range(9)] +
                                          [Tetromino((x, y), "square", 1, t) for x in range(9)] +
                                          [Tetromino((x, y), "square", 2, t) for x in range(9)] +
                                          [Tetromino((x, y), "square", 3, t) for x in range(9)])

            # J
            constraint.add_exactly_one(E, [Tetromino((x, y), "J", 0, t) for x in range(1, 9)] +
                                          [Tetromino((x, y), "J", 1, t) for x in range(1, 10)] +
                                          [Tetromino((x, y), "J", 2, t) for x in range(1, 9)] +
                                          [Tetromino((x, y), "J", 3, t) for x in range(0, 9)])

            # L
            constraint.add_exactly_one(E, [Tetromino((x, y), "L", 0, t) for x in range(1, 9)] +
                                          [Tetromino((x, y), "L", 1, t) for x in range(1, 10)] +
                                          [Tetromino((x, y), "L", 2, t) for x in range(1, 9)] +
                                          [Tetromino((x, y), "L", 3, t) for x in range(0, 9)])

            # S
            constraint.add_exactly_one(E, [Tetromino((x, y), "S", 0, t) for x in range(1, 9)] +
                                          [Tetromino((x, y), "S", 1, t) for x in range(1, 10)] +
                                          [Tetromino((x, y), "S", 2, t) for x in range(1, 9)] +
                                          [Tetromino((x, y), "S", 3, t) for x in range(1, 10)])

            # T
            constraint.add_exactly_one(E, [Tetromino((x, y), "T", 0, t) for x in range(1, 9)] +
                                          [Tetromino((x, y), "T", 1, t) for x in range(1, 10)] +
                                          [Tetromino((x, y), "T", 2, t) for x in range(1, 9)] +
                                          [Tetromino((x, y), "T", 3, t) for x in range(0, 9)])

            # Z
            constraint.add_exactly_one(E, [Tetromino((x, y), "Z", 0, t) for x in range(1, 9)] +
                                          [Tetromino((x, y), "Z", 1, t) for x in range(1, 10)] +
                                          [Tetromino((x, y), "Z", 2, t) for x in range(1, 9)] +
                                          [Tetromino((x, y), "Z", 3, t) for x in range(1, 10)])

    # A tetromino cannot overlap with occupied cells
    for x in range(10):
        for y in range(20):
            for t in range(20):
                E.add_constraint(~(Block(x, y, t) & Cell(x, y)))

    # A Tetromino will drop if there is no cell below it up to 19 ticks
    for x in range(10):
        for y in range(20):
            for t in range(19):
                for tetromino in TETROMINOS.keys():
                    for rotation in range(4):
                        cells = []
                        for coord in range(4):
                            cells.append(~Cell(x + TETROMINOS[tetromino][rotation][coord][0], y + 1))
                        E.add_constraint((Tetromino((x, y), tetromino, rotation, t) & And(cells)) >> Tetromino((x, y + 1), tetromino, rotation, t + 1))

    # A Tetromino will turn into cells if there exists one cell below
    for x in range(10):
        for y in range(20):
            for t in range(19):
                for tetromino in TETROMINOS.keys():
                    for rotation in range(4):
                        tetromino_to_cells = []
                        cells_below = []
                        for coord in range(4):
                            cells_below.append(Cell(x + TETROMINOS[tetromino][rotation][coord][0], y + 1))
                            tetromino_to_cells.append(Cell(x + TETROMINOS[tetromino][rotation][coord][0], y + TETROMINOS[tetromino][rotation][coord][1]))
                        E.add_constraint((Tetromino((x, y), tetromino, rotation, t) & Or(cells)) >> And(cells))

    # If time reaches 20 ticks, then it is not possible for a row to be cleared
    for x in range(10):
        for y in range(20):
            for tetromino in TETROMINOS.keys():
                for rotation in range(4):
                    E.add_constraint(Tetromino((x, y), tetromino, rotation, 20) >> ~row_cleared)


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
    for v, vn in zip([a, b, c, x, y, z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
