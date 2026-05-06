import cv2
import easyocr
import re
import pandas as pd
import os

def extract_text_from_video_cpu(
    video_path,
    output_excel="extracted_signboards.xlsx",
    frame_skip=10,
    downscale_factor=0.5
):
    """
    Extract phone numbers and company names from a video efficiently on CPU.
    
    :param video_path: Path to the video file
    :param output_excel: Path to save Excel output
    :param frame_skip: Process every Nth frame to reduce workload
    :param downscale_factor: Reduce frame resolution to speed up OCR
    """
    
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'], gpu=False)
    
    # Regex patterns
    PHONE_REGEX = r'(\+?233[- ]?\d{9}|0\d{2}[- ]?\d{3}[- ]?\d{3})'
    COMPANY_REGEX = r'([A-Z][A-Za-z&,\.\s]{3,}(?:Ltd|Limited|Company|Enterprise|Ventures|Services|Group)?)'
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Cannot open video: {video_path}")
    
    frame_count = 0
    all_phones = set()
    all_companies = set()
    rows = []

    # Ensure output folder exists
    folder = os.path.splitext(output_excel)[0] + "_frames"
    os.makedirs(folder, exist_ok=True)
    
    print(f"Processing video: {video_path}")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Skip frames to reduce CPU usage
        if frame_count % frame_skip == 0:
            # Downscale frame
            if downscale_factor != 1.0:
                frame = cv2.resize(frame, (0, 0), fx=downscale_factor, fy=downscale_factor)
            
            # OCR
            texts = reader.readtext(frame, detail=0)
            combined_text = " ".join(texts)
            
            # Extract phone numbers & company names
            phones = set(re.findall(PHONE_REGEX, combined_text))
            companies = set(re.findall(COMPANY_REGEX, combined_text))
            
            # Only store new info to avoid duplicates
            new_phones = phones - all_phones
            new_companies = companies - all_companies
            
            if new_phones or new_companies:
                all_phones.update(new_phones)
                all_companies.update(new_companies)
                
                frame_file = f"{folder}/frame_{frame_count}.jpg"
                cv2.imwrite(frame_file, frame)  # optional: save frame
                
                rows.append({
                    "frame_number": frame_count,
                    "phones": ", ".join(new_phones),
                    "companies": ", ".join(new_companies),
                    "raw_text": " | ".join(texts),
                    "frame_file": frame_file
                })
                
                print(f"Frame {frame_count}: Phones={new_phones}, Companies={new_companies}")
        
        frame_count += 1
    
    cap.release()
    
    # Save results to Excel
    df = pd.DataFrame(rows)
    df.to_excel(output_excel, index=False)
    print(f"\n✅ Extraction complete! Results saved to: {output_excel}")
    return output_excel


# Example usage
VIDEO_FILE = r'C:\Users\MASCOM\Pictures\AburiImages.mp4'
extract_text_from_video_cpu(
    video_path=VIDEO_FILE,
    output_excel="mcharty_signboards.xlsx",
    frame_skip=10,       # Process every 10th frame
    downscale_factor=0.5 # Half-size frames for faster OCR
)

