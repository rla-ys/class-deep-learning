#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube 스크립트 추출기
YouTube URL을 입력하면 자동으로 자막/스크립트를 추출합니다.
"""

import re
import sys
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def extract_video_id(url):
    """
    YouTube URL에서 비디오 ID를 추출합니다.
    
    Args:
        url (str): YouTube URL
        
    Returns:
        str: 비디오 ID 또는 None
    """
    # 다양한 YouTube URL 형식을 지원
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
        r'youtube\.com\/v\/([^&\n?#]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None


def get_transcript(video_id, language_codes=['ko', 'en']):
    """
    YouTube 비디오의 스크립트를 가져옵니다.
    
    Args:
        video_id (str): YouTube 비디오 ID
        language_codes (list): 우선순위 언어 코드 리스트
        
    Returns:
        str: 스크립트 텍스트 또는 None
    """
    try:
        # 자동 생성 자막 우선 시도
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=language_codes)
        
        # 텍스트 포맷터를 사용하여 깔끔한 텍스트로 변환
        formatter = TextFormatter()
        formatted_text = formatter.format_transcript(transcript)
        
        return formatted_text
        
    except Exception as e:
        print(f"스크립트를 가져오는 중 오류가 발생했습니다: {e}")
        return None


def save_transcript(text, video_id, filename=None):
    """
    스크립트를 파일로 저장합니다.
    
    Args:
        text (str): 스크립트 텍스트
        video_id (str): 비디오 ID
        filename (str): 저장할 파일명 (선택사항)
    """
    if not filename:
        filename = f"transcript_{video_id}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"스크립트가 '{filename}' 파일로 저장되었습니다.")
    except Exception as e:
        print(f"파일 저장 중 오류가 발생했습니다: {e}")


def main():
    """메인 함수"""
    print("=== YouTube 스크립트 추출기 ===\n")
    
    # 사용자로부터 URL 입력 받기
    while True:
        url = input("YouTube URL을 입력하세요 (종료하려면 'quit' 입력): ").strip()
        
        if url.lower() in ['quit', 'exit', 'q']:
            print("프로그램을 종료합니다.")
            break
            
        if not url:
            print("URL을 입력해주세요.")
            continue
        
        # 비디오 ID 추출
        video_id = extract_video_id(url)
        if not video_id:
            print("유효하지 않은 YouTube URL입니다. 다시 입력해주세요.")
            continue
        
        print(f"비디오 ID: {video_id}")
        print("스크립트를 가져오는 중...")
        
        # 스크립트 가져오기
        transcript = get_transcript(video_id)
        
        if transcript:
            print("\n=== 스크립트 내용 ===")
            print(transcript)
            print("\n" + "="*50)
            
            # 파일 저장 여부 확인
            save_choice = input("\n스크립트를 파일로 저장하시겠습니까? (y/n): ").strip().lower()
            if save_choice in ['y', 'yes', '예']:
                custom_filename = input("파일명을 입력하세요 (엔터 시 기본값 사용): ").strip()
                filename = custom_filename if custom_filename else None
                save_transcript(transcript, video_id, filename)
        else:
            print("스크립트를 가져올 수 없습니다.")
        
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
        sys.exit(0)
    except Exception as e:
        print(f"\n예상치 못한 오류가 발생했습니다: {e}")
        sys.exit(1)
