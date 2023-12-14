import os

from openai import OpenAI

print(os.getenv("OPENAI_API_KEY"))


if __name__ == "__main__":
    client = OpenAI()
    client.api_key = os.getenv("OPENAI_API_KEY")

    response = client.images.generate(
        model="dall-e-3",
        prompt="Generate an image of a nightclub called 'Velvet Shadows', where the interior design is inspired by Cyberpunk aesthetics. The club's foyer is characterized by soft, pulsating lights that give guests a mysterious aura. The main dance floor should be adorned with complex multicolored lighting and LED strips, creating captivating patterns on the dancing surfaces. Three-dimensional holograms should be shown hovering above the dancing crowd, moving in sync with the futuristic music beats. The club also contains private VIP areas enclosed by semi-transparent glass walls, allowing occupants to retreat from the crowd whilst still being able to observe the spectacles.",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    print(image_url)
