文档问答小工具
做出来的一个RAG应用，能把本地文档喂给大模型，让它基于文档内容回答你的问题。

具体作用
简单说就是：你丢一个文档进去，问它问题，它从文档里找答案给你。比如我放了一份简历进去，问“这个人做过什么项目”，它就能从简历里提取出来回答。解决了大模型瞎编的问题吧。

所需工具
-Python 3.10
-LangChain（边学边用）
-ChromaDB做向量检索
-硅基流动的API

怎么跑起来
bash

装依赖
pip install langchain langchain-community chromadb openai

跑脚本
python rag_demo.py
