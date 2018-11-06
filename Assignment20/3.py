def check_bricks(num_small, num_big, goal):
    total_length = num_small * 1
    total_length += num_big * 5
    if total_length >= goal:
        return True
    else:
        return False