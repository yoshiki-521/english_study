# YouTube Transcript Email Automation

YouTube動画の字幕を自動取得し、自分宛にメールで送信するPythonスクリプトです。

ポートフォリオ用に作成した「毎日英語に触れる自動化ツール」です。

---

## プロジェクト概要

`youtube_links.txt` に登録した複数のYouTube動画の中から**ランダムに1本**を選択し、字幕（トランスクリプト）を取得してメールで送信します。

英語学習の習慣化を目的として開発しました。cronやGitHub Actionsなどで毎日自動実行することで、毎朝英語コンテンツを自動的に届けることができます。

---

## 主な機能

- YouTube URLから動画IDを自動抽出
- `youtube_transcript_api` を使用した字幕自動取得
- 字幕が取得できない動画は自動スキップ（エラーハンドリング完備）
- Gmail対応（アプリパスワード使用）
- 動画URLと字幕全文をメール本文に記載

---

## ファイル構成
youtube-transcript-mailer/
├── youtube_script.py          # メインスクリプト
├── youtube_links.txt          # 取得したい動画URLを記載
├── README.md
└── requirements.txt           # （任意）
text---

## 必要環境・インストール

### 必要なライブラリ

```bash
pip install youtube-transcript-api
Gmailアプリパスワード設定

Googleアカウントで2段階認証を有効化
「アプリパスワード」を生成（アプリ：メール）
生成された16文字のパスワードをスクリプト内に設定


⚙️ 使い方
1. 動画URLの登録
youtube_links.txt にYouTubeのURLを1行に1つずつ記載してください。
例：
txthttps://www.youtube.com/watch?v=dQw4w9wgxcq
https://youtu.be/xxxxxxxxxxx
2. スクリプト実行
Bashpython youtube_script.py
実行すると、登録動画からランダムに1本を選んで字幕を取得し、メールを送信します。

📧 送信されるメール内容例
件名: Today's English Articles
本文:
texthttps://www.youtube.com/watch?v=xxxxxxxxxxx

[ここに字幕の全文が表示されます]

🔧 カスタマイズポイント

送信元・宛先メールアドレスの変更
メール件名（subject）の変更
字幕取得後の処理（要約など）の追加
毎日自動実行の設定（GitHub Actions推奨）


🛡️ エラーハンドリング

字幕が無効な動画
字幕が存在しない動画
その他の予期せぬエラー

上記全てに対応し、問題のある動画は自動で除外します。

📌 今後の拡張アイデア

GitHub Actionsによる毎日自動実行
AIによる字幕要約機能
難易度やトピックによるフィルタリング
LINE/Slack通知対応
