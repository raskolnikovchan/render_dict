#関数保存場所
from flask import ( send_file, after_this_request, session)
import tempfile
import os




def send_word_file(doc):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_file:
        doc.save(tmp_file.name)
        tmp_file_path = tmp_file.name

    response = send_file(tmp_file_path, as_attachment=True)
    @after_this_request
    def cleanup(response):
        try:
            os.remove(tmp_file_path)
        except Exception as e:
            print(f"エラー: {e}")
        return response

    return response




def initialize_sessions():
    from main import Word
    session.setdefault("words", [])
    session.setdefault("new_words", [])
    session.setdefault("change_words", [])
    session.setdefault("image_texts", [])
    session.setdefault("heading", [])
    session.setdefault("existing_words", [word.name for word in Word.query.all()])