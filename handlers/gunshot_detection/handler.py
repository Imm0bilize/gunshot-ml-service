import io

import torch
import torchaudio
from ts.torch_handler.base_handler import BaseHandler


class GunshotDetectionHandler(BaseHandler):
    def __init__(self):
        super(GunshotDetectionHandler, self).__init__()

        self.img_padding_length = 2000
        self.sample_rate = 16000
        self.n_mels = 128
        self.n_fft = 2048
        self.hop_length = 128
        self.f_min = 32
        self.f_max = 16384
        self.eps = 1e-9

        self._preprocessing = torch.nn.Sequential(
            torchaudio.transforms.MelSpectrogram(
                sample_rate=self.sample_rate,
                n_mels=self.n_mels,
                n_fft=self.n_fft,
                hop_length=self.hop_length,
                f_max=self.f_max,
                f_min=self.f_min,
            )
        )

        self._preprocessing.eval()

    def _normalize(self, spec: torch.Tensor) -> torch.Tensor:
        mean = spec.mean()
        std = spec.std()
        return (spec - mean) / (std + self.eps)

    def preprocess_one_audio(self, req):
        wave, _ = torchaudio.load(io.BytesIO(req.get("data")))

        image = torch.zeros(1, self.n_mels, self.img_padding_length)

        mel_spectrogram = self._normalize(torch.log(self._preprocessing(wave) + self.eps))
        image[0, :, :mel_spectrogram.size(2)] = mel_spectrogram[:, :, :self.img_padding_length]
        image = image.repeat(3, 1, 1)

        return torch.unsqueeze(image, 0)

    def preprocess(self, requests):
        batch = [self.preprocess_one_audio(req) for req in requests]
        return torch.cat(batch)
