class Node:

	def __init__(self, string='', start = 0, father = None, root = False):

		self.root = root
		self.start = start
		self.suffixes = 0
		self.children = list()
		self.label = string
		self.mapping = dict()
		self.father = father
		self.strings=list()
		self.mark=0       
		self.lcs = '' 

	def insert(self, string, str_pos = 0, preffix = ''):
		'''
		Insere o sufixo na árvore
		'''
		print('Inserindo a string '+string+' no nó '+self.label)
		self.suffixes += 1
		if not str_pos:
			str_pos = self.suffixes

		if self.root:	
			if self.children:
				for child in self.children:
					preffix = child.get_commom_preffix(string)

					if preffix:
						child.insert(string, str_pos, preffix)
						break
				if not preffix:
					self.add_children(Node(string, start = str_pos, father = self))

			else:				
				self.add_children(Node(string, start = str_pos, father = self))

		else:

			if preffix == self.label:
				child,child_preffix,_string = self.check_child_preffix(string,str_pos,preffix)
				if child_preffix:
					child.split_node(_string,str_pos,child_preffix)
				else:
					self.split_node(string,str_pos,preffix)
			else:
				self.split_node(string,str_pos,preffix)

	def add_children(self, child):
		'''
		Adiciona os filhos ao nó. 
		'''

		if isinstance(child, list):
			self.children.extend(child)
			for _node in child:
				self.mapping[_node.label] = _node
		else:
			self.children.append(child)
			self.mapping[child.label] = child
		
		return None

	def get_commom_preffix(self, string):
		''' 
		Encontra o maior prefixo em comum entre duas strings.
		'''

		if len(self.label) == len(string):
			_max = self.label
			_min = string
		else:
			_max = max([self.label,string], key=len)
			_min = min([self.label,string], key=len)

		for i, c in enumerate(_min):
			if c != _max[i]:
				return _min[:i]
	    
		return _min


	def children_generator(self, string, start, preffix = ''):
		'''
		Gera os novos filhos do nó cuja aresta será dividida em dois caminhos possíveis
		de sufixo.
		'''
		_label = string.split(preffix, 1)[1]
		_start = start + len(preffix)
		new_node = Node(string=_label, start = _start, father = self)

		_label = self.label.split(preffix, 1)[1]
		_start = self.start + len(preffix)
		splited_node = Node(string=_label, start = _start, father = self)

		return splited_node, new_node


	def check_child_preffix(self, string, start, preffix):
		'''
		Verifica se existe prefixo entre um novo sufixo e os filhos do nó
		de prefixo em comum.
		'''
		if self.children:
			string = string.split(preffix, 1)[1]
			for child in self.children:
				_preffix = child.get_commom_preffix(string)

				if _preffix:
					#child.insert(string, start, _preffix)
					#preffix = preffix + _preffix
					#break
			
					return child,_preffix,string
		return None,'',string

	def split_node(self, string, str_pos, preffix):
		'''
		Divide a aresta, gerando dois filhos para o nó: o antigo e o novo sufixo
		'''
		aux_label = self.label
		splited_node, new_node = self.children_generator(string, str_pos, preffix)
		self.label = preffix

		if splited_node.label:
			old_children = self.children
			splited_node.add_children(old_children)

			self.children = list()
			self.add_children([splited_node,new_node])

			children_to_remove = list(map(lambda x: x.label, old_children))
			for k in children_to_remove:
			    self.mapping.pop(k,None)
		else:
			self.add_children(new_node)

		self.father.mapping[preffix] = self.father.mapping.pop(aux_label)

		return None

	def get_size(self):
		'''Retorna o comprimento do sufixo representado pelo nó
		'''
		return len(self.label)

	def node_classifier(self, positions):
		''' 
		Marca um nó caso este possua filhos que são sufixos de todas as
		strings da lista
		'''
		if self.label == '' and not self.root:
			self.strings.append(positions[self.start])	
			
			for child in self.children:
				child.node_classifier(positions)
				child.father.strings.extend(child.strings)
			
			try:
				self.strings.remove('')
			except:
				pass
				
			if len(set(self.strings)) == (len(set(positions.values()))-1):
				self.mark = 1
	
	
		return None

	def print_tree(self, level = 0):
		'''
		Desenha a árvora de sufixos
		'''
		if level == 0: print('┬')
		for k,v in self.mapping.items():
			if level != 0:
				if k == list(self.mapping.keys())[-1]:
					print('│' + '   '*level + f'└──{k} -> {v.start}')
				else:
					print('│' + '   '*level + f'├──{k} -> {v.start}')
			else:
				if k == list(self.mapping.keys())[-1]:
					print(f'└───{k} -> {v.start}')
				else:
					print(f'├───{k} -> {v.start}')
			if isinstance(v.mapping,dict):
				v.print_tree(level+1)

		return None

	def run(self, string):
		''' Constrói a árvore de sufixos'''
		
		for i in range(len(string)):
			self.insert(string[i:])
			self.print_tree()


if __name__ == '__main__':
	
	#abcab#xuxa$xuxu&
	#bcab#xuxa$xuxu&
	#cab#xuxa$xuxu&
	#ab#xuxa$xuxu&
	#b#xuxa$xuxu&
	##xuxa$xuxu&
	#xuxa$xuxu&
	#uxa$xuxu&
	#xa$xuxu&
	#a$xuxu&
	#$xuxu&
	#xuxu&
	#uxu&
	#xu&
	#u&
	#&

	tree = Node(string = '', root = True)
	tree.run('abcab#xuxa$xuxu&')