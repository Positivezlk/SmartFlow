
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80

FROM node:22-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install || true
COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev"]

