# 导入GRADIO
import gradio as gr

# 导入TRANSFORMERS相关包
from transformers import *

# 通过INTERFACE加载PIPELINE并启动阅读理解服务
gr.Interface.from_pipeline(pipeline("question-answering", model="uer/roberta-base-chinese-extractive-qa")).launch()
