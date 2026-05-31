
# leetcode nickname asucha_473109

# 2026-05-31 leetcode daily problem --- medium --- 2126. Destroying Asteroids --- solved

"""
2126. Destroying Asteroids

You are given an integer mass, which represents the original mass of a planet. You are further given an integer array asteroids, where asteroids[i] is the mass of the ith asteroid.

You can arrange for the planet to collide with the asteroids in any arbitrary order. If the mass of the planet is greater than or equal to the mass of the asteroid, the asteroid is destroyed and the planet gains the mass of the asteroid. Otherwise, the planet is destroyed.

Return true if all asteroids can be destroyed. Otherwise, return false.


Constraints:

1 <= mass <= 10^5
1 <= asteroids.length <= 10^5
1 <= asteroids[i] <= 10^5


Example 1:

Input: mass = 10, asteroids = [3,9,19,5,21]
Output: true
Explanation: One way to order the asteroids is [9,19,5,3,21]:
- The planet collides with the asteroid with a mass of 9. New planet mass: 10 + 9 = 19
- The planet collides with the asteroid with a mass of 19. New planet mass: 19 + 19 = 38
- The planet collides with the asteroid with a mass of 5. New planet mass: 38 + 5 = 43
- The planet collides with the asteroid with a mass of 3. New planet mass: 43 + 3 = 46
- The planet collides with the asteroid with a mass of 21. New planet mass: 46 + 21 = 67
All asteroids are destroyed.
Example 2:

Input: mass = 5, asteroids = [4,9,23,4]
Output: false
Explanation: 
The planet cannot ever gain enough mass to destroy the asteroid with a mass of 23.
After the planet destroys the other asteroids, it will have a mass of 5 + 4 + 9 + 4 = 22.
This is less than 23, so a collision would not destroy the last asteroid.
"""

from typing import List

# Solution Attempt 1 - Accepted, passed all 75 test cases, beats 54% runtime-wise and 54% memory-wise

# At first the task seems easy since the contraints does not permit 
# the usage of sorting algorithms, but such approach can be inefficient,
# since it will potentially need to put the entire set of 10^5 asteroids
# and this seems inefficient since it will need to go through all of the
# masses and compare them, but lets try at first  

# Okay it did work afterall...

# class Solution:
#     def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
#         planetmass = mass
#         order = sorted(asteroids)

#         for asteroid in order:
#             if planetmass >= asteroid:
#                 planetmass += asteroid
#             else:
#                 return False
#         return True

# Solution Attempt 2 - Accepted, now beats 74% runtime-wise and 75% memory-wise

# Let's put some optimisation tweaks in place 

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        asteroids.sort()

        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass += asteroid
                
        return True



# primitive tests
o = Solution()
print( o.asteroidsDestroyed(10, [3,9,19,5,21]) )
print( o.asteroidsDestroyed(5, [4,9,23,4]) )
