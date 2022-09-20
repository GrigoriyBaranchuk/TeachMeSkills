
def geometry_progression(first_num: int, base: int) -> int:
    while True:
        first_num *= base
        yield first_num


g = geometry_progression(2, 2)

for i in range(1, 11):
    print(f"iteration {i}: value g = {next(g)}")
