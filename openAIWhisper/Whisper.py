import os
from dotenv import load_dotenv
import openai

# 載入 .env 檔案
load_dotenv()

# 從環境變數取得 OpenAI API 金鑰
openai.api_key = os.getenv("OPENAI_API_KEY")


# 指定要遍歷的資料夾路徑（建議用 r 字串避免跳脫字元問題）
FOLDER_PATH = r"C:\SurFastVideos"  # 你可以改成你要的資料夾

# 遍歷資料夾下所有 mp3 檔案
def get_mp3_files(folder_path):
    mp3_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.mp3'):
                mp3_files.append(os.path.join(root, file))
    return mp3_files


def transcribe_audio(file_path, language="zh"):
    with open(file_path, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language=language
        )
    return transcript.text


# 主程式
if __name__ == "__main__":
    mp3_files = get_mp3_files(FOLDER_PATH)
    if not mp3_files:
        print("找不到任何 mp3 檔案！")
    for mp3_file in mp3_files:
        print(f"正在處理: {mp3_file}")
        try:
            text = transcribe_audio(mp3_file, language="zh")
            print(f"內容：{text}\n")
            # 產生同名 txt 檔案路徑
            txt_file = os.path.splitext(mp3_file)[0] + ".txt"
            with open(txt_file, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"已儲存：{txt_file}")
        except Exception as e:
            print(f"處理 {mp3_file} 時發生錯誤: {e}")
