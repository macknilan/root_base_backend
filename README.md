```bash
██████╗░░█████╗░░█████╗░████████╗  ██████╗░░█████╗░░██████╗███████╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝██║░░██║██║░░██║░░░██║░░░  ██████╦╝███████║╚█████╗░█████╗░░
██╔══██╗██║░░██║██║░░██║░░░██║░░░  ██╔══██╗██╔══██║░╚═══██╗██╔══╝░░
██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░  ██████╦╝██║░░██║██████╔╝███████╗
╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝

██████╗░░█████╗░░█████╗░██╗░░██╗███████╗███╗░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝████╗░██║██╔══██╗
██████╦╝███████║██║░░╚═╝█████═╝░█████╗░░██╔██╗██║██║░░██║
██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██║╚████║██║░░██║
██████╦╝██║░░██║╚█████╔╝██║░╚██╗███████╗██║░╚███║██████╔╝
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░
```

Proyecto que tiene la intención que sirva como plantilla/ejemplo/pruebas para uso de Django Rest Framework.

Esta basado en [Cookiecutter Django](https://cookiecutter-django.readthedocs.io/en/latest/)

Tiene implementado plantillas realizadas con [tailwind](https://flowbite.com/) para la administración de usuarios.

Esta implementado Django Rest Framework para realizar el registro de usuarios.

- La API tiene las siguientes direcciones.
  - Home: http://localhost:8080/
  - Admin: http://localhost:8080/admin/
  - Flower: http://localhost:5555/
  - MailHog: http://localhost:8025/
  - Redoc: http://localhost:8080/api/v1/redoc/
  - Swagge: http://localhost:8080/api/v1/swagger/


Los requerimientos se encuentran en `root-base-backend/requirements`

Para hacer el `build` de proyecto que están especificados en el archivo `local.yml`

```docker
docker compose -f local.yml build
```

Para levantar y ejecutar los servicios.

```docker
docker compose -f local.yml up
```

Eliminar el contenedor de `django` una vez que se levanto el proyecto; esto sirve para hacer cambios/debbugear/pruebas al momento de programar.

Crear las migraciones.

```docker
docker compose -f local.yml run --rm django python manage.py makemigrations
```

Hacer las migraciones.

```docker
docker compose -f local.yml run --rm django python manage.py migrate
```

Crear el super usuario. Antes se tiene que eliminar el contenedor de `django` preferentemente.

```docker
docker compose -f local.yml run --rm django python manage.py createsuperuser
```
Levantar el contenedor de `django`

```docker
docker compose -f local.yml run --rm --service-ports django
```

