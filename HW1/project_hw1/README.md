# 딥러닝 과제 HW1: Cursor/Gemini CLI/Claude CLI 등을 이용한 Vibe 코드 작성1

## 1. 과제 개요
본 과제는 Google Gemini를 비롯한 LLM과의 상호작용을 통해 원하는 프로젝트를 구현하고, 그 과정과 결과물을 GitHub에 기록합니다.

## 2. 사용 도구
* Python
* youtube-transcript-api (파이썬 라이브러리)
* Cursor / Gemini (LLM)

## 3. 개발 과정

### 3.1 LLM과의 상호작용 (Prompt)
본 프로젝트는 다음의 주요 프롬프트를 통해 코드를 생성하고 오류를 해결하는 과정을 거쳤습니다.

#### 최초 코드 생성 프롬프트
"유튜브 스크립트를 추출하는 파이썬 프로그램을 만들어줘. youtube transcript api를 이용할 거야. 내가 유튜브 url만 입력하면 스크립트를 바로 추출해줘"

#### 오류 해결 프롬프트
"pip : 'pip' 용어가 cmdlet, 함수..."
"import 오류 해결: youtube_transcript_api.formatters"
"git add . 오류: fatal: not a git repository..."

## 4. 결과물: YouTube 스크립트 추출기

YouTube URL을 입력하면 자동으로 자막/스크립트를 추출하는 파이썬 프로그램입니다.

### 4.1 기능
- 다양한 YouTube URL 형식 지원 (youtube.com, youtu.be, embed 등)
- 한국어/영어 자막 자동 감지 및 추출
- 스크립트를 콘솔에 출력
- 스크립트를 텍스트 파일로 저장 가능
- 사용자 친화적인 인터페이스

### 4.2 설치 방법
필요한 패키지 설치:
```bash
pip install -r requirements.txt
```
또는 직접 설치:
```bash
pip install youtube-transcript-api
```

### 4.3 사용 방법
1. 프로그램 실행:
```bash
python youtube_transcript_extractor.py
```
2. YouTube URL 입력:
```
YouTube URL을 입력하세요 (종료하려면 'quit' 입력): https://www.youtube.com/watch?v=VIDEO_ID
```
3. 스크립트 확인 및 저장:
   - 추출된 스크립트가 콘솔에 출력됩니다
   - 파일로 저장할지 선택할 수 있습니다

### 4.4 지원하는 URL 형식
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`
- `https://www.youtube.com/v/VIDEO_ID`

### 4.5 예시
```
=== YouTube 스크립트 추출기 ===

YouTube URL을 입력하세요 (종료하려면 'quit' 입력): https://www.youtube.com/watch?v=qgk7ro45ZPI
비디오 ID: qgk7ro45ZPI
스크립트를 가져오는 중...

=== 스크립트 내용 ===
[스크립트 내용이 여기에 표시됩니다]

==================================================

스크립트를 파일로 저장하시겠습니까? (y/n): y
파일명을 입력하세요 (엔터 시 기본값 사용): my_transcript.txt
스크립트가 'my_transcript.txt' 파일로 저장되었습니다.
```

## 주의사항
- 자막이 없는 동영상의 경우 스크립트를 추출할 수 없습니다
- 자동 생성 자막이 있는 동영상만 지원합니다
- 일부 동영상은 지역 제한이나 기타 이유로 스크립트를 가져올 수 없을 수 있습니다

## 문제 해결
- **"스크립트를 가져올 수 없습니다" 오류**: 해당 동영상에 자막이 없거나 접근할 수 없는 경우입니다
- **"유효하지 않은 YouTube URL입니다" 오류**: 올바른 YouTube URL 형식인지 확인해주세요
