cd ./frontend/
npm install
npm run build
cd ..
docker build -f Dockerfile -t sinner .
docker stop sinner
docker run -p 4117:80 --mount type=volume,src=sinner-data,target=/app/data --name sinner --rm -it sinner
