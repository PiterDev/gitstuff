# 🧰 GitStuff  
Manage your, well, Git stuff.

---

## 📖 About  
GitStuff is a lightweight project management tool built using the GitHub API.
Whilte it's not a production-ready product, it servers as a proof of concept and learning project.
The goal was to:
- Gain experience with GitHub's API
- Integrate Django (backend) with SvelteKit (frontend)
- Try to build a faster alternative to conventional project management tools.
---

## 🚀 Getting Started


### ✅ Prerequisites  
- Set up a [GitHub OAuth App](https://github.com/settings/developers)  
- Create `.env` files in both the `backend/` and `frontend/` directories.  
  Refer to the `.env.example` in each folder for required s and secrets.

---

This project can work in two environment setups.  
Either:

- 🐳 In a docker container  
- 💻 On bare metal (e.g. a dev environment)

---

### 🐳 1. Inside a Docker Container  
From the project root, run:

```bash
docker compose up
```

> ℹ️ If you're using an older version of Docker, use `docker-compose up` instead.

### 💻 2. Bare Metal (Development)

#### 📦 Backend Setup

Make sure you have:
- A Python package manager (`uv` recommended, or `pip`)
- A Node package manager (`pnpm`, `npm`, `yarn`, `bun`, etc.)

Open a terminal in the `backend/` folder:

```bash
# If using uv
uv run ./manage.py runserver
```

Or with `pip`:

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run migrations
python ./manage.py migrate

# (Optional) For development: make migrations
python ./manage.py makemigrations
python ./manage.py migrate

# Start the backend server
python ./manage.py runserver
```

---

#### 🧑‍🎨 Frontend Setup

Open a terminal in the `frontend/` folder:

```bash
# Install dependencies
pnpm install  # or npm install / yarn install / bun install

# Start the dev server
pnpm dev  # or npm run dev / yarn dev / bun dev
```

---

## 📂 Project Structure

```txt
.
├── backend/          # Django project
├── frontend/         # SvelteKit app
├── docker-compose.yml
└── README.md
└── LICENSE
```

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.