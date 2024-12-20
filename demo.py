import os
import numpy as np
from scipy.io.wavfile import write
from core.models.model_module_infer import model_module

model_load_paths = ['CoDi_encoders.pth', 'CoDi_text_diffuser.pth', 'CoDi_audio_diffuser_m.pth', 'CoDi_video_diffuser_8frames.pth']
inference_tester = model_module(data_dir='checkpoints/', pth=model_load_paths, fp16=False)
inference_tester = inference_tester.cuda()
inference_tester = inference_tester.eval()

# Give a prompt
prompt = 'a hiphop song.'

# Generate audio
audio_wave = inference_tester.inference(
                xtype = ['audio'],
                condition = [prompt],
                condition_types = ['text'],
                scale = 7.5,
                n_samples = 1, 
                ddim_steps = 50)[0]

# WAVファイルに保存
write('output.wav', 16000, (audio_wave * 32767).astype(np.int16))