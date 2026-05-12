import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI

# 配置
os.environ["OPENAI_API_KEY"] = "sk-qxowgilipvztzzphptdbhqzychcjvjcykrumcpgovlachnen"
os.environ["OPENAI_API_BASE"] = "https://api.siliconflow.cn/v1"

file_path = "C:/Users/15621/Desktop/knowledge.txt"

# 1. 加载文档
loader = TextLoader(file_path, encoding="utf-8")
documents = loader.load()
print("1. ✅ 已加载文档")

# 2. 切分文档
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)
print("2. ✅ 已切分文档")

# 3. 创建向量数据库
embeddings = OpenAIEmbeddings(model="BAAI/bge-large-zh-v1.5")
vectordb = Chroma.from_documents(texts, embeddings)
print("3. ✅ 向量数据库已创建")

# 4. 检索相关内容 (修正的关键点)
retriever = vectordb.as_retriever()
相关文档 = retriever.invoke("这个文档讲了什么内容？") # 使用 invoke 而不是 get_relevant_documents

# 5. 打印结果
print("\n--- 查询结果 ---")
if 相关文档:
    print(f"📝 答案: {相关文档[0].page_content}")
else:
    print("❌ 未检索到相关内容")

print("\n🎉 脚本运行完成！")