# 🎓 Poetry Analysis Agents | AI-Powered Multi-Agent System

> An AI-based poetry classifier and analyzer that detects the type of poem (Lyric, Narrative, or Dramatic) using a multi-agent architecture with intelligent routing and emotional analysis.  
> 💡 Built using Python with a modular and scalable agent system.

---

## 📌 Table of Contents

- [📖 About the Project](#-about-the-project)
- [🚀 Features](#-features)
- [🧠 Agents Overview](#-agents-overview)
- [🛠️ Technologies Used](#-technologies-used)
- [📂 Project Structure](#-project-structure)
- [⚙️ How to Run](#-how-to-run)
- [🧪 Sample Output](#-sample-output)
- [📈 Future Enhancements](#-future-enhancements)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 📖 About the Project

This project demonstrates a simple **AI-powered agent-based system** to classify and analyze poetry into one of the three main types:

- 🎵 **Lyric Poetry** – Emotional and expressive  
- 📜 **Narrative Poetry** – Storytelling-based  
- 🎭 **Dramatic Poetry** – Performance-style monologue/dialogue  

It uses a **parent (triage) agent** that intelligently routes the given poem to the right analyzer agent based on detected keywords and tone.

---

## 🚀 Features

✅ Multi-agent modular structure  
✅ Supports both user-input and pre-defined poems  
✅ Keyword-based intelligent routing  
✅ Tashreeh (explanation) provided per type  
✅ Command-line based interaction  
✅ Beginner-friendly and extendable

---

## 🧠 Agents Overview

| Agent Type | Role |
|------------|------|
| 🧑‍🎤 **Poet Agent** | Supplies a built-in sample poem (2 stanzas) |
| 🧪 **Triage Agent** | Detects poem type and routes to the right analyst |
| 📝 **Lyric Analyst** | Analyzes poems focused on emotions/feelings |
| 📖 **Narrative Analyst** | Analyzes story-based poetic structure |
| 🎭 **Dramatic Analyst** | Analyzes performance/monologue-style poems |

---

## 🛠️ Technologies Used

- ✅ Python 3.x
- ✅ Basic string processing & keyword matching
- ✅ Modular function-based architecture (easily upgradeable)

---

## 📂 Project Structure

```plaintext
📁 poetry-analysis-agents/
├── main.py   # Main Python script
└── README.md                       # Project documentation
```

⚙️ How to Run
🔧 Prerequisites
Python 3 installed

▶️ Steps

# Clone the repository
git clone https://github.com/Tayyaba-Ramzan/Q4-GENAI-Learning

# Run the script
main.py

📥 During execution:
Choose to use built-in poem or enter your own

Enter 2+ lines of poem and type END

The system detects the poem type and prints its Tashreeh (explanation)

📌 Do you want to use the built-in poem from poet agent? (y/n): y

📜 Poet Agent's Poem:
Tears fall in silence, hearts in pain,
Yet hope arises like morning rain.
Dreams once shattered, now take flight,
In darkest hours, we find our light.

🔍 Detecting poem type and generating analysis...

📝 Lyric Poetry Analysis:
- This poem expresses deep personal emotions and reflections.
- Tashreeh: The poet shares their inner journey from sorrow to hope...

📈 Future Enhancements
 Integrate with GPT-based sentiment analysis

 Add GUI using Tkinter or Flask

 Enhance NLP detection using spaCy or NLTK

 Support Urdu poetry (Roman & Unicode)

🤝 Contributing
If you'd like to improve this project, feel free to fork it and send a pull request.

📄 License
This project is open-source and available under the MIT License.

Made with 💻 and 💖 by Tayyaba Ramzan