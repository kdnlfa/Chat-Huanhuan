import torch
from modelscope import snapshot_download, AutoModel, AutoTokenizer
import os

try:
    print("开始下载模型...")
    model_dir = snapshot_download(
        'LLM-Research/Meta-Llama-3.1-8B-Instruct', 
        cache_dir='/root/autodl-tmp', 
        revision='master'
    )
    print(f"模型下载完成，保存在: {model_dir}")
    
    # 验证下载是否完成
    required_files = ['config.json', 'pytorch_model.bin', 'tokenizer.json']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(os.path.join(model_dir, file)):
            missing_files.append(file)
    
    if missing_files:
        print(f"警告：缺少文件: {missing_files}")
    else:
        print("所有必需文件都已下载完成")
        
except Exception as e:
    print(f"下载失败: {e}")