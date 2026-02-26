# =========================
# Etapa de build
# =========================
FROM node:20-alpine AS build

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos solo package.json y package-lock.json
# Esto aprovecha cache de Docker
COPY frontend/package*.json ./

# Instalamos dependencias
RUN npm install

# Copiamos todo el código del frontend
COPY frontend/. .

# Construimos la app para producción
RUN npm run build

# =========================
# Etapa de producción
# =========================
FROM nginx:alpine

# Copiamos los archivos generados por el build al directorio de nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Exponemos el puerto 80
EXPOSE 80

# Iniciamos nginx
CMD ["nginx", "-g", "daemon off;"]