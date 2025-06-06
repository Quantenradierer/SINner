cd ./frontend/
npm install
npm run build
cd ..
sudo cp /var/lib/docker/volumes/sinner-data/_data/db.sqlite3 ../backups/db_$(date +%Y-%m-%d_%H%M).sqlite
docker build -f Dockerfile -t sinner .
docker stop sinner
docker wait sinner
docker run --rm -p 4117:80 --mount type=volume,src=sinner-data,target=/app/data --detach --name sinner sinner