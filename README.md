ENGR 3770U -- Design and Analysis of Algorithms -- Final Project
=================================================================

Our implementation of algorithmic solutions to the convex hull and shortest-path problems
assigned for the algorithms project.


Summary of Algorithms Used
---------------------------

For the convex hull problem we initially tried to create our own algorithm which utilized 
the Point in Poly (PNPOLY) algorithm, but continually ran into corner case issues with our
implementation. Instead, we resorted to using the Monotone Chain algorithm which is easy to
grasph, was well documented, and a fairly optimal solution.

For the shortest path problem we used Dijkstra's Algorithm as it is one of the most optimal
algorithms for solving the shortest path problem and involves the use of dynamic programming,
such that each selection of a node (local optima) leads to a globally optimal solution. Unfortunately,
our shortest path solution does not solve the [Canadian Traveller Problem](http://en.wikipedia.org/wiki/Canadian_traveller_problem),
but we believe that snow shoes may be the optimal solution to that probolem.


Copyright (Really Copyleft)
---------------------------

All of the source code in this repository, where the copyright notice is indicated in the source
code, is licensed under the [GNU General Public License, Version 3](http://www.gnu.org/licenses/gpl.html)
