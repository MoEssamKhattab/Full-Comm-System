import numpy as np
import matplotlib.pyplot as plt
from BPSK.bpsk_receiver import bpsk_receiver
from util.util import awgn, calculate_ber,hamming_distance
from conv.decoder import decode


def channel_demod_channel_decode(bit_seq,bpsk_modulated_sequence_without_conv,modulated_signal,generator_polynomials,K,snr_start, snr_end, snr_step, fc, Tb, n):
    """
    Communication Link (AWGN Channel -> Demodulation -> Channel Decoding) and plot BER vs. SNR
    :param bpsk_modulated_sequence_without_conv:
    :param channel_encoded_sequence:
    :param modulated_signal:
    :param bit_seq: original bit sequence
    :param src_encoded_mod_sig: source encoded modulated signal
    :param channel_encoded_mod_sig: channel encoded modulated signal
    :param snr_start: start point of SNR
    :param snr_end: end point of SNR
    :param snr_step: step of SNR
    :return: restored bit sequence channel encoded signal
    """
    SNR_dB = np.arange(snr_start, snr_end + snr_step, snr_step)
    src_encoded_ber = np.zeros(len(SNR_dB))
    channel_decoded_ber = np.zeros(len(SNR_dB))
    for i in range(len(SNR_dB)):
        # AWGN Channel
        noisy_channel_encoded_sig = awgn(modulated_signal, SNR_dB[i])
        noisy_src_encoded_sig = awgn(bpsk_modulated_sequence_without_conv, SNR_dB[i])

        # Demodulation
        restored_channel_encoded_bit_seq = bpsk_receiver(noisy_channel_encoded_sig, fc, Tb, n)
        restored_src_encoded_bit_seq = bpsk_receiver(noisy_src_encoded_sig, fc, Tb, n)

        # BER
        src_encoded_ber[i] = calculate_ber(bit_seq, restored_src_encoded_bit_seq)
        channel_decoded_signal = decode(restored_channel_encoded_bit_seq,generator_polynomials,K)

        channel_decoded_ber[i] = hamming_distance(bit_seq, channel_decoded_signal)

    plt.plot(SNR_dB, channel_decoded_ber, label='Channel Encoded')
    plt.plot(SNR_dB, src_encoded_ber, label='Source Encoded')
    plt.yscale('log')
    plt.xlabel('SNR (dB)')
    plt.ylabel('BER')
    plt.legend()
    plt.grid()
    plt.show()
    return channel_decoded_signal  # of the max SNR
