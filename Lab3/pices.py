from math import ceil

def can_eat_in_time(piles, hours, eating_speed):
    required_time = 0
    for pile in piles:
        required_time += ceil(pile/eating_speed)
    return required_time <= hours

def find_min_eating_speed(piles, hours, possible_eating_speeds):
    if len(possible_eating_speeds) == 1:
        return possible_eating_speeds[0]
    
    current_eating_speed = possible_eating_speeds [len(possible_eating_speeds) // 2]
    if can_eat_in_time (piles, hours, current_eating_speed):
        return find_min_eating_speed(piles,hours, possible_eating_speeds[len(possible_eating_speeds) // 2:])
    else:
        return find_min_eating_speed(piles,hours, possible_eating_speeds[:len(possible_eating_speeds) // 2])

def count_min_eating_time(piles, hours):
    if len(piles) == hours:
        return max(piles)
    if len(piles) > hours:
        raise ValueError("Jackie will not be able to eat all the bananas in time")
    if sum(piles) <= hours:
        return 1
    
    possible_eating_speeds = [i for i in range(max(piles), 1, -1)]
    return find_min_eating_speed(piles, hours, possible_eating_speeds)

if __name__ == '__main__':
    print(count_min_eating_time([30,11,23,4,20],6))
    print(count_min_eating_time([3,6,7,11],8))
    print(count_min_eating_time([30,11,23,4,20],5))
    print(count_min_eating_time([5, 2, 1, 3, 2], 15))
    print(count_min_eating_time([90, 11, 23, 4, 20], 5))
    