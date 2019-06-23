# Design-Patterns-in-Python
Most commonly used python design patterns

**1. Abstract Factory:** El método de fábrica abstracta proporciona una interfaz para crear objetos relacionados dependientes, en el ejemplo utilizado, contamos con una tienda de mascotas que cuenta con perros y gatos y dependiendo de la fábrica que elejimos (en este caso hacemos uso de la librería de python "random" para que automáticamente decida la fábrica con la que trabajará) llamaremos esa fábrica pero es posible realizarlo porque respetan la misma interfaz. En la clase de la tienda de mascotas contamos con la función de salida que nos muestra si es un perro o un gato con el sonido característico del animal.

[Código del patrón Abstract Factory](https://github.com/NapsterZ4/Design-Patterns-in-Python/blob/master/design_patterns/venv/include/design_patterns/abstract_factory.py)

*Referencias: Williams, S. (2019). Recuperado de: https://github.com/faif/python-patterns/blob/master/patterns/creational/abstract_factory.py*

**2. Builder:** Este patrón, por su naturaleza realiza la construcción de representaciones por diferentes métodos, utilizamos un ejemplo en la compra de una computadora que tiene diferentes características, tomamos en cuenta la cantidad de memoria física (RAM), cantidad de espacio en disco duro y el modelo de tarjeta gráfica. Los cambios son los siguientes: Se introduce un constructor, un director o ingeniero en hardware y va realizando paso a paso la construcción de la computadora, una característica básica del patrón builder.

[Código del patrón Builder](https://github.com/NapsterZ4/Design-Patterns-in-Python/blob/master/design_patterns/venv/include/design_patterns/builder.py)

*Referencias: Kasampalis, S. (2015). Mastering Python Design Patterns. 2nd ed. Birmingham - Bombay: PACKT Publishing, pp.32 - 33.*

**3. Factory Method:** El objetivo es proporcionar una interfaz para crear familias de objetos relacionados sin especificar la clase concreta. Tenemos un ejemplo sencillo de la fábrica abstracta en el cual tenemos que decidir el nombre y el sexo de una persona a través de métodos de entrada, la , insertamos el nombre y el género representado por: Masculino="M" y Femenino="F". Se realiza por medio e una clase central y la clase fábrica se encarga de la clasificación de las funciones o instancias creadas por la clase abstracta central. 
Tenemos una clase llamada persona con dos métodos para obtener el nombre y genero que a su vez cuentan con dos subclases que permiten imprimir el mensaje. La clase Fábrica tiene los métodos que tienen los argumentos del nombre y género de la persona. El cliente crea la instancia de la clase fábrica y llama los métodos con los argumentos.

[Código el patrón Factory Method](https://github.com/NapsterZ4/Design-Patterns-in-Python/blob/master/design_patterns/venv/include/design_patterns/factory_method.py)

*Referencias: Verma, R. and Giridhar, C. (2011). Design Patters in Python. 1st ed. Testing Perspective, pp.33 - 34.*

**4. Simple Factory (Fábrica de objetos en su implementación mas simple):** Se considera una fábrica porque crea objetos de diferentes tipos en lugar de instancias de objetos directos, es una referencia comprender la implementación mas simple para visualizar el método de fábrica y la fábrica abstracta. Tomamos un ejemplo de la implementación del [método fábrica](https://github.com/NapsterZ4/Design-Patterns-in-Python/blob/master/design_patterns/venv/include/design_patterns/factory_method.py) sobre la selección de animales pero esta vez en la emisión de sonidos. Creamos un producto abstracto llamado "Animal"  de loa cual se derivan dos productos que son perros y gatos para emitir el sonido correspondiente del animal. Establecemos la clase de fábrica para hacer la llamada de los sonidos y se pasa el tipo de argumento al cliente quién debe elejir por input entre perro="Dog" y gato="Cat" (sensible a entradas de Strings).

[Código del patrón Simple Factory](https://github.com/NapsterZ4/Design-Patterns-in-Python/blob/master/design_patterns/venv/include/design_patterns/simple_factory.py)

*Referencias: Giridhar, C. (2016). Learning Python Design Patterns. 2nd ed. Birminghan: PACKT Publishing, pp.107 - 108.*
