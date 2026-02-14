from graphviz import Digraph

# Создаем объект графа
dot = Digraph()

# Определяем узлы
dot.node('A', 'Начало')
dot.node('B', 'Проверить: i > 0')
dot.node('C', 'Инкрементировать: i += 1')
dot.node('D', 'Конец')

# Определяем ребра
dot.edge('A', 'B')
dot.edge('B', 'C', label='да')
dot.edge('B', 'D', label='нет')

# Генерируем граф в файл
dot.render('graph', format='png', cleanup=True)
