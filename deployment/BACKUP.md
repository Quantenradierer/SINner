# Backup & restore

The database is SQLite on a single Docker volume (`sinner-data`). These two
scripts make consistent snapshots and restore them.

- `deployment/backup.sh` — online snapshot + local retention + optional offsite
- `deployment/restore.sh` — stop, snapshot current, swap in a backup, restart

Both are configured with `SINNER_*` environment variables (see the header of
each script). Defaults assume the container is named `sinner` and backups live
in `/srv/backups/sinner`.

## Backup

```bash
sudo mkdir -p /srv/backups/sinner
deployment/backup.sh
```

Produces `db_<timestamp>.sqlite3.gz`. Old ones beyond `SINNER_RETENTION_DAYS`
(14) are pruned. Uses SQLite's online backup API, so it is safe to run while
the app serves traffic.

### Run it daily (cron)

```cron
# /etc/cron.d/sinner-backup   (adjust the path and user)
30 3 * * *  deploy  /srv/SINner/deployment/backup.sh >> /var/log/sinner-backup.log 2>&1
```

### Offsite copy

Set up an [rclone](https://rclone.org/) remote (Backblaze B2, S3, etc.) once,
then point the script at it:

```bash
rclone config                       # create a remote called e.g. "b2"
export SINNER_RCLONE_REMOTE=b2:my-bucket/sinner
deployment/backup.sh
```

Put that `export` in the cron entry or a wrapper so every run ships offsite.

### Also archive generated images (optional)

Regenerating portraits costs real money, so you may want them too:

```bash
export SINNER_BACKUP_IMAGES=1        # adds images_<timestamp>.tar.gz
```

## Restore

```bash
deployment/restore.sh latest            # newest local backup
deployment/restore.sh /srv/backups/sinner/db_2026-08-20_0330.sqlite3.gz
deployment/restore.sh --yes latest      # non-interactive
```

What it does:

1. `docker compose stop web`
2. Copies the current DB to `pre-restore_<timestamp>.sqlite3` next to the source
3. Decompresses/copies the backup into the volume, clears stale WAL/journal files
4. `PRAGMA integrity_check` — on failure it restores the pre-restore copy and
   restarts, leaving you where you started
5. `docker compose up -d` and waits for the healthcheck

The `pre-restore_*` file is your undo. Delete it once you're happy.

## Test your backups

A backup you have never restored is not a backup. Once, on a scratch box or
just before a known-safe moment:

```bash
deployment/backup.sh
deployment/restore.sh --yes latest
# log in, click around, confirm data is intact
```

Do this again after any change to the DB schema tooling or the volume layout.
