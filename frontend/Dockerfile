# Use official Node.js image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Install pnpm globally
RUN corepack enable && corepack prepare pnpm@latest --activate

# Copy lockfile and package manifest first for better caching
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN pnpm install

# Copy rest of the project
COPY . .

# Build the SvelteKit app
RUN pnpm build

# Expose the port (change if you're using a different adapter)
EXPOSE 3000

# Start the app (adjust if using an adapter like node or vercel)
CMD ["pnpm", "preview", "--port", "3000"]
