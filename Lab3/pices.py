from math import ceil

def can_eat_in_time(piles, hour, speed):
    required_time = 0
    for pile in piles:
        required_time += ceil(pile/speed)
    return required_time <= hour

def count_min_eating_time(piles, hour):
    biggest_pile = max(piles)
    num_of_piles = len (piles)
    if num_of_piles == hour:
        return max(piles)
    if num_of_piles > hour:
        raise ValueError("Jackie will not be able to eat all the bananas in time")
    if sum(piles) <= hour:
        return 1
    average_eating_time = sum(piles) // hour
    while average_eating_time < biggest_pile: 
        speed = (average_eating_time + biggest_pile) // 2
        if can_eat_in_time(piles, hour, speed):
            biggest_pile = speed
        else:
            average_eating_time = speed + 1
    return average_eating_time

if __name__ == '__main__':
    print(count_min_eating_time([30,11,23,4,20],6))
    print(count_min_eating_time([3,6,7,11],8))
    print(count_min_eating_time([30,11,23,4,20],5))
    print(count_min_eating_time([5, 2, 1, 3, 2], 15))
    print(count_min_eating_time([90, 11, 23, 4, 20], 5))
    