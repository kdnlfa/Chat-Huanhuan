# ChatHuanhuan - 甄嬛AI角色扮演聊天机器人

一个基于甄嬛传剧本数据训练的AI角色扮演聊天机器人，让AI扮演甄嬛与用户进行对话。项目基于Meta-Llama-3.1-8B-Instruct模型，使用LoRA微调技术训练。

## 📋 项目简介

ChatHuanhuan是一个有趣的AI角色扮演项目，通过收集和处理《甄嬛传》的剧本数据，训练AI模型扮演甄嬛这一经典角色。用户可以与AI甄嬛进行对话，体验宫斗剧的经典情节和对话风格。

## 🚀 主要特性

- **角色扮演**: AI完美还原甄嬛的说话风格和语调
- **剧本数据**: 基于完整的甄嬛传剧本(第1-76集)进行训练
- **高效训练**: 使用LoRA技术进行参数高效微调
- **即开即用**: 提供完整的训练和推理流程

## 📁 项目结构

```
ChatHuanhuan/
├── download.py              # 模型下载脚本
├── train.py                 # 模型训练脚本  
├── single.py                # 单次推理测试脚本
├── huanhuan_qa.json         # 处理后的问答格式训练数据
├── 数据和数据处理/
│   ├── data_process.py      # 数据预处理脚本
│   ├── huanhuan.json        # 原始对话数据
│   ├── huanhuan_qa.json     # 问答格式数据
│   └── 甄嬛传剧本01-76.txt   # 原始剧本文件(分集)
└── README.md
```

## 🛠️ 安装要求

### 环境要求
- Python 3.8+
- CUDA 11.0+ (GPU训练)
- 内存: 16GB+ (推荐32GB)
- GPU显存: 8GB+ (推荐24GB)

### 依赖包安装

```bash
pip install torch transformers datasets pandas
pip install peft accelerate bitsandbytes
pip install modelscope
```

## 📚 使用教程

### 1. 模型下载

首先下载预训练模型：

```bash
python download.py
```

这会下载Meta-Llama-3.1-8B-Instruct模型到指定目录。

### 2. 数据预处理

如果需要重新处理数据：

```bash
cd 数据和数据处理
python data_process.py
```

数据处理流程：
- 解析剧本文件，提取对话内容
- 将连续对话转换为问答对格式
- 过滤和清理数据，确保质量

### 3. 模型训练

开始训练甄嬛AI模型：

```bash
python train.py
```

训练参数：
- **模型**: Meta-Llama-3.1-8B-Instruct
- **微调方法**: LoRA (r=8, alpha=32)
- **训练轮数**: 3 epochs
- **批次大小**: 4 (梯度累积步数4)
- **学习率**: 1e-4
- **最大长度**: 384 tokens

### 4. 模型推理

使用训练好的模型进行对话：

```bash
python single.py
```

在`single.py`中修改对话内容：

```python
prompt = "嬛嬛你怎么了，朕替你打抱不平！"  # 修改这里的对话内容
```

## 🎯 使用示例

### 训练数据格式
```json
{
  "instruction": "嬛嬛你怎么了，朕替你打抱不平！",
  "input": "",
  "output": "皇上，臣妾只是有些累了，您别担心。"
}
```

### 对话示例
```
皇上：嬛嬛你怎么了，朕替你打抱不平！
嬛嬛：皇上，臣妾只是有些累了，您别担心。臣妾知道您心疼臣妾，但宫中之事，臣妾自会处理。
```

## 🔧 技术细节

### 模型架构
- **基座模型**: Meta-Llama-3.1-8B-Instruct
- **微调技术**: LoRA (Low-Rank Adaptation)
- **目标模块**: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- **数据类型**: bfloat16

### LoRA配置
```python
config = LoraConfig(
    task_type=TaskType.CAUSAL_LM, 
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    r=8,                    # LoRA秩
    lora_alpha=32,          # LoRA alpha参数
    lora_dropout=0.1        # Dropout比例
)
```

### 数据处理
1. **剧本解析**: 提取角色对话，过滤舞台提示
2. **对话配对**: 将连续对话转换为问答对
3. **格式转换**: 转换为训练所需的指令格式
4. **质量控制**: 清理无效数据，确保对话连贯性

## 📋 注意事项

1. **显存要求**: 训练需要较大显存，建议使用RTX 3090或更高配置
2. **训练时间**: 完整训练需要数小时，请耐心等待
3. **模型路径**: 请根据实际下载路径修改`train.py`和`single.py`中的模型路径
4. **数据版权**: 剧本数据仅供学习研究使用

## 🚀 进阶使用

### 自定义训练参数

在`train.py`中可以调整以下参数：
- `num_train_epochs`: 训练轮数
- `per_device_train_batch_size`: 批次大小
- `learning_rate`: 学习率
- `save_steps`: 保存间隔

### 扩展其他角色

可以通过以下方式扩展其他角色：
1. 收集其他角色的对话数据
2. 修改数据处理脚本中的角色提示
3. 重新训练模型

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进项目：
- 数据质量优化
- 训练策略改进
- 新功能添加
- Bug修复

## 📄 许可证

本项目仅供学习和研究使用，不得用于商业目的。

## 📞 联系方式

如有问题或建议，欢迎通过Issue联系我们。

---

*享受与AI甄嬛的对话吧！* 👑 