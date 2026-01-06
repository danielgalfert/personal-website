#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/home/deploy/apps/mysite"
VENV_DIR="$APP_DIR/site_env"
DJANGO_SETTINGS_MODULE="config.settings.production"   # CHANGE if needed
GUNICORN_SERVICE="gunicorn"                           # CHANGE if needed

cd "$APP_DIR"

echo "[1/6] Pull latest code..."
git fetch --all --prune
git reset --hard origin/master

echo "[2/6] Activate venv..."
if [ ! -d "$VENV_DIR" ]; then
  echo "Venv not found at $VENV_DIR. Create it first."
  exit 1
fi
source "$VENV_DIR/bin/activate"

echo "[3/6] Install python deps..."
pip install --upgrade pip
pip install -r requirements.txt


echo "[4/6] Migrate..."
python manage.py migrate --noinput

echo "[5/6] Collect static..."
python manage.py collectstatic --noinput

echo "[6/6] Restart services..."
sudo systemctl restart mysite-gunicorn
sudo systemctl reload nginx

echo "Deploy complete."
