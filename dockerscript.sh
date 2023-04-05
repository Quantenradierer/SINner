source .env
cd ./frontend/
npm install
npm run build
cd ..
docker build -f Dockerfile -t sinner . --build-arg OPENAI_API_KEY=$OPENAI_API_KEY --build-arg MJ_CHANNEL_ID=$MJ_CHANNEL_ID --build-arg MJ_PRIVATE_DISCORD_TOKEN=$MJ_PRIVATE_DISCORD_TOKEN --build-arg MJ_SERVER_ID=$MJ_SERVER_ID --build-arg DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY --build-arg DJANGO_HOST=$DJANGO_HOST --build-arg DJANGO_PORT=$DJANGO_PORT
docker stop sinner
docker run -p 8000:80 --mount type=volume,src=sinner-data,target=/app/data --name sinner --rm -it sinner
