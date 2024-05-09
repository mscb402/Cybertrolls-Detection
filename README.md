> ## 🔔 特别提醒：这个项目是2019年我在学习DL的时候写的。现在已经2024年，以GPT为首的模型在NLP领域已经有了相当大的突破，目前这个项目已经远远过时，无法再给各位提供任何有意义的价值，希望各位学习AI的朋友，不要花时间在我这个项目上面，省的浪费大家宝贵的时间！

# Cybertrolls Detection
Cybertrolls Detection using deep learning

文章发表地址 [http://www.freebuf.com/others-articles/204523.html](http://www.freebuf.com/others-articles/204523.html)

基于深度学习的网络欺凌检测

# 文件说明

- `Dataset for Detection of Cyber-Trolls.json` 是训练数据集，一行一个json对象
- `CybertrollsDetection-Train.ipynb` 是一个ipynb文件,内容是对模型进行训练，可以导入你的jupyter notebook进行查看和运行
- `CybertrollsDetection.ipynb` 模型运行的实际例子，ipynb文件版
- `CybertrollsDetection.py` 模型运行的实际例子，纯python文件版本
- `model.h5` 已经训练好的模型文件
- `word.json` 已经构建好的词表文件

# 使用例子

请务必将`model.h5`和`word.json`文件放在于`CybertrollsDetection.py`相同目录下。

然后需要安装`keras`、`tensorflow`、`numpy`这些库

比如 `pip install keras tensorflow numpy`

安装完成以后，调用下面的语句执行

`python3 CybertrollsDetection.py 'BAD WORDS'`

