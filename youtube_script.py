import random
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import re

def extract_video_id(url):
    # 正規表現でYouTube動画IDを抽出（11文字）
    patterns = [
        r"v=([a-zA-Z0-9_-]{11})",
        r"youtu\.be/([a-zA-Z0-9_-]{11})"
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

# YouTubeリンク読み込みとID抽出
with open("youtube_links.txt", "r") as f:
    youtube_links = f.read().splitlines()

video_id_list = [extract_video_id(link) for link in youtube_links if extract_video_id(link)]

import random
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

full_text = ""
video_id = ""

# 安全に取得するためのループ
while video_id_list:
    video_id = random.choice(video_id_list)

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = "\n".join([entry['text'] for entry in transcript])
        break  # 成功したらループを抜ける

    except (TranscriptsDisabled, NoTranscriptFound):
        print(f"No transcript for video: {video_id} — removed.")
        video_id_list.remove(video_id)

    except Exception as e:
        print(f"Unexpected error for {video_id}: {e}")
        video_id_list.remove(video_id)

if not full_text:
    print("No valid transcripts found in any of the provided videos.")
else:
    # メール送信処理（省略せずに使える）
    sender_email = "ai.automation.shift@gmail.com"
    receiver_email = "ai.automation.shift@gmail.com"
    app_password = "nhfbfynipbyutspg"

    subject = "Today's English Articles"
    youtube_link = f"https://www.youtube.com/watch?v={video_id}"
    body = f"{youtube_link}\n\n{full_text}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(message)

    print("Email sent successfully!")