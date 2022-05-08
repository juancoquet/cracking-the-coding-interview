# 7.2 call centre
class Employee():

    def __init__(self):
        self.available = True
        self.call = None


class Respondent(Employee):

    def __init__(self):
        super().__init__()


class Manager(Employee):

    def __init__(self):
        super().__init__()


class Director(Employee):

    def __init__(self):
        super().__init__()


class Call:

    def __init__(self):
        self.handler = None


class NoHandler(Exception):
    pass


class NoEscalation(Exception):
    pass


class CallCentre:

    def __init__(self):
        self.respondents = []
        self.managers = []
        self.directors = []
        self.available_repondents = []
        self.available_managers = []
        self.available_directors = []
        self.active_calls = []

    def add_respondent(self):
        resp = Respondent()
        self.respondents.append(resp)
        self.available_respondents.append(resp)

    def add_manager(self):
        manager = Manager()
        self.managers.append(manager)
        self.available_managers.append(manager)

    def add_director(self):
        director = Director()
        self.directors.append(director)
        self.available_directors.append(director)

    def dispatch_call(self, call):
        if self.available_respondents:
            resp = self.available_respondents.pop()
            call.handler = resp
            resp.available = False
            resp.call = call
            self.active_calls.append(call)
        else:
            raise NoHandler("There is no respondent available")

    def escalate(self, call):
        old_handler = call.handler
        if old_handler.type() == Respondent:
            if self.available_managers:
                handler = self.available_managers.pop()
                call.handler = handler
                handler.available = False
                handler.call = call
                self.available_respondents.append(old_handler)
            else:
                raise NoHandler("There is no manager availbale")
        elif old_handler.type() == Manager:
            if self.available_directors:
                handler = self.available_directors.pop()
                call.handler = handler
                handler.available = False
                handler.call = call
                self.available_managers.append(old_handler)
            else:
                raise NoHandler("There is no director available")
        else:
            raise NoEscalation("The call cannot be escalated above the director level")
        old_handler.available = True
        old_handler.call = None

    def end_call(self, call):
        self.active_calls.remove(call)
        if call.handler.type() == Respondent:
            self.available_respondents.append(call.handler)
        elif call.handler.type() == Manager:
            self.available_managers.append(call.handler)
        else:
            self.available_directors.append(call.handler)
        call.handler.available = True
        call.handler.call = None
        call.handler = None


# 7.6 'jigsaw'
class Piece:

    def __init__(self, id):
        self.id = id
        self.belongs_with = {
            'top': None,
            'right': None,
            'bottom': None,
            'left': None
        }
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

    def is_solved(self):
        top = self.top == self.belongs_with['top']
        right = self.right == self.belongs_with['right']
        bottom = self.bottom == self.belongs_with['bottom']
        left = self.left == self.belongs_with['left']
        return all([top, right, bottom, left])

    def is_top(self):
        return self.belongs_with['top'] is None

    def is_right(self):
        return self.belongs_with['right'] is None

    def is_bottom(self):
        return self.belongs_with['bottom'] is None

    def is_left(self):
        return self.belongs_with['left'] is None

    def is_corner(self):
        top = self.is_top()
        right = self.is_right()
        bottom = self.is_bottom()
        left = self.is_left()
        return ((top is None and left is None) or
            (top is None and right is None) or
            (bottom is None and left is None) or
            (bottom is None and right is None))


class Jigsaw:

    def __init__(self, size):
        self.size = size
        self.pieces = self._generate()
        self.placed = {}
        self.solved = {}


    def _generate(self):
        pieces = {}
        for i in range(self.size**2):
            pieces[i] = Piece(i)
        
        for i, p in pieces.items():
            if not self._belongs_top(p):
                p.belongs_with['top'] = self.pieces[i-self.size]
            if not self._belongs_right(p):
                p.belongs_with['right'] = self.pieces[i+1]
            if not self._belongs_bottom(p):
                p.belongs_with['bottom'] = self.pieces[i+self.size]
            if not self._belongs_left(p):
                p.belongs_with['left'] = self.pieces[i-1]	
            
        return pieces

    def _belongs_top(self, piece):
        return piece.id < self.size

    def _belongs_right(self, piece):
        return piece.id % self.size == self.size - 1

    def _belongs_bottom(self, piece):
        return piece.id >= self.size * (self.size - 1)

    def _belongs_left(self, piece):
        return piece.id % self.size == 0

    def connect(self, p1, p2):
        for edge, piece in p1.belongs_with.items():
            if piece == p2:
                p1[edge] = p2
                break
        for edge, piece in p2.belongs_with.items():
            if piece == p1:
                p2[edge] = p1
                break

    def solve(self):
        for i, piece in self.pieces.items():
            if piece.is_corner():
                self.placed[i] = piece
                del self.pieces[i]

            for target in piece.belongs_with.values():
                if target.id in self.placed:
                    self.connect(piece, target)
                if not piece.id in self.placed:
                    self.placed[piece.id] = piece
                    del self.pieces[piece.id]
                if target.is_solved():
                    self.sovled[target.id] = target
                    del self.placed[target.id]
                if piece.is_solved():
                    self.solved[piece.id] = piece
                    del self.placed[piece.id]


