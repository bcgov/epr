# Reference
# https://automationrhapsody.com/dockerize-react-application-with-a-docker-multi-staged-build/

# ========= BUILD =========
FROM node:10 as builder

WORKDIR /app

COPY package*.json ./

## Install non-dev packages only defined in the package-lock.json
RUN npm set progress=false && npm ci --production

# Copy the contents of the project to the image
COPY . .

# Build the application
RUN npm run build

# ========= RUN ==========
FROM abiosoft/caddy:1.0.3

COPY Caddyfile /etc/Caddyfile

# Copy the build from the previous stage and stick it into Caddy file server
COPY --from=builder /app/build /usr/share/caddy/html
