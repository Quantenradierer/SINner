
cd ./frontend/
npm run build
cd ..
docker stop sinner
docker build -f Dockerfile -t sinner . --build-arg OPENAI_API_KEY=$OPENAI_API_KEY --build-arg MJ_CHANNEL_ID=$MJ_CHANNEL_ID --build-arg MJ_PRIVATE_DISCORD_TOKEN=$MJ_PRIVATE_DISCORD_TOKEN --build-arg MJ_SERVER_ID=$MJ_SERVER_ID
docker run -p 8000:80 -v ./npcs:/www/data/images/npcs -v ./data:/app/data --name sinner --rm -it sinner
