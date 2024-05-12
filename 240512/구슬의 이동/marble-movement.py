n, m, t, k = map(int, input().split())

grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]

turn_dict = {
    "U": "D",
    "R": "L",
    "D": "U",
    "L": "R",
}

d_coord_dict = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1)
}


def in_range(row, col):
    return 0 <= row < n and 0 <= col < n 

def gen_coord(row, col, d):
    d_row, d_col = d_coord_dict[d]
    n_row, n_col = row + d_row, col + d_col
    return (n_row, n_col)

class Ball:
    def __init__(self, row, col, d, p, i):
        self.row = row
        self.col = col
        self.d = d
        self.p = p
        self.i = i
        self.status = True
    
    def move(self, _grid):
        if not self.status:
            return

        for _ in range(self.p):
            n_row, n_col = gen_coord(self.row, self.col, self.d)
            if not in_range(n_row, n_col):
                self.d = turn_dict[self.d]
                n_row, n_col = gen_coord(self.row, self.col, self.d)
        
            self.row, self.col = n_row, n_col

        n_target = _grid[self.row][self.col]

        if len(n_target) < k:
            n_target.append(self)
            
        else:   
            last = n_target[len(n_target) - 1]
            if self.p > last.p or self.p == last.p and self.i > last.i:
                n_target.pop().status = False
                n_target.append(self)
            else:
                self.status = False

        n_target.sort(lambda x: (x.p, x.i), reverse=True)

ball_list = []

for i in range(m):
    _row, _col, d, _p = input().split()
    
    row = int(_row) - 1
    col = int(_col) - 1
    p = int(_p)

    ball = Ball(row, col, d, p, i)

    grid[row][col].append(ball)
    ball_list.append(ball)

for _ in range(t):
    _grid = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]

    for ball in ball_list:
        ball.move(_grid)

    grid = _grid

cnt = 0

for ball in ball_list:
    if ball.status:
        cnt += 1
    
print(cnt)