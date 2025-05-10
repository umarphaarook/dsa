class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class List:
	def __init__(self):
		self.head = None

	def insert_head(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_tail(self, data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			return
		curr_node = self.head
		while curr_node.next:
			curr_node = curr_node.next
		curr_node.next = new_node

	def insert_at(self, data, index):
		new_node = Node(data)
		if self.head == None or index <= 0:
			self.insert_head(data)
			return
		curr_node = self.head
		curr_node_index = 0
		while curr_node.next:
			next_node_index = curr_node_index + 1
			if next_node_index == index:
				next_node = curr_node.next
				curr_node.next = new_node
				new_node.next = next_node
				break
			else:
				curr_node = curr_node.next
				if not curr_node.next:
					curr_node.next = new_node
					break
			curr_node_index = next_node_index

	def insert(self, data):
		self.insert_tail(data)

	def find_left_neighbor(self, data):
		curr_node = self.head
		while curr_node.next:
			if curr_node.next.data == data: return curr_node
			else: curr_node = curr_node.next

	def find(self, data):
		curr_node = self.head
		if not curr_node: return None
		# when the first node is the target
		elif curr_node.data == data: return	curr_node.data
		else:
			neighbor = self.find_left_neighbor(data)
			if neighbor: return neighbor.next.data
			else: return None
		
	def delete(self, data):
		curr_node = self.head
		if curr_node:
			# when the first node is the target
			if curr_node.data == data: self.head = curr_node.next
			else:
				neighbor = self.find_left_neighbor(data)
				if neighbor:
					gabbage = neighbor.next
					new_next = gabbage.next
					neighbor.next = new_next
	
	def reverse(self):
		prev_node = None
		curr_node = self.head
		while curr_node:
			next_node = curr_node.next
			curr_node.next = prev_node
			prev_node = curr_node
			curr_node = next_node
		self.head = prev_node

	def print(self):
		curr_node = self.head
		print('list: ', end='')
		while curr_node:
			print(curr_node.data, end=' -> ')
			curr_node = curr_node.next
		print(end='None\n')

if __name__ == '__main__':
	ll = List()
	ll.insert_head(1)
	ll.insert_head(2)
	ll.insert_head(3)
	ll.insert(4)
	ll.insert(5)
	ll.insert(6)
	ll.insert_at(7, 0)
	ll.insert_at(8, 70)
	ll.print()
	ll.delete(7)
	ll.delete(4)
	ll.delete(8)
	ll.print()
	print(f'Find {2}: {ll.find(2)}')
	print(f'Find {9}: {ll.find(9)}')
	ll.reverse()
	ll.print()
