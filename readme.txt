--------------------------- Models y Databases--------------------

En Django, los models son una parte fundamental de la estructura de una aplicación, ya que definen la estructura de la base de datos de la aplicación. Los models son clases de Python que heredan de la clase django.db.models.Model y que representan una tabla de la base de datos.

Cuando se realizan cambios en los modelos de Django, como agregar un nuevo campo o modificar una restricción, es necesario crear una migración para que esos cambios se reflejen en la base de datos. El comando makemigrations analiza los modelos actuales y genera las migraciones necesarias para aplicar esos cambios en la base de datos.

python manage.py makemigrations

Es importante destacar que el comando makemigrations no aplica los cambios en la base de datos, solo genera los archivos de migración. Para aplicar las migraciones y actualizar la base de datos, se debe utilizar el comando migrate.

python manage.py migrate


------------------------------Django Admin---------------------------------------

python manage.py createsuperuser



