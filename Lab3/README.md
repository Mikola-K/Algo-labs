# Algo_lab 3

## Defining the problem 

Jackie Gorilla from the Munich Zoo loves to eat bananas. The zoo has N baskets (piles) with bananas, in the i-th basket there is a certain number of bananas H. The baskets are guarded, but the guard patrols the zoo for H hours, during which Jackie can enjoy his favorite dish.
Jackie can eat bananas in an hour. Every hour she picks a basket of bananas and eats K bananas from there. If the basket has less than K bananas, it will eat all the bananas from it and will no longer eat bananas during that hour.
Jackie likes to eat slowly, but still wants to finish eating all the bananas before the guards return.
Determine the minimum integer K so that Jackie can eat all the bananas in the warehouse for H hours until the guards return.

# Constraints :
  - 1 <= piles.length <= 10^4
  - piles.length <= H <= 10^9
  - 1 <= piles[i] <= 10^9

# Examples:
  Example 1

    Input: piles = [3,6,7,11], H = 8 <br>
    Output: 4

  Example 2 

    Input: piles = [30,11,23,4,20], H = 5 <br>
    Output: 30

  Example 3

    Input: piles = [30,11,23,4,20], H = 6 <br>
    Output: 23

  # Complexity analyses 
  ## Complexity analyses 

  - Space complexity O(1)
  - Time complexity O(nlog(m))

## How to run
  + `cd` into folder where you want to store this repository
  + Clone this repository with command `https://github.com/Mikola-K/Algo-labs.git`
  + Choose branch lab3 with command `git checkout lab3`
  + Go into folder with files with command `cd Algo-labs`
  + run command `python3 pices.py` on Mac/Linux *or* `py pices.py` on Windows