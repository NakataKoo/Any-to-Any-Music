## Installation
```
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirement.txt
```

## Inference
Download checkpoints from [Hugginface Model](https://huggingface.co/ZinengTang/CoDi)

|**Model Parts**|**Huggingface Weights Address**|**fp16 weights**|
|:-------------:|:-------------:|:-------------:|
|CoDi Encoders and VAEs|[CoDi_encoders.pth](https://huggingface.co/ZinengTang/CoDi/resolve/main/CoDi_encoders.pth)|[CoDi_encoders.pth](https://huggingface.co/ZinengTang/CoDi/resolve/main/checkpoints_fp16/CoDi_encoders.pth)|
|CoDi Text Diffuser|[CoDi_text_diffuser.pth](https://huggingface.co/ZinengTang/CoDi/resolve/main/CoDi_text_diffuser.pth)|[CoDi_text_diffuser.pth](https://huggingface.co/ZinengTang/CoDi/resolve/main/checkpoints_fp16/CoDi_text_diffuser.pth)|
|CoDi Audio Diffuser|[CoDi_audio_diffuser_m.pth](https://huggingface.co/ZinengTang/CoDi/resolve/main/CoDi_audio_diffuser_m.pth)|[CoDi_audio_diffuser_m.pth](https://huggingface.co/ZinengTang/CoDi/resolve/main/checkpoints_fp16/CoDi_audio_diffuser_m.pth)|
|CoDi Vision Diffuser|[CoDi_video_diffuser_8frames.pth](https://huggingface.co/ZinengTang/CoDi/resolve/main/CoDi_video_diffuser_8frames.pth)|[CoDi_video_diffuser_8frames.pth](https://huggingface.co/ZinengTang/CoDi/resolve/main/checkpoints_fp16/CoDi_video_diffuser_8frames.pth)|


```
wget https://huggingface.co/ZinengTang/CoDi/resolve/main/CoDi_encoders.pth -P checkpoints/
wget https://huggingface.co/ZinengTang/CoDi/resolve/main/CoDi_text_diffuser.pth -P checkpoints/
wget https://huggingface.co/ZinengTang/CoDi/resolve/main/CoDi_audio_diffuser_m.pth -P checkpoints/
wget https://huggingface.co/ZinengTang/CoDi/resolve/main/CoDi_video_diffuser_8frames.pth -P checkpoints/
```

```
# Or fp16 weights
wget https://huggingface.co/ZinengTang/CoDi/resolve/main/checkpoints_fp16/CoDi_encoders.pth -P checkpoints/
wget https://huggingface.co/ZinengTang/CoDi/resolve/main/checkpoints_fp16/CoDi_text_diffuser.pth -P checkpoints/
wget https://huggingface.co/ZinengTang/CoDi/resolve/main/checkpoints_fp16/CoDi_audio_diffuser_m.pth -P checkpoints/
wget https://huggingface.co/ZinengTang/CoDi/resolve/main/checkpoints_fp16/CoDi_video_diffuser_8frames.pth -P checkpoints/
```

Run demo.ipynb

## Reference

The code structure is based on [Versatile Diffusion](https://github.com/SHI-Labs/Versatile-Diffusion). The audio diffusion model is based on [AudioLDM](https://github.com/haoheliu/AudioLDM). The video diffusion model is partially based on [Make-A-Video](https://github.com/lucidrains/make-a-video-pytorch).

[![arXiv](https://img.shields.io/badge/arXiv-2305.11846-brightgreen.svg?style=flat-square)](https://arxiv.org/abs/2305.11846)  [![githubio](https://img.shields.io/badge/GitHub.io-Project_Page-blue?logo=Github&style=flat-square)](https://codi-gen.github.io/)  [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/ZinengTang/CoDi)