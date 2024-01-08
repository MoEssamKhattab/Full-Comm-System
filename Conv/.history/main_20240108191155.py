from conv.encoder import encode
from BPSK.bpsk_transmitter import bpsk_transmitter
from channel_demod_channel_decode import channel_demod_channel_decode


def communication_link():
    s = '101101' * 200
    K = 3
    generator_polynomials = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    fc = 0.1
    Ab = 1
    Tb = 100
    n = 1000
    snr_start = -32
    snr_end = -10
    snr_step = 1

    channel_encoded_sequence = encode(s, generator_polynomials, 3)
    modulated_signal = bpsk_transmitter(channel_encoded_sequence,fc,Ab,Tb,n)
    modulated_signal_without_conv = bpsk_transmitter(s,fc,Ab,Tb,n)
    decoded_signal = channel_demod_channel_decode(s,modulated_signal_without_conv,modulated_signal,generator_polynomials,K,snr_start,snr_end,snr_step,fc,Tb,n)

    return decoded_signal