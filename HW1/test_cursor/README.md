# 🎬 유튜브 스크립트 추출기

유튜브 URL만 입력하면 자동으로 스크립트를 추출해주는 파이썬 프로그램입니다.

## ✨ 주요 기능

- 🔗 유튜브 URL에서 자동으로 비디오 ID 추출
- 📝 자동으로 스크립트 추출 (한국어 우선)
- 💾 스크립트를 텍스트 파일로 저장
- 🎯 다양한 유튜브 URL 형식 지원
- 🖥️ 사용자 친화적인 인터페이스

## 🚀 설치 및 실행

### 1. 필요한 라이브러리 설치

```bash
pip install -r requirements.txt
```

### 2. 프로그램 실행

```bash
python youtube_transcript_extractor.py
```

## 📖 사용법

1. 프로그램을 실행합니다
2. 유튜브 URL을 입력합니다 (예: `https://www.youtube.com/watch?v=VIDEO_ID`)
3. 스크립트가 자동으로 추출됩니다
4. 필요시 파일로 저장할 수 있습니다

### 지원하는 URL 형식

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`

## 🔧 주요 함수

### `extract_video_id(url)`
- 유튜브 URL에서 비디오 ID를 추출합니다
- 다양한 URL 형식을 지원합니다

### `get_transcript(video_id, language='ko')`
- 지정된 비디오 ID의 스크립트를 가져옵니다
- 한국어를 우선으로 하며, 없으면 사용 가능한 언어를 사용합니다

### `save_transcript(transcript, video_id, filename=None)`
- 스크립트를 텍스트 파일로 저장합니다
- 파일명을 지정하지 않으면 `transcript_VIDEO_ID.txt`로 저장됩니다

## ⚠️ 주의사항

- 모든 유튜브 비디오에 스크립트가 있는 것은 아닙니다
- 스크립트가 없는 비디오의 경우 오류 메시지가 표시됩니다
- 일부 비디오는 자동 생성된 자막만 있을 수 있습니다

## 🛠️ 요구사항

- Python 3.6+
- youtube-transcript-api 0.6.2

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.
