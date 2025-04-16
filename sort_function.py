from random import randint


class BubbleSort:
    """Классическая пузырьковая сортировка.
    
    Проходится по массиву многократно, сравнивая и меняя местами соседние элементы.
    Каждый проход уменьшает размер неотсортированной части на 1.
    
    Attributes:
        app: Главное приложение с данными для сортировки.
        size (int): Размер массива.
        i (int): Внешний индекс (граница неотсортированной части).
        j (int): Внутренний индекс (текущая позиция сравнения).
    """
    
    def __init__(self, app) -> None:
        """Инициализирует сортировку с ссылкой на приложение."""
        self.app = app
        self.size = app.size
        self.i, self.j = app.size, 0  # Начинаем с конца массива

    def sort_step(self) -> bool:
        """Выполняет один шаг сортировки.
        
        Returns:
            flag (bool): True если сортировка продолжается, False если завершена
        """
        self.app.colors = {self.j+1: (230, 0, 0)}  # Подсветка текущих элементов
        
        if self.i == 1:  # Условие завершения
            self.app.colors = {}
            return False
            
        if self.app.arr[self.j+1] < self.app.arr[self.j]:  # Сравнение соседей
            self.app.arr[self.j+1], self.app.arr[self.j] = self.app.arr[self.j], self.app.arr[self.j+1]  # Обмен
            
        if self.j == self.i - 2:  # Конец внутреннего прохода
            self.j = -1
            self.i -= 1  # Уменьшаем границу
            
        self.j += 1
        return True


class BubbleSortWithFlag(BubbleSort):
    """Оптимизированная пузырьковая сортировка с флагом.
    
    Добавляет проверку на отсутствие перестановок для досрочного завершения.
    
    Attributes:
        flag (bool): Флаг наличия перестановок на текущем проходе.
    """
    
    def __init__(self, app) -> None:
        """Инициализирует сортировку с ссылкой на приложение."""
        super().__init__(app)
        self.flag = True

    def sort_step(self) -> bool:
        """Выполняет один шаг сортировки.
        
        Returns:
            flag (bool): True если сортировка продолжается, False если завершена
        """
        self.app.colors = {self.j+1: (230, 0, 0)}
        
        if self.i == 1:
            self.app.colors = {}
            return False
            
        if self.app.arr[self.j+1] < self.app.arr[self.j]:
            self.flag = False  # Была перестановка
            self.app.arr[self.j+1], self.app.arr[self.j] = self.app.arr[self.j], self.app.arr[self.j+1]
            
        if self.j == self.i - 2:
            self.j = -1
            self.i -= 1
            if self.flag:  # Если перестановок не было
                self.i = 1  # Завершаем
            self.flag = True  # Сброс флага
            
        self.j += 1
        return True


class ShakerSort:
    """Шейкерная сортировка (двунаправленная пузырьковая).
    
    Проходит массив в обоих направлениях, что ускоряет сортировку.
    
    Attributes:
        positive_direction (bool): Направление текущего прохода.
        k (int): Нижняя граница неотсортированной части.
        i (int): Верхняя граница неотсортированной части.
        j (int): Текущая позиция.
    """
    
    def __init__(self, app) -> None:
        """Инициализирует сортировку с ссылкой на приложение."""
        self.app = app
        self.size = app.size
        self.i, self.k, self.j = app.size, 0, 0
        self.positive_direction = True

    def sort_step(self) -> bool:
        """Выполняет один шаг сортировки.
        
        Returns:
            flag (bool): True если сортировка продолжается, False если завершена.
        """
        if self.positive_direction:
            self.app.colors = {self.j + 1: (230, 0, 0)}
        else:
            self.app.colors = {self.j: (230, 0, 0)}
            
        if self.i == self.k:  # Условие завершения
            self.app.colors = {}
            return False
            
        # Управление границами и направлением    
        if self.j > self.i - 2:
            self.positive_direction = False
            self.j = self.i - 2
            self.i -= 1
            
        if self.j < self.k:
            self.positive_direction = True 
            self.j = self.k
            self.k += 1
            
        # Сравнение и обмен
        if self.app.arr[self.j + 1] < self.app.arr[self.j]:
            self.app.arr[self.j + 1], self.app.arr[self.j] = self.app.arr[self.j], self.app.arr[self.j + 1]

        # Движение в текущем направлении
        self.j += 1 if self.positive_direction else -1
        return True


class SelectionSort:
    """Сортировка выбором - на каждом проходе ищется максимальный элемент.
    
    Attributes:
        max_num (int): Текущее максимальное значение.
        indx (int): Индекс текущего максимального значения.
        i (int): Граница неотсортированной части.
        j (int): Текущий индекс сравнения.
    """
    
    def __init__(self, app) -> None:
        """Инициализирует сортировку с ссылкой на приложение."""
        self.app = app
        self.size = app.size
        self.i, self.j = app.size, 0
        self.max_num, self.indx = -1, 0

    def sort_step(self) -> bool:
        """Выполняет один шаг сортировки.
        
        Returns:
            flag (bool): True если сортировка продолжается, False если завершена.
        """
        self.app.colors = {self.j: (230, 0, 0)}  # Текущий элемент
        
        if self.i == 0:  # Условие завершения
            self.app.colors = {}
            return False
            
        if self.app.arr[self.j] > self.max_num:  # Поиск максимума
            self.max_num = self.app.arr[self.j]
            self.indx = self.j
            
        if self.j == self.i - 1:  # Конец прохода
            self.j = -1
            self.i -= 1
            # Перенос максимума в конец
            self.app.arr[self.i], self.app.arr[self.indx] = self.max_num, self.app.arr[self.i]
            self.max_num, self.indx = -1, 0
            
        self.app.colors[self.indx] = (0, 0, 230)  # Подсветка текущего максимума
        self.j += 1
        return True


