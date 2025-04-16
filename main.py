import pygame as pg

from sort_function import *

from typing import Tuple


class App:
    """Главный класс приложения для визуализации алгоритмов сортировки.
    
    Обеспечивает:
    - Инициализацию параметров сортировки
    - Генерацию случайного массива
    - Визуализацию процесса сортировки
    - Управление выполнением (пауза/продолжение)
    
    Attributes:
        clock (pg.time.Clock): Таймер для контроля FPS
        size (int): Размер сортируемого массива
        arr (List[int]): Сортируемый массив
        screen_size (Tuple[int, int]): Размеры окна (ширина, высота)
        width (int): Ширина столбца визуализации
        height (int): Высота единицы значения элемента
        screen (pg.Surface): Поверхность для отрисовки
        time (int): Счетчик времени для контроля задержки
        delay (int): Задержка между шагами сортировки (в кадрах)
        colors (dict): Цвета элементов для визуализации
        running (bool): Флаг выполнения сортировки
        sort: Объект алгоритма сортировки
    """

    def __init__(
            self, size: int, num_range: int, delay: int, 
            sort_name: str = 'BubbleSort',
            screen_size: Tuple[int, int] = (1200, 700), 
        ) -> None:
        """Инициализирует приложение с параметрами визуализации.
        
        Args:
            size: Количество элементов в массиве
            num_range: Максимальное значение элемента (от 1 до num_range)
            delay: Задержка между шагами (в кадрах)
            sort_name: Название алгоритма сортировки (по умолчанию BubbleSort)
            screen_size: Размер окна визуализации (ширина, высота)
        """
        self.clock = pg.time.Clock()
        self.size = size
        self.arr = [randint(1, num_range) for _ in range(size)]
        self.screen_size = self.screen_width, self.screen_height = screen_size
        self.width, self.height = self.screen_width // size, self.screen_height // num_range
        self.screen = pg.display.set_mode(self.screen_size)
        self.time, self.delay = 0, delay
        self.colors = {}
        self.running = False

        name_to_func = {
            'BubbleSort': BubbleSort, 
            'BubbleSortWithFlag': BubbleSortWithFlag, 
            'ShakerSort': ShakerSort, 
            'SelectionSort': SelectionSort, 
            'InsertionSort': InsertionSort, 
            'RandomPermutationSort': RandomPermutationSort,
            'DeleteSort': DeleteSort
        }
        self.sort = name_to_func[sort_name](self)

    def __draw(self) -> None:
        """Отрисовывает текущее состояние массива."""
        self.screen.fill(pg.Color('black'))
        for i, num in enumerate(self.arr):
            col = self.colors.get(i, "gray")
            pg.draw.rect(self.screen, col, (i * self.width, self.screen_height - num * self.height,
                                            self.width - 2, num * self.height))

    def run(self) -> None:
        """Главный цикл приложения."""
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.running = not self.running
            
            if self.running and (self.time % self.delay == 0):
                self.sort.sort_step()
            self.__draw()

            pg.display.flip()
            if self.running:
                self.time += 1
            self.clock.tick(self.clock.get_fps())


if __name__ == "__main__":
    app = App(size=100, num_range=350, delay=1, sort_name='SelectionSort')
    app.run()
