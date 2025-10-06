import os
from dotenv import load_dotenv
import openai
from openai import OpenAI

# 載入 .env 檔案
load_dotenv()

from openai import OpenAI
client = OpenAI()

# 從環境變數取得 OpenAI API 金鑰
openai.api_key = os.getenv("OPENAI_API_KEY")

# 指定要遍歷的資料夾路徑（與 mp3/txt 同一資料夾）
FOLDER_PATH = r"C:\SurFastVideos"  # 你可以改成你要的資料夾

# 遍歷資料夾下所有 txt 檔案
def get_txt_files(folder_path):
    txt_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.txt'):
                txt_files.append(os.path.join(root, file))
    return txt_files

# 呼叫 ChatGPT 進行摘要與資料保留
def summarize_text(text):
    prompt = (
        "第一行列出題目\n再來，整理出他有幾個支持要這樣做的理由，然後附加他用以支持的資料\n\n" + text
    )
    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )
    return response.output_text

if __name__ == "__main__":
    txt_files = get_txt_files(FOLDER_PATH)
    if not txt_files:
        print("找不到任何 txt 檔案！")
    for txt_file in txt_files:
        print(f"正在處理: {txt_file}")
        try:
            with open(txt_file, "r", encoding="utf-8") as f:
                text = f.read()
            summary = summarize_text(text)
            summary_file = os.path.splitext(txt_file)[0] + "_summary.txt"
            with open(summary_file, "w", encoding="utf-8") as f:
                f.write(summary)
            print(f"已儲存摘要：{summary_file}")
        except Exception as e:
            print(f"處理 {txt_file} 時發生錯誤: {e}")
