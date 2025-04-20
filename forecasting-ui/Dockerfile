# ───────────────────────────────────────────────────────────────
#  Stage 1: Build the React (Vite) App
# ───────────────────────────────────────────────────────────────
FROM node:18-alpine AS builder

# Set working dir
WORKDIR /app

# Copy package manifests & install deps
COPY . .
RUN npm i -f

# Copy rest of source
# COPY . .

# Build for production (outputs to /app/dist by default)
RUN npm run build

# ───────────────────────────────────────────────────────────────
#  Stage 2: Serve with nginx
# ───────────────────────────────────────────────────────────────
FROM nginx:alpine

# Remove default nginx site config
# RUN rm /etc/nginx/conf.d/default.conf

# Copy our nginx.conf (see below) into place
# COPY nginx.conf /etc/nginx/conf.d/

# Copy built assets from builder
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Run nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
