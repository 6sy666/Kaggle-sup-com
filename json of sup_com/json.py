import os
import re
import shutil

# 设置数据目录路径
datadir = "D:\\pythonvscode\\sup_cop"
ROOT="./"
def copy_json_files():
    for root, dirs, files in os.walk(datadir):
        for file in files:
            if file.endswith('.json')and "info" in file:
                try:
                    # 获取当前目录的父目录名
                    parent_dir = os.path.basename(root)
                    if parent_dir:
                        # 在当前目录创建以父目录名命名的文件夹
                        dataset_dir = os.path.join(ROOT, parent_dir)
                        os.makedirs(dataset_dir, exist_ok=True)
                        
                        # 构建源文件和目标文件的路径
                        source_file = os.path.join(root, file)
                        target_file = os.path.join(dataset_dir, file)
                        shutil.copy(source_file, target_file)
                        # 移动文件
                        print(f"已复制 -> {dataset_dir}")
                    else:
                        print(f"无法获取父目录名: {root}")
                except Exception as e:
                    print(f"处理文件 {file} 时出错: {str(e)}")

if __name__ == "__main__":
    copy_json_files()