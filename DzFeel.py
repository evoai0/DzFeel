def clean_text(text):
    replacements = {
        "راك": "أنت", "راكِ": "أنتِ", "راكم": "أنتم", "راني": "أنا", "رانا": "نحن",
        "كاين": "هناك", "كاينة": "هناك", "كاينين": "هناك", "بزاف": "كثير", "شوية": "قليل",
        "شوية شوية": "ببطء", "مليح": "جيد", "مليحة": "جيدة", "مزيان": "جيد", "مزيانة": "جيدة",
        "واش": "ماذا", "علاش": "لماذا", "نحب": "أحب", "نكره": "أكره", "نقدر": "أستطيع",
        "نحبك": "أحبك", "نحبك بزاف": "أحبك كثيرا", "صحة": "صحة", "يعجبني": "يعجبني",
        "ما يعجبنيش": "لا يعجبني", "خايب": "سيء", "حلو": "جميل", "سخون": "حار", "برد": "بارد",
        "لي": "الذي", "ليها": "التي", "ليهم": "الذين", "صح": "صحيح", "غلط": "خطأ",
        "مليت": "تعبت", "تعبان": "متعب", "زوين": "جميل", "كيما": "كما", "حاجة": "شيء",
        "حاجة باهية": "شيء جيد", "حاجة خايبة": "شيء سيء", "ماشي": "ليس"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    symbols = ['!', '?', '.', ',', '😊', '😢', '👍']
    for sym in symbols:
        text = text.replace(sym, '')
    return text.strip()

def tokenize(text):
    return text.split()

def rule_based_sentiment(text):
    positive_words = {
        "أحب", "ممتع", "جميل", "رائع", "سعيد", "كثير", "حلو", "ممتاز", "مبهر", "لطيف", "مفرح"
    }
    negative_words = {
        "لا يعجبني", "سيء", "حزين", "تعيس", "خايب", "رديء", "سخيف", "صعب", "مزعج", "ممل"
    }
    negations = {"ما", "مش", "ماشي"}

    tokens = tokenize(text)
    score = 0
    negate = False

    for word in tokens:
        if word in negations:
            negate = True
            continue
        if word in positive_words:
            score += -1 if negate else 1
            negate = False
        elif word in negative_words:
            score += 1 if negate else -1
            negate = False
        else:
            negate = False

    if score > 0:
        return "إيجابي"
    elif score < 0:
        return "سلبي"
    else:
        return "محايد"

def analyze_sentiment(text):
    cleaned = clean_text(text)
    return rule_based_sentiment(cleaned)

def test_samples():
    test_samples = [
        "نحب الخدمة تاعو، راهو يخدم مليح.",
        "البرنامج هذا زوين بزاف وساهل في الاستعمال.",
        "عجبني بزاف، مفيد وممتع.",
        "كاين ميزات رائعة ما كنتش نتوقعها.",
        "ما عجبنيش التطبيق، ثقيل بزاف.",
        "فيه أخطاء كثيرة وما يخدمش كيما لازم.",
        "الواجهة خايبة ومعقدة بزاف.",
        "تعبت وانا نحاول نستعملو، غير مشاكل.",
        "جربت البرنامج البارح، راني نشوف فيه.",
        "حملت التطبيق اليوم ومازال ما استعملتو.",
    ]

    for sentence in test_samples:
        result = analyze_sentiment(sentence)
        print(f"🗨️ \"{sentence}\" → {result}")

if __name__ == "__main__":
    # البرنامج لن يعمل أي اختبار إلا إذا ناديت على test_all_samples() بنفسك.
    user_input = input("أدخل جملة باللهجة: ")
    result = analyze_sentiment(user_input)
    print("تحليل المشاعر:", result)

