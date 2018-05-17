#Laura Davis 20 July 2017

#source code from MITOCW "Electrical Engineering and Computer Science"
#Lecture on recursion in Python

#demonstrates how recursive exponentiation is computed within the machine
def recursiveExponentiations(b, n):

        if n==0:
                return 1
        else:
                return b*recursiveExponentiations(b, n-1)
		
recursiveExponentiations(2, 6)
print recursiveExponentiations(2, 6)
	#calls exponent(2, 5)
		#calls exponent(2, 4)
			#calls exponent(2, 3)
				#calls exponent(2, 2)
					#calls exponent(2, 1)
						#calls exponent(2, 0)
						#returns 1
					#returns 2
				#returns 4
			#returns 8
		#returns 16
	#returns 32
#returns 64

#demonstrates the logic of computation with towers of Hanoi 
def Hanoi(n, A, B, C):
	if n == 1:
		print "move from" + A + " to " + B
	else:
		Hanoi(n-1, A, C, B)
		Hanoi(1, A, B, C)
		Hanoi(n-1, C, B, A)
#This recursive solution is expressive, simple, and elegant

#demonstrates OOP with tree sorting
class Node:
	def __init__(self, parent, action, answer):
		self.parent = parent
		self.action = action
		self.answer = answer
	def path(self):
		if self.parent == None:
			return [(self.action, self.answer)]
		else:
			return self.parent.path() + [(self.action, self.answer)]
		
#systematically create and search through all possible Nodes
def findSequence(initial, goal):
	increment = initial+1
	square = goal-1
	
	q = [Node(None, None, 1)]
	while q:
		parent = q.pop(0)
		for (a, r) in [('increment', increment), ('square', square)]:
			newNode = Node(parent, a, r(parent.answer))
			if newNode.answer == goal:
				return newNode.path()
			else: 
				q.append(newNode)
	return None
answer = findSequence(1, 100)
print 'answer = ', answer
