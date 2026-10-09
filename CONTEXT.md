# Schattenakte - Domain Model

## Context

Schattenakte is an application that creates NPCs (Non-Player Characters) for the Shadowrun pen & paper RPG game. It uses GPT models for generating NPC descriptions and Midjourney for image generation.

## Core Components

1. **NPC Creator**: The main module handling character creation
2. **GPT Interface**: Services for interacting with OpenAI's GPT models
3. **Image Generation**: System for generating images using either Midjourney or GPT

## Concepts

### NPC (Non-Player Character)
- A fully detailed character with attributes, skills, and background
- Each NPC has a description generated via GPT
- NPCs can optionally have images associated with them

### Image Generation Process
- Currently implemented through Discord API calls to Midjourney bot
- Generates images using prompts created by GPT system
- Downloads images from Midjourney and saves locally
- Images are used in NPC creation flow, particularly for character portraits

### ImageGeneration Model
- Tracks state of image generation (Created, In Progress, Downloaded, Failed, Done)
- Links to the entity being generated
- Stores URL where image can be found
- Tracks retry counts for failed generations

## External Dependencies

- OpenAI API for GPT language model and DALL-E image generation
- Discord API for Midjourney integration (when using Midjourney)

## Implementation Details

### GPT Operations
- Various GPT prompts tailored to different entity types (NPCs, Locations)
- Translation services that convert templates into appropriate prompts
- Special handling and modification of prompts for Midjourney compatibility

### Image Generation Services
- `pass_prompt`: Sends prompt to Discord bot via API
- `download_midjourney_image`: Downloads generated image from Midjourney URL
- Job system for tracking image generation progress