# 7.8 othello
WHITE = True
BLACK = False

class Piece:

    def __init__(self, colour=WHITE):
        self.colour = colour
        self.square = None
        
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

    @property
    def neighbours(self):
        neighbours = [self.top, self.right, self.bottom, self.left]
        return [n for n in neighbours if n is not None]

    def _flip(self):
        self.colour = not self.colour

    def update(self):
        vertical, horizontal = False, False
        if self.top is not None and self.bottom is not None:
            if (self.top.colour != self.colour 
            and self.bottom.colour != self.colour):
                vertical = True
            if (self.left.colour != self.colour
            and self.right.colour != self.colour):
                horizontal = False
        
        if vertical or horizontal:
            self._flip()
        
        return vertical or horizontal


class Board:

    def __init__(self, size=8):
        self.size = size
        self.occupied = []
        self.unoccupied = []
        self.squares = self._generate_board()
        self.turn = WHITE
        self._place_start_pieces()

    def _generate_board(self):
        squares = {}
        for r in range(self.size):
            for c in range(self.size):
                sq = (r, c)
                squares[sq] = None
                self.unoccupied.append(sq)
        
        return squares

    def _change_turn(self):
        self.turn = not self.turn

    def _place_start_pieces(self):
        mid = self.size // 2
        self.place((mid, mid), skip_validation=True)
        self.place((mid, mid-1), skip_validation=True)
        self.place((mid-1, mid-1), skip_validation=True)
        self.place((mid-1, mid), skip_validation=True)

    def place(self, sq, skip_validation=False):
        if not skip_validation:
            if self.squares[sq] is not None:
                raise InvalidMove('Square is not empty')
                
            if not self._move_valid(sq):
                raise InvalidMove('Move is not valid')
        
        piece = Piece(colour=self.turn)

        self.squares[sq] = piece
        piece.square = sq
        self.unoccupied.remove(sq)
        self.occupied.append(sq)
        self._update_connections(piece)
        self._update_surroundings(piece)
        self._change_turn()

    def _move_valid(self, sq):
        r, c = sq

        top = self.squares.get((r-1, c))
        if top is not None:
            if top.colour != self.turn:
                while top is not None:
                    if top.colour == self.turn:
                        return True
                    top = top.top

        right = self.squares.get((r, c+1))
        if right is not None:
            if right.colour != self.turn:
                while right is not None:
                    if right.colour == self.turn:
                        return True
                    right = right.right

        bottom = self.squares.get((r+1, c))
        if bottom is not None:
            if bottom.colour != self.turn:
                while bottom is not None:
                    if bottom.colour == self.turn:
                        return True
                    bottom = bottom.bottom

        left = self.squares.get((r, c-1))
        if left is not None:
            if left.colour != self.turn:
                while left is not None:
                    if left.colour == self.turn:
                        return True
                    left = left.left

        return False

    def _update_surroundings(self, piece):
        to_visit = [piece]
        while len(to_visit) > 0:
            curr = to_visit.pop(0)
            for neighbour in curr.neighbours:
                updated = neighbour.update()
                if updated:
                    to_visit.append(neighbour)

    def _update_connections(self, piece):
        r, c = piece.square
        piece.top = self.squares.get((r-1, c))
        piece.right = self.squares.get((r, c+1))
        piece.bottom = self.squares.get((r+1, c))
        piece.left = self.squares.get((r, c-1))

    @property
    def end_game(self):
        for sq in self.unoccupied:
            if self._move_valid(sq):
                return False
        return True

    def get_winner(self):
        white, black = 0, 0
        for sq in self.occupied:
            if self.squares[sq].colour == WHITE:
                white += 1
            elif self.squares[sq].colour == BLACK:
                black += 1
        if white > black:
            return 'white'
        elif black > white:
            return 'black'
        else:
            return None

class InvalidMove(Exception):
    pass



# board = Board()

# game loop
# while not board.end_game:
#     r = input('row?')
#     c = input('col?')
#     sq = (int(r), int(c))
#     try:
#         board.place(sq)
#     except InvalidMove as e:
#         print(e)
#         continue
# winner = board.get_winner()


# 7.9 circular array
class CircularArray:

    def __init__(self, arr):
        self.arr = arr
        
    def __iter__(self):
        for x in self.arr:
            yield x

    def __repr__(self):
        return self.arr

    def __str__(self):
        s = "["
        for x in self:
            s += str(x) + ', '
        s = s[:-2] + ']'
        return s

    def rotate_left(self, n=1):
        if len(self.arr) <= 1:
            return
        for _ in range(n):
            first = self.arr[0]
            self.arr = self.arr[1:] + [first]

    def rotate_right(self, n=1):
        if len(self.arr) <= 1:
            return
        for _ in range(n):
            last = self.arr[-1]
            self.arr = [last] + self.arr[:-1]