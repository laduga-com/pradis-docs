ПРВП: A
===========

**Псевдоним: **

**Описание: Программа расчета
смасштабированного значения ускорения
узла**


.. csv-table:: **Паспорт**
   :header: "Название", "Тип", "Описание", "По умолчанию"
   :widths: 25 10 60 25

   "OUT", "int", "Число компонент ПРВП","1"
   "SYS", "int", "Число передаваемых в ПРВП внутренних переменных","1"
   "VPS", "list", "Признак переменного числа внутренних переменных [None, Variable, Even, Odd]","0"
   "PAR", "int", "Число параметров простого типа","1"
   "VPR", "list", "Признак переменного числа параметров [None, Variable, Even, Odd]","0"
   "WRK", "int", "Число рабочих переменных","0"
   "WRS", "int", "Сколько рабочих переменных соответствуют каждому внутренней переменной","0"
   "WRP", "int", "Сколько рабочих переменных соответствуют каждому параметру","0"
.. csv-table:: **Узлы**
   :header: "Название", "Тип", "Описание"
   :widths: 25, 20, 60

   "variable", "DOF1", "Произвольная степень свободы."


.. csv-table:: **Параметры**
   :header: "Название", "Тип", "Описание", "По умолчанию"
   :widths: 25, 20, 60, 25

   "scale", "base.real", "Масштаб", "1.0"


.. csv-table:: **Рабочий вектор**
   :header: "Название", "Тип", "Описание"
   :widths: 25 20 60

   ""
