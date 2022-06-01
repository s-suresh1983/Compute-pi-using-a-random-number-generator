# Compute-pi-using-a-random-number-generator
Compute π using a random number generator
The number π (Pi) can be calculated using random numbers. Suppose you have a circle with radius 1 which is inscribed in a square with a side length of 2 (see figure below). Then the square has an area of 4 (2 * 2) and the circle has an area of π (r = 1, thus π * r² = π).
If thousands of points are randomly created within the square, then some points are inside the square and inside the circle, others are inside the square and not inside the circle. The situation can be simplified if you just consider the upper right quadrant of the above figure. This square has a side length of 1. Each point within the square can be described by the coordinates x and y where (0 < x, y < 1). If x² + y² < 1, then a point specified by (x, y) lies within the circle.
As the relation between the sizes of circle and square is π/4, the relation between the points in the circle and the points in the square must be π/4 as well. Using this formula, one can now use a random number generator to calculate π.

Your Task

Using the library random create 10,000 random points inside the square. That means generate 10,000 random pairs of values for x and y. The random value must be between 0 and 1 in order for a point to be inside the square. For each point check if x² + y² is < 1. If this is the case, then the point is within the circle. Count the total number of points and the points which are in the circle. Use these numbers to calculate π. Finally compare your calculated value of π with the value of π found in the math library. Do this by printing the calculated value of π, the value from the math library as well as the difference.
