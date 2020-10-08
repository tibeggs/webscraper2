SET log_file=%cd%\batlog.txt
call C:\Users\Timothy\anaconda3\Scripts\activate.bat
cd C:\Users\Timothy\Documents\GitHub\webscraper2
python main.py> %log_file%