class InsertionSort:
    """Сортировка вставками - элементы по одному вставляются в отсортированную часть.
    
    Attributes:
        i (int): Граница между отсортированной и неотсортированной частями.
        j (int): Текущий индекс для вставки.
    """
    
    def __init__(self, app) -> None:
        """Инициализирует сортировку с ссылкой на приложение."""
        self.app = app
        self.size = app.size
        self.i, self.j = 0, 0

    def sort_step(self) -> bool:
        """Выполняет один шаг сортировки.
        
        Returns:
            flag (bool): True если сортировка продолжается, False если завершена.
        """
        self.app.colors = {self.j - 1: (0, 0, 230)}  # Подсветка
        
        if self.i == self.size:  # Условие завершения
            self.app.colors = {}
            return False
            
        if (self.j == 0) or (self.app.arr[self.j] > self.app.arr[self.j - 1]):  # Переход к новому элементу
            self.i += 1
            self.j = self.i
        else:  # Вставка элемента
            self.app.arr[self.j], self.app.arr[self.j - 1] = self.app.arr[self.j - 1], self.app.arr[self.j]
            self.j -= 1
            
        self.app.colors[self.i] = (230, 0, 0)  # Подсветка границы
        return True


class RandomPermutationSort:
    """Экспериментальный алгоритм сортировки случайными перестановками.
    
    Attributes:
        i, j (int): Случайные индексы для перестановки.
        flag (bool): Флаг проверки отсортированности.
        sorted (bool): Флаг завершения сортировки.
        count_of_permutation (int): Счетчик выполненных перестановок.
    """
    
    def __init__(self, app) -> None:
        """Инициализирует сортировку с ссылкой на приложение."""
        self.app = app
        self.size = app.size
        self.i, self.j, self.k = randint(0, self.size - 1), randint(0, self.size - 1), 0
        while self.i == self.j:
            self.i, self.j = randint(0, self.size - 1), randint(0, self.size - 1)
        self.flag = False
        self.sorted = False
        self.count_of_permutation = 0

    def sort_step(self) -> bool:
        """Выполняет один шаг сортировки.
        
        Returns:
            flag (bool): True если сортировка продолжается, False если завершена.
        """
        self.app.colors = {self.i: (230, 0, 0), self.j: (230, 0, 0)}
        
        if self.sorted:  # Условие завершения
            self.app.colors = {}
            return False
            
        if self.flag:  # Фаза проверки
            if self.k == self.size - 2:
                self.sorted = True
            if self.app.arr[self.k] > self.app.arr[self.k + 1]:  # Найдена неотсортированная пара
                self.i, self.j, self.k = randint(0, self.size - 1), randint(0, self.size - 1), -1
                while self.i == self.j:
                    self.i, self.j = randint(0, self.size - 1), randint(0, self.size - 1)
                self.flag = False
                self.sorted = False
            self.k += 1
        else:  # Фаза перестановки
            self.app.arr[self.j], self.app.arr[self.i] = self.app.arr[self.i], self.app.arr[self.j]
            self.count_of_permutation += 1
            self.flag = True
            
        return True


class DeleteSort:
    """Экспериментальный алгоритм сортировки путем удаления неупорядоченных элементов.
    
    Attributes:
        i (int): Текущий индекс проверки.
        flag (bool): Флаг необходимости удаления.
        indx (int): Индекс последнего удаленного элемента.
    """
    
    def __init__(self, app) -> None:
        """Инициализирует сортировку с ссылкой на приложение."""
        self.app = app
        self.size = app.size
        self.i = 0
        self.flag = False
        self.indx = -1

    def sort_step(self) -> bool:
        """Выполняет один шаг сортировки.
        
        Returns:
            flag (bool): True если сортировка продолжается, False если завершена.
        """
        self.app.colors = {self.i: (230, 0, 0), self.i + 1: (230, 0, 0)}
        
        if self.i == self.size - 1:  # Условие завершения
            self.app.colors = {}
            return False
            
        if self.flag:  # Режим проверки после удаления
            if self.app.arr[self.i + 1] < self.app.arr[self.indx]:
                self.app.arr.pop(self.i + 1)
                self.size -= 1
                self.app.width = self.app.screen_width // self.size
            else:
                self.flag = False
                self.indx = -1
        else:  # Основной режим
            if self.app.arr[self.i] > self.app.arr[self.i + 1]:  # Нарушение порядка
                self.flag = True
                self.app.arr.pop(self.i + 1)
                self.size -= 1
                self.app.width = self.app.screen_width // self.size
                self.indx = self.i
            else:
                self.i += 1
                
        return True
