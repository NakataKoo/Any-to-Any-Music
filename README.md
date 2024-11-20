[![arXiv](https://img.shields.io/badge/arXiv-2305.11846-brightgreen.svg?style=flat-square)](https://arxiv.org/abs/2305.11846)  [![githubio](https://img.shields.io/badge/GitHub.io-Project_Page-blue?logo=Github&style=flat-square)](https://codi-gen.github.io/)  [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/ZinengTang/CoDi)

## Introduction 

We present Composable Diffusion (CoDi), a novel generative model capable of generating any combination of output modalities, such as language, image, video, or audio, from any combination of input modalities. Unlike existing generative AI systems, CoDi can generate multiple modalities in parallel and its input is not limited to a subset of modalities like text or image. Despite the absence of training datasets for many combinations of modalities, we propose to align modalities in both the input and output space. This allows CoDi to freely condition on any input combination and generate any group of modalities, even if they are not present in the training data. CoDi employs a novel composable generation strategy which involves building a shared multimodal space by bridging alignment in the diffusion process, enabling the synchronized generation of intertwined modalities, such as temporally aligned video and audio. Highly customizable and flexible, CoDi achieves strong joint-modality generation quality, and outperforms or is on par with the unimodal state-of-the-art for single-modality synthesis.  

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