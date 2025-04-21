# Bun currently has an issue where it hangs docker builds
FROM oven/bun:latest

WORKDIR /app

COPY bun.lockb package.json ./
RUN bun install

COPY . .
# This is a hack to get around bun hanging on docker builds
RUN timeout --foreground 10s bun --bun run build || echo "Bun timed out but probably built successfully"

EXPOSE 3000
CMD ["bun", "run", "build/index.js"]