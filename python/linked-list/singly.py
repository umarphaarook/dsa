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

	def insert_head_r(self, data):
		self.insert_head(data)

	def insert_tail(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
		else:
			curr_node = self.head
			while curr_node.next:
				curr_node = curr_node.next
			curr_node.next = new_node

	def insert_tail_r(self, data):
		curr_node = self.head
		new_node = Node(data)
		if not curr_node:
			self.head = new_node
		else:
			def _insert_tail_r(curr_node, new_node):
				if curr_node.next:
					_insert_tail_r(curr_node.next, new_node)
				else:
					curr_node.next = new_node
			_insert_tail_r(curr_node, new_node)

	def insert_at(self, data, index):
		curr_node = self.head
		new_node = Node(data)
		if not curr_node or index <= 0:
			self.insert_head(data)
		else:
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

	def insert_at_r(self, data, index):
		curr_node = self.head
		new_node = Node(data)
		if not curr_node or index <= 0:
			self.insert_head_r(data)
		else:
			def _insert_at_r(index, curr_node, curr_node_index, new_node):
				if curr_node.next:
					next_node = curr_node.next
					next_node_index = curr_node_index + 1
					if index == next_node_index:
						curr_node.next = new_node
						new_node.next = next_node
					else:
						_insert_at_r(index, next_node, next_node_index, new_node)
				else:
					curr_node.next = new_node
			_insert_at_r(index, curr_node, 0, new_node)

	def insert(self, data):
		self.insert_tail(data)

	def insert_r(self, data):
		self.insert_tail_r(data)

	def search_left_neighbor(self, key):
		curr_node = self.head
		while curr_node.next:
			if curr_node.next.data == key:
				return curr_node
			else:
				curr_node = curr_node.next

	def search_left_neighbor_r(self, key):
		def _search_left_neighbor_r(key, curr_node):
			if not curr_node.next:
				return None
			elif curr_node.next.data == key:
				return curr_node
			else:
				return _search_left_neighbor_r(key, curr_node.next)
		return _search_left_neighbor_r(key, self.head)

	def search(self, key):
		curr_node = self.head
		if not curr_node:
			return None
		# when the first node is the target
		elif curr_node.data == key:
			return	curr_node.data
		else:
			# neighbor = self.search_left_neighbor_r(key)
			neighbor = self.search_left_neighbor(key)
			if neighbor:
				return neighbor.next.data
			else:
				return None
		
	def delete(self, data):
		curr_node = self.head
		if curr_node:
			# when the first node is the target
			if curr_node.data == data:
				self.head = curr_node.next
			else:
				# neighbor = self.search_left_neighbor_r(data)
				neighbor = self.search_left_neighbor(data)
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

	def reverse_r(self):
		def _reverse_r(prev_node, curr_node):
			if curr_node:
				_reverse_r(curr_node, curr_node.next)
				curr_node.next = prev_node
			else:
				self.head = prev_node
		_reverse_r(None, self.head)

	def show_list(self):
		curr_node = self.head
		print('list: ', end='')
		while curr_node:
			print(curr_node.data, end=' -> ')
			curr_node = curr_node.next
		print(end='None\n')

	def show_list_r(self):
		print('list: ', end='')
		def _show_list_r(curr_node):
			if curr_node:
				print(curr_node.data, end=' -> ')
				_show_list_r(curr_node.next)
		_show_list_r(self.head)
		print(end='None\n')

if __name__ == '__main__':
	print('\n<< Iterative >>\n')
	ll = List()
	ll.insert_head(1)
	ll.show_list()
	ll.insert_head(2)
	ll.show_list()
	ll.insert_head(3)
	ll.show_list()
	ll.insert(4)
	ll.show_list()
	ll.insert(5)
	ll.show_list()
	ll.insert_tail(6)
	ll.show_list()
	ll.insert_at(7, 0)
	ll.show_list()
	ll.insert_at(8, 3)
	ll.show_list()
	ll.insert_at(9, 90)
	ll.show_list()
	ll.delete(7)
	ll.show_list()
	ll.delete(4)
	ll.show_list()
	ll.delete(8)
	ll.show_list()
	print(f'Search {2}: {ll.search(2)}')
	print(f'search {9}: {ll.search(9)}')
	print(f'search {10}: {ll.search(10)}')
	ll.reverse()
	ll.show_list()

	print('\n<< Recursive >>\n')
	ll_r = List()
	ll_r.insert_head_r(1)
	ll_r.show_list_r()
	ll_r.insert_head_r(2)
	ll_r.show_list_r()
	ll_r.insert_head_r(3)
	ll_r.show_list_r()
	ll_r.insert_r(4)
	ll_r.show_list_r()
	ll_r.insert_r(5)
	ll_r.show_list_r()
	ll_r.insert_tail_r(6)
	ll_r.show_list_r()
	ll_r.insert_at_r(7, 0)
	ll_r.show_list_r()
	ll_r.insert_at_r(8, 3)
	ll_r.show_list_r()
	ll_r.insert_at_r(9, 90)
	ll_r.show_list_r()
	ll_r.delete(7)
	ll_r.show_list_r()
	ll_r.delete(4)
	ll_r.show_list_r()
	ll_r.delete(8)
	ll_r.show_list_r()
	print(f'Search {2}: {ll_r.search(2)}')
	print(f'search {9}: {ll_r.search(9)}')
	print(f'search {10}: {ll_r.search(10)}')
	ll_r.reverse_r()
	ll_r.show_list_r()
