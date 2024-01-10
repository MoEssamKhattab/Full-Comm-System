from JPEG.Utilities.read_image import read_image
from JPEG.DEFS import CompressionMode
from JPEG.encoder import encoder
import numpy as np
from JPEG.Utilities.calculate_compression_ratio import calculate_comprrssion_ratio
from JPEG.decoder import decoder
from JPEG.Utilities.save_image import save_image
import matplotlib.pyplot as plt
from Conv.communication_link import communication_link


def main():
    # ==================== Read Image =======================
    N = 8
<<<<<<< Updated upstream
    image_path = "./img2.jpg"
=======
    image_path = "./ha3.jpeg"
>>>>>>> Stashed changes
    image_array, vertical_padding, horizontal_padding = read_image(image_path, N)

    print(image_array.shape)

    # ==================== Encode Image =======================
    compression_mode = CompressionMode.LOW
    encoded_data, huffman_tree, no_vertical_blocks, no_horizontal_blocks = encoder(image_array, N, compression_mode)

    # ==================== Communication Link =======================
    K = 3
    generator_polynomials = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    fc = 0.1
    Ab = 1
    Tb = 100
    n = 1000
    snr_start = -40
    snr_end = -10
    snr_step = 5
    block_size = 64
    channel_decoded_data = communication_link(encoded_data, generator_polynomials, K, fc, Ab, Tb, n, snr_start, snr_end,
                                              snr_step, block_size)

    # ==================== Decode Image =======================
    decoded_image = decoder(channel_decoded_data, N, compression_mode, vertical_padding, horizontal_padding,
                            huffman_tree, no_vertical_blocks, no_horizontal_blocks)

    # ==================== Calculate Compression Ratio =======================
    compression_ratio = calculate_comprrssion_ratio(image_array, encoded_data)
    print(f"Compression ratio: {compression_ratio}:1")

    # ==================== Show and Save Image =======================
    # save the decoded image as jpg

    original_image = image_array[:decoded_image.shape[0] - vertical_padding,
                     :decoded_image.shape[1] - horizontal_padding]
    save_image(original_image, decoded_image, compression_ratio, compression_mode)


if __name__ == "__main__":
    main()
