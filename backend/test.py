from PIL import Image


def tile_image(input_path, output_path, grid_rows=10, grid_cols=10):
    # Open the input image
    img = Image.open(input_path)
    w, h = img.size

    # Use the same mode as the input (supports RGBA for transparency)
    mode = img.mode

    # Create a new image with size 10x10 tiles of the original image
    tiled_img = Image.new(
        mode, (w * grid_cols, h * grid_rows), (0, 0, 0, 0) if "A" in mode else None
    )
    h -= 150
    w -= 120
    for row in range(grid_rows):
        for col in range(grid_cols):
            # Checkerboard: rotate every second tile by 180°
            if (row + col) % 2 == 1:
                tile = img.rotate(180)
            else:
                tile = img

            # Paste, using mask if image has an alpha channel
            tiled_img.paste(
                tile, (col * w, row * h), mask=tile if "A" in mode else None
            )

    # Save the result as PNG to preserve transparency
    tiled_img.save(output_path, "PNG")
    print(f"Tiled image saved to {output_path}")


if __name__ == "__main__":
    input_image = "v.png"  # Replace with your input filename
    output_image = "tiled_output.png"  # Output filename
    tile_image(input_image, output_image, grid_rows=10, grid_cols=10)
