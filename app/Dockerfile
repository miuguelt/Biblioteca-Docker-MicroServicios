# Usa una imagen de Python basada en Alpine
FROM python:3.12-alpine

# Instala las herramientas de compilación necesarias
RUN apk add --no-cache \
    build-base \
    linux-headers \
    gcc \
    musl-dev

# Establece el directorio de trabajo
RUN mkdir -p /workspace

WORKDIR /workspace

# Copia el archivo de requerimientos
COPY .  /workspace

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para mantener el contenedor en ejecución (ajusta según tus necesidades)
#CMD [ "sleep", "infinity" ]
CMD [ "python", "run.py" ]
