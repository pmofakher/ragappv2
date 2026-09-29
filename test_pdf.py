from app.utils.pdf import extract_text


text = extract_text(
    "uploads/تحلیل شبکه های پیچیده.pdf"
)


print(text[:1000])