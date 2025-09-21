#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
유튜브 스크립트 추출기
YouTube Transcript Extractor

유튜브 URL을 입력하면 자동으로 스크립트를 추출해주는 프로그램입니다.
"""

import re
import sys
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def extract_video_id(url):
    """
    유튜브 URL에서 비디오 ID를 추출합니다.
    
    Args:
        url (str): 유튜브 URL
        
    Returns:
        str: 비디오 ID 또는 None
    """
    # 다양한 유튜브 URL 형식을 지원
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
        r'youtube\.com\/watch\?.*v=([^&\n?#]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None


def get_transcript(video_id, language='ko'):
    """
    유튜브 비디오의 스크립트를 가져옵니다.
    
    Args:
        video_id (str): 유튜브 비디오 ID
        language (str): 언어 코드 (기본값: 'ko')
        
    Returns:
        str: 스크립트 텍스트 또는 None
    """
    try:
        # 먼저 지정된 언어로 시도
        transcript = YouTubeTranscriptApi().fetch(video_id, languages=[language])
    except:
        try:
            # 지정된 언어가 없으면 사용 가능한 언어 중 첫 번째 사용
            transcript = YouTubeTranscriptApi().fetch(video_id)
        except Exception as e:
            print(f"❌ 스크립트를 가져올 수 없습니다: {e}")
            return None
    
    # 텍스트 포맷터를 사용하여 스크립트를 텍스트로 변환
    formatter = TextFormatter()
    formatted_text = formatter.format_transcript(transcript)
    
    return formatted_text


def save_transcript(transcript, video_id, filename=None):
    """
    스크립트를 파일로 저장합니다.
    
    Args:
        transcript (str): 스크립트 텍스트
        video_id (str): 비디오 ID
        filename (str): 저장할 파일명 (선택사항)
    """
    if not filename:
        filename = f"transcript_{video_id}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(transcript)
        print(f"✅ 스크립트가 '{filename}' 파일로 저장되었습니다.")
    except Exception as e:
        print(f"❌ 파일 저장 중 오류가 발생했습니다: {e}")


def main():
    """메인 프로그램"""
    print("🎬 유튜브 스크립트 추출기")
    print("=" * 50)
    
    while True:
        # 유튜브 URL 입력 받기
        url = input("\n📺 유튜브 URL을 입력하세요 (종료하려면 'quit' 입력): ").strip()
        
        if url.lower() in ['quit', 'exit', '종료', 'q']:
            print("👋 프로그램을 종료합니다.")
            break
        
        if not url:
            print("❌ URL을 입력해주세요.")
            continue
        
        # 비디오 ID 추출
        video_id = extract_video_id(url)
        if not video_id:
            print("❌ 유효하지 않은 유튜브 URL입니다.")
            continue
        
        print(f"🔍 비디오 ID: {video_id}")
        print("📝 스크립트를 가져오는 중...")
        
        # 스크립트 가져오기
        transcript = get_transcript(video_id)
        
        if transcript:
            print("✅ 스크립트를 성공적으로 가져왔습니다!")
            
            # 자동으로 파일로 저장
            save_transcript(transcript, video_id)
        else:
            print("❌ 스크립트를 가져올 수 없습니다. 다른 URL을 시도해보세요.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 프로그램이 중단되었습니다.")
    except Exception as e:
        print(f"\n❌ 예상치 못한 오류가 발생했습니다: {e}")
        sys.exit(1)
