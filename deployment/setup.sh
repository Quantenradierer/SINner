#!/usr/bin/env bash
# One-time (idempotent) server bootstrap for SINner.
#
#   deployment/setup.sh                 core: checks, volume, backup dir, .env
#   deployment/setup.sh --cron          also install the daily backup cron job
#   deployment/setup.sh --systemd       also install a boot unit (docker compose up)
#   deployment/setup.sh --deploy        also run ./dockerscript.sh at the end
#   deployment/setup.sh --all           cron + systemd + deploy
#
# Config via environment (all optional):
#   SINNER_BACKUP_DIR     default /srv/backups/sinner
#   SINNER_VOLUME         default sinner-data
#   SINNER_CONTAINER      default sinner
#   SINNER_RCLONE_REMOTE  if set, baked into the cron job for offsite copies
#   SINNER_CRON_USER      user the cron job runs as (default: current user)
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."
REPO_ROOT="$(pwd)"

BACKUP_DIR="${SINNER_BACKUP_DIR:-/srv/backups/sinner}"
VOLUME="${SINNER_VOLUME:-sinner-data}"
CONTAINER="${SINNER_CONTAINER:-sinner}"
CRON_USER="${SINNER_CRON_USER:-$(id -un)}"

WITH_CRON=0 WITH_SYSTEMD=0 DO_DEPLOY=0
for arg in "$@"; do
    case "$arg" in
        --cron)    WITH_CRON=1 ;;
        --systemd) WITH_SYSTEMD=1 ;;
        --deploy)  DO_DEPLOY=1 ;;
        --all)     WITH_CRON=1; WITH_SYSTEMD=1; DO_DEPLOY=1 ;;
        -h|--help) sed -n '2,20p' "$0"; exit 0 ;;
        *) echo "unknown option: $arg (try --help)" >&2; exit 1 ;;
    esac
done

step() { printf '\n== %s\n' "$1"; }
have() { command -v "$1" >/dev/null 2>&1; }

# ---------------------------------------------------------------- prerequisites
step "prerequisites"
missing=0
for c in docker git; do
    if have "$c"; then echo "  ok   $c"; else echo "  MISS $c"; missing=1; fi
done
if docker compose version >/dev/null 2>&1; then
    echo "  ok   docker compose"
else
    echo "  MISS docker compose (v2 plugin)"; missing=1
fi
if have npm; then echo "  ok   npm"; else echo "  WARN npm not found — dockerscript.sh needs it to build the frontend"; fi
[ "$missing" -eq 0 ] || { echo; echo "install the missing tools and re-run"; exit 1; }

# ------------------------------------------------------------------ data volume
step "docker volume: $VOLUME"
if docker volume inspect "$VOLUME" >/dev/null 2>&1; then
    echo "  exists"
else
    docker volume create "$VOLUME" >/dev/null
    echo "  created"
fi

# ------------------------------------------------------------------- backup dir
step "backup dir: $BACKUP_DIR"
if [ -d "$BACKUP_DIR" ]; then
    echo "  exists"
else
    mkdir -p "$BACKUP_DIR" 2>/dev/null || sudo mkdir -p "$BACKUP_DIR"
    echo "  created"
fi
if [ ! -w "$BACKUP_DIR" ]; then
    sudo chown "$(id -un)" "$BACKUP_DIR"
    echo "  chowned to $(id -un)"
fi

# -------------------------------------------------------------------------- env
step ".env"
ENV_FILE="$REPO_ROOT/.env"
required_keys="DJANGO_SECRET_KEY DJANGO_HOST OPENAI_API_KEY MJ_SERVER_ID MJ_CHANNEL_ID MJ_PRIVATE_DISCORD_TOKEN"
if [ -f "$ENV_FILE" ]; then
    ok=1
    for k in $required_keys; do
        v="$(sed -n "s/^${k}=//p" "$ENV_FILE" | head -n1)"
        [ -n "$v" ] || { echo "  EMPTY  $k"; ok=0; }
    done
    if [ "$ok" -eq 1 ]; then
        echo "  present, required keys set"
    else
        echo; echo "fill the empty keys in $ENV_FILE and re-run"; exit 1
    fi
else
    cp "$REPO_ROOT/deployment/env.example" "$ENV_FILE"
    key="$(LC_ALL=C tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 50)"
    tmp="$(mktemp)"
    sed "s|^DJANGO_SECRET_KEY=.*|DJANGO_SECRET_KEY=${key}|" "$ENV_FILE" > "$tmp"
    mv "$tmp" "$ENV_FILE"
    chmod 600 "$ENV_FILE"
    echo "  created $ENV_FILE with a generated DJANGO_SECRET_KEY"
    echo
    echo ">> Edit $ENV_FILE now: set DJANGO_HOST, OPENAI_API_KEY and the MJ_* keys,"
    echo ">> then re-run this script."
    exit 1
fi

# ---------------------------------------------------------------- backup cron
if [ "$WITH_CRON" -eq 1 ]; then
    step "daily backup cron"
    cron_file="/etc/cron.d/sinner-backup"
    {
        echo "# Managed by deployment/setup.sh"
        echo "PATH=/usr/local/bin:/usr/bin:/bin"
        printf '30 3 * * * %s ' "$CRON_USER"
        printf 'SINNER_BACKUP_DIR=%s ' "$BACKUP_DIR"
        [ -n "${SINNER_RCLONE_REMOTE:-}" ] && printf 'SINNER_RCLONE_REMOTE=%s ' "$SINNER_RCLONE_REMOTE"
        printf '%s/deployment/backup.sh >> /var/log/sinner-backup.log 2>&1\n' "$REPO_ROOT"
    } | sudo tee "$cron_file" >/dev/null
    sudo chmod 644 "$cron_file"
    echo "  wrote $cron_file (runs 03:30 daily as $CRON_USER)"
fi

# -------------------------------------------------------------------- systemd
if [ "$WITH_SYSTEMD" -eq 1 ]; then
    step "systemd boot unit"
    docker_bin="$(command -v docker)"
    unit="/etc/systemd/system/sinner.service"
    sudo tee "$unit" >/dev/null <<EOF
[Unit]
Description=SINner (schattenakte) container stack
Requires=docker.service
After=docker.service network-online.target

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=${REPO_ROOT}
ExecStart=${docker_bin} compose up -d
ExecStop=${docker_bin} compose down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
EOF
    sudo systemctl daemon-reload
    sudo systemctl enable sinner.service >/dev/null
    echo "  enabled sinner.service — the stack comes up on boot"
    echo "  (deploys still go through ./dockerscript.sh)"
fi

# --------------------------------------------------------------------- deploy
if [ "$DO_DEPLOY" -eq 1 ]; then
    step "initial deploy"
    exec "$REPO_ROOT/dockerscript.sh"
fi

step "done"
echo "  next: ./dockerscript.sh   (build + backup + start)"
