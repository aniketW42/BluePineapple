#builder
FROM node:20 AS builder

WORKDIR /restaurant
COPY ./package*.json .
RUN npm install --only-production
COPY . .

#production
FROM node:20 AS production
WORKDIR /restaurant
COPY --from=builder /restaurant /restaurant
EXPOSE 3000

CMD ["npm", "run", "devStart"]
