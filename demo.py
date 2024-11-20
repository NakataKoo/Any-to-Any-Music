import os
from core.models.model_module_infer import model_module

model_load_paths = ['CoDi_encoders.pth', 'CoDi_text_diffuser.pth', 'CoDi_audio_diffuser_m.pth', 'CoDi_video_diffuser_8frames.pth']
inference_tester = model_module(data_dir='checkpoints/', pth=model_load_paths, fp16=False) # turn on fp16=True if loading fp16 weights
inference_tester = inference_tester.cuda()
inference_tester = inference_tester.eval()

# Give a prompt
prompt = 'a train enters station.'

# Generate audio
audio_wave = inference_tester.inference(
                xtype = ['audio'],
                condition = [prompt],
                condition_types = ['text'],
                scale = 7.5,
                n_samples = 1, 
                ddim_steps = 50)[0]