import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    """
    攞 YouTube 影片嘅字幕。

    Args:
        video_id (str): YouTube 影片嘅 ID。

    Returns:
        str: 字幕嘅文字，如果攞唔到就返回 None。
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        output = ''
        for x in transcript:
            sentence = x['text']
            output += f' {sentence}\n'
        return output
    except Exception as e:
        return f"攞唔到字幕: {e}"

def main():
    """
    Streamlit 應用程式嘅主要函數。
    """
    st.title("YouTube 字幕攞取器")

    youtube_url = st.text_input("請輸入 YouTube URL:")

    if youtube_url:
        try:
            # 從 URL 攞影片 ID
            video_id = youtube_url.replace('https://www.youtube.com/watch?v=', '')
            video_id = video_id.split('&')[0]  # 如果有其他參數，例如時間戳記
        except:
            st.error("URL 格式唔啱。")
            return

        st.write(f"影片 ID: {video_id}")

        transcript_text = get_transcript(video_id)

        if transcript_text:
            st.subheader("字幕:")
            st.text_area("字幕內容", value=transcript_text, height=300) # 用 st.text_area 顯示字幕
        else:
            st.error("攞唔到字幕。請檢查 URL 或者影片係咪有字幕。")

if __name__ == "__main__":
    main()
