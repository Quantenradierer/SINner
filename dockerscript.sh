cd ./frontend/
npm install
npm run build
cd ..
sudo cp -a /var/lib/docker/volumes/sinner-data /var/lib/docker/volumes/$(date)
docker build -f Dockerfile -t sinner .
docker stop sinner
docker run -p 4117:80 --mount type=volume,src=sinner-data,target=/app/data --name sinner --rm -it sinner
