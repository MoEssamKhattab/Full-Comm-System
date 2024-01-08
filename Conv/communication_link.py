from conv.encoder import encode
from BPSK.bpsk_transmitter import bpsk_transmitter
from channel_demod_channel_decode import channel_demod_channel_decode

def communication_link(s,generator_polynomials,K,fc,Ab,Tb,n,snr_start,snr_end,snr_step):
    """
    Communication Link (Source Encoding -> Channel Encoding -> Modulation -> AWGN Channel -> Demodulation -> Channel Decoding)
    :param s: original bit sequence
    :param generator_polynomials: generator polynomials
    :param K: constraint length
    :param fc: carrier frequency
    :param Ab: amplitude of carrier
    :param Tb: bit duration
    :param n: number of samples in one bit duration
    :param snr_start: start point of SNR
    :param snr_end: end point of SNR
    :param snr_step: step of SNR
    :return: restored bit sequence channel encoded signal
    """
    channel_encoded_sequence = encode(s, generator_polynomials, 3)
    modulated_signal = bpsk_transmitter(channel_encoded_sequence,fc,Ab,Tb,n)
    modulated_signal_without_conv = bpsk_transmitter(s,fc,Ab,Tb,n)
    decoded_signal = channel_demod_channel_decode(s,modulated_signal_without_conv,modulated_signal,generator_polynomials,K,snr_start,snr_end,snr_step,fc,Tb,n)

    return decoded_signal