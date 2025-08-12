# MFCC Spectrogram conversion code from VGGish, Google Inc.
# https://github.com/tensorflow/models/tree/master/research/audioset

import numpy as np
from scipy.io import wavfile
from . import params
from . import mel_features


def wavform_to_concat_examples(wav_data, lower_edge_hertz=params.MEL_MIN_HZ, 
                               upper_edge_hertz=params.MEL_MAX_HZ, sr=16000):
    
    assert wav_data.dtype == np.int16, 'Bad sample type: %r' % wav_data.dtype
    data = wav_data / 32768.0    # Convert to [-1.0, +1.0]

    # Convert to mono.
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)

    # Compute log mel spectrogram features.
    log_mel = mel_features.log_mel_spectrogram(data,
                                               audio_sample_rate=sr, log_offset=params.LOG_OFFSET, window_length_secs=params.STFT_WINDOW_LENGTH_SECONDS,
                                               hop_length_secs=params.STFT_HOP_LENGTH_SECONDS, num_mel_bins=params.NUM_MEL_BINS,
                                               lower_edge_hertz=lower_edge_hertz, upper_edge_hertz=upper_edge_hertz)

    return log_mel

def wavform_to_examples(wav_data, lower_edge_hertz=params.MEL_MIN_HZ, upper_edge_hertz=params.MEL_MAX_HZ, sr=16000):
    # 여기서 wav data의 형태는 int 16 이어야 함.
    assert wav_data.dtype == np.int16, 'Bad sample type: %r' % wav_data.dtype
    
    # 16비트의 값이 -32,768 ~ 32,767 값이기 때문에 정규화를 해준다.
    data = wav_data / 32768.0    # Convert to [-1.0, +1.0]

    # Convert to mono.
    # Stereo Audio는 (샘플 수, 채널 수(보통 왼쪽, 오른쪽))으로 이루어져 있어서, 이를 단일 채널인 Mono Audio로 바꿔준다.
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)

    # Compute log mel spectrogram features.
    log_mel = mel_features.log_mel_spectrogram(data,
                                               audio_sample_rate=sr, log_offset=params.LOG_OFFSET, window_length_secs=params.STFT_WINDOW_LENGTH_SECONDS,
                                               hop_length_secs=params.STFT_HOP_LENGTH_SECONDS, num_mel_bins=params.NUM_MEL_BINS,
                                               lower_edge_hertz=lower_edge_hertz, upper_edge_hertz=upper_edge_hertz)

    # Frame features into examples.
    features_sample_rate = 1.0 / params.STFT_HOP_LENGTH_SECONDS
    example_window_length = int(round(params.EXAMPLE_WINDOW_SECONDS * features_sample_rate))
    example_hop_length = int(round(params.EXAMPLE_HOP_SECONDS * features_sample_rate))
    log_mel_examples = mel_features.frame(log_mel, window_length=example_window_length, hop_length=example_hop_length)
    return log_mel_examples


def wavfile_to_concat_examples(wav_file, lower_edge_hertz=params.MEL_MIN_HZ, 
                               upper_edge_hertz=params.MEL_MAX_HZ):
    sr, wav_data = wavfile.read(wav_file)
    assert wav_data.dtype == np.int16, 'Bad sample type: %r' % wav_data.dtype
    data = wav_data / 32768.0    # Convert to [-1.0, +1.0]

    # Convert to mono.
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)

    # Compute log mel spectrogram features.
    log_mel = mel_features.log_mel_spectrogram(data,
                                               audio_sample_rate=sr,
                                               log_offset=params.LOG_OFFSET,
                                               window_length_secs=params.STFT_WINDOW_LENGTH_SECONDS,
                                               hop_length_secs=params.STFT_HOP_LENGTH_SECONDS,
                                               num_mel_bins=params.NUM_MEL_BINS,
                                               lower_edge_hertz=lower_edge_hertz,
                                               upper_edge_hertz=upper_edge_hertz)

    return log_mel

def wavfile_to_examples(wav_file, lower_edge_hertz=params.MEL_MIN_HZ, 
                               upper_edge_hertz=params.MEL_MAX_HZ):
    sr, wav_data = wavfile.read(wav_file)
    assert wav_data.dtype == np.int16, 'Bad sample type: %r' % wav_data.dtype
    data = wav_data / 32768.0    # Convert to [-1.0, +1.0]
    # print("sampling rate:", sr, "length", wav_data.shape)

    # Convert to mono.
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)

    # Compute log mel spectrogram features.
    log_mel = mel_features.log_mel_spectrogram(data,
                                               audio_sample_rate=sr,
                                               log_offset=params.LOG_OFFSET,
                                               window_length_secs=params.STFT_WINDOW_LENGTH_SECONDS,
                                               hop_length_secs=params.STFT_HOP_LENGTH_SECONDS,
                                               num_mel_bins=params.NUM_MEL_BINS,
                                               lower_edge_hertz=lower_edge_hertz,
                                               upper_edge_hertz=upper_edge_hertz)

    # print(log_mel.shape)
    # Frame features into examples.
    features_sample_rate = 1.0 / params.STFT_HOP_LENGTH_SECONDS
    example_window_length = int(round(params.EXAMPLE_WINDOW_SECONDS * features_sample_rate))
    example_hop_length = int(round(params.EXAMPLE_HOP_SECONDS * features_sample_rate))
    log_mel_examples = mel_features.frame(log_mel, window_length=example_window_length, hop_length=example_hop_length)
    return log_mel_examples
