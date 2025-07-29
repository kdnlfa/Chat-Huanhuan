import re
import json

def parse_script_to_json(text):
    """
    将剧本格式转换为JSON格式
    """
    lines = text.strip().split('\n')
    result = []
    
    for line in lines:
        line = line.strip()
        
        # 跳过空行、舞台提示（括号内容）、场次标题
        if not line or line.startswith('（') or line.startswith('第') or line.startswith('('):
            continue
            
        # 匹配对话行（包含冒号的行）
        match = re.match(r'^(.+?)：(.+)$', line)
        if match:
            role = match.group(1).strip()
            content = match.group(2).strip()
            
            # 清理角色名中的括号描述
            role = re.sub(r'（.*?）', '', role)
            role = re.sub(r'\(.*?\)', '', role)
            role = role.strip()
            
            result.append({
                "rloe": role,
                "content": content
            })
    
    return result

def convert_to_qa_format(dialogue_list):
    """
    将对话格式转换为问答格式
    跳跃式配对：第1句->第2句，第3句->第4句，以此类推
    """
    qa_result = []
    
    # 每次取两个连续的对话作为一对问答
    for i in range(0, len(dialogue_list) - 1, 2):
        instruction_item = dialogue_list[i]
        output_item = dialogue_list[i + 1]
        
        # 创建问答对
        qa_pair = {
            "instruction": instruction_item["content"],
            "input": "",
            "output": output_item["content"]
        }
        
        qa_result.append(qa_pair)
    
    return qa_result

# 示例使用
if __name__ == "__main__":
    # 从JSON文件读取对话数据
    try:
        with open('huanhuan.json', 'r', encoding='utf-8') as f:
            dialogue_data = json.load(f)
            
        # 转换为问答格式
        qa_data = convert_to_qa_format(dialogue_data)
        
        # 保存为新的JSON文件
        with open('huanhuan_qa.json', 'w', encoding='utf-8') as out_f:
            json.dump(qa_data, out_f, ensure_ascii=False, indent=2)
            
        print(f"转换完成！生成了 {len(qa_data)} 个问答对")
        print("已保存到 huanhuan_qa.json 文件")
        
        # 显示前几个示例
        print("\n前3个问答对示例：")
        for i, qa in enumerate(qa_data[:3]):
            print(f"\n问答对 {i+1}:")
            print(f"instruction: {qa['instruction']}")
            print(f"output: {qa['output']}")
            
    except FileNotFoundError:
        print("未找到 huanhuan.json 文件，请先运行剧本解析功能")
    except Exception as e:
        print(f"处理过程中出现错误: {e}")