Модель: Mux
=================

Псевдоним: MATH25
--------------------------

Описание: Мультиплексор
++++++++++++++++++++++++++++++++++++++++++++


.. csv-table:: **Паспорт**
   :header: "Название", "Тип", "Описание", "По умолчанию"
   :widths: 25 10 60 25

   "EXT", "int", "Число внешних степеней свободы","4"
   "ENT", "int", "Число внутренних степеней свободы","0"
   "PAR", "int", "Число параметров простого типа","1"
   "VPR", "list", "Признак переменного числа параметров [None, Variable, Even, Odd]","Variable"
   "STR", "int", "Число переменных состояния","0"
   "STP", "int", "Сколько переменных состояния соответствуют каждому параметру","0"
   "WRK", "int", "Число рабочих переменных","0"
   "WRP", "int", "Сколько рабочих переменных соответствуют каждому параметру","0"
   "ADR", "list", "Ключ, относительно чего записан якобиан [Displacement, Velocity, Acceleration]","Displacement"
   "IGN", "list", "Ключ, какие элементы якобиана игнорировать [None, Velocity, Acceleration, VelocityAcceleration]","Velocity"


.. csv-table:: **Узлы**
   :header: "Название", "Тип", "Описание"
   :widths: 25, 20, 60

   "In", "DOF1", "Входной узел"
   "In2", "DOF1", "Выходной узел"
   "Signal", "DOF1", "Сигнал управления"
   "Out", "DOF1", "Результат"


.. csv-table:: **Параметры**
   :header: "Название", "Тип", "Описание", "По умолчанию"
   :widths: 25, 20, 60, 25

   "Thresh", "real", "Пороговое значение сигнала", "0"


.. csv-table:: **Рабочий вектор**
   :header: "Название", "Тип", "Описание"
   :widths: 25 20 60

   ""


.. csv-table:: **Вектор состояния**
   :header: "Название", "Тип", "Описание"
   :widths: 25 20 60

   ""
