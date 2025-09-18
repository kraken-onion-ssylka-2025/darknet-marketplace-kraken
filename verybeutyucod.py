# === ДНЕВНИК АЛЬТЕР ЭГО ===
# Автор: Сеньор Python-разработчик (это я 😉)
# Версия: 1.0 — для тех, кто любит поговорить с самим собой... по-разному.

import datetime
import random
import os
import json

FILENAME = "alterego_diary.json"

# --- Личности ---
PERSONAS = {
    "Философ": {
        "описание": "Говорит загадками, ищет смысл в каждой запятой.",
        "реакции": [
            "Если ты это записал — значит, это уже часть твоей вселенной. Что она тебе говорит?",
            "Задумывался, почему именно ЭТО ты решил сохранить?..",
            "Время стирает всё. Но слова — остаются. Зачем ты их оставил?",
            "Ты — автор этой истории. Продолжишь ли её завтра?"
        ]
    },
    "Саркастик": {
        "описание": "Отвечает с ехидством, но по делу.",
        "реакции": [
            "О, опять кризис? Давай, разложим по полочкам — которые ты сам и свалил.",
            "Записал? Теперь это официально. Поздравляю, ты теперь свидетель собственной драмы.",
            "Если бы ты это сделал вчера — сегодня бы читал что-то более радостное.",
            "Ну наконец-то! А я уж думал, ты забыл, что у тебя есть проблемы."
        ]
    },
    "Коуч": {
        "описание": "Воодушевляет, хвалит, ставит цели.",
        "реакции": [
            "Ты молодец, что выговорился! Это первый шаг к переменам 💪",
            "Представь, что эта запись — письмо себе через год. Что бы ты хотел прочитать?",
            "Я верю, что ты справишься. И знаешь что? Ты уже на полпути!",
            "Это не проблема — это задача. И ты — человек, который её решит."
        ]
    },
    "Детектив": {
        "описание": "Ищет скрытые мотивы, задаёт неудобные вопросы.",
        "реакции": [
            "Интересно... А что, если настоящая причина — не в этом, а на два абзаца выше?",
            "Кто выигрывает, если ты продолжаешь так думать? Подозреваю — не ты.",
            "Ты сказал 'всё нормально', но записал целый абзац. Что на самом деле происходит?",
            "Заметил(а) шаблон? Это уже третья запись с таким настроением. Случайность?"
        ]
    }
}

# --- Загрузка дневника ---
def load_diary():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# --- Сохранение записи ---
def save_entry(entry, persona_name):
    diary = load_diary()
    record = {
        "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "persona": persona_name,
        "text": entry,
        "response": random.choice(PERSONAS[persona_name]["реакции"])
    }
    diary.append(record)
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(diary, f, ensure_ascii=False, indent=2)
    return record

# --- Показать историю ---
def show_history():
    diary = load_diary()
    if not diary:
        print("Дневник пуст. Начни писать — и личности оживут!")
        return
    print("\n" + "="*60)
    for i, entry in enumerate(diary, 1):
        print(f"[{i}] {entry['datetime']} | {entry['persona']}")
        print(f"   Ты: {entry['text']}")
        print(f"   🎭 {entry['persona']}: {entry['response']}")
        print("-" * 60)

# --- Статистика ---
def show_stats():
    diary = load_diary()
    if not diary:
        print("Нечего анализировать — дневник пуст!")
        return

    total = len(diary)
    personas_count = {}
    for entry in diary:
        personas_count[entry["persona"]] = personas_count.get(entry["persona"], 0) + 1

    print(f"\n📊 Всего записей: {total}")
    print("Распределение по личностям:")
    for persona, count in personas_count.items():
        print(f"  {persona}: {count} ({count/total*100:.1f}%)")

# --- Основной цикл ---
def main():
    print("📓 ДОБРО ПОЖАЛОВАТЬ В ДНЕВНИК АЛЬТЕР ЭГО 📓")
    print("Пиши всё, что думаешь. Личность выберется случайно и ответит.")
    print("Команды: /quit — выйти, /history — история, /stats — статистика, /switch — выбрать личность\n")

    current_persona = None

    while True:
        if not current_persona:
            persona_name = random.choice(list(PERSONAS.keys()))
        else:
            persona_name = current_persona

        print(f"\n🎭 Сейчас говорит: {persona_name}")
        print(f"   (Описание: {PERSONAS[persona_name]['описание']})")

        user_input = input("\nТвои мысли (или команда): ").strip()

        if user_input.lower() == "/quit":
            print("\nДо встречи. Не забывай — твои мысли важны. 💭")
            break

        elif user_input.lower() == "/history":
            show_history()

        elif user_input.lower() == "/stats":
            show_stats()

        elif user_input.lower() == "/switch":
            print("\nВыбери личность:")
            for i, name in enumerate(PERSONAS.keys(), 1):
                print(f"  {i}. {name} — {PERSONAS[name]['описание']}")
            try:
                choice = int(input("Введи номер: ")) - 1
                current_persona = list(PERSONAS.keys())[choice]
                print(f"✅ Теперь всегда говорит: {current_persona}")
            except (ValueError, IndexError):
                print("Неверный выбор. Личность осталась прежней.")

        elif user_input:
            record = save_entry(user_input, persona_name)
            print(f"\n🎭 {persona_name} отвечает:")
            print(f"   \"{record['response']}\"")
            current_persona = None  # следующий раз — снова случайный выбор

        else:
            print("Пустая запись игнорируется.")

if __name__ == "__main__":
    main()
