# poetry_analysis_assignment.py

# -------- 1. Poet Agent --------
def poet_agent():
    return """
Tears fall in silence, hearts in pain,
Yet hope arises like morning rain.
Dreams once shattered, now take flight,
In darkest hours, we find our light.
"""

# -------- 2. Analyst Agents --------
def lyric_analyst(poem: str):
    return f"""
📝 Lyric Poetry Analysis:
- This poem expresses deep personal emotions and reflections.
- It focuses on internal feelings like pain, hope, sadness, or love.
- Tashreeh (Explanation): The poet shares their inner journey from sorrow to hope, making it a classic example of **lyric poetry**.
"""

def narrative_analyst(poem: str):
    return f"""
📖 Narrative Poetry Analysis:
- This poem narrates a story or journey involving change, characters, or events.
- It follows a beginning, middle, and end structure, like storytelling.
- Tashreeh (Explanation): The transformation from despair to rising hope shows a clear story progression, typical of **narrative poetry**.
"""

def dramatic_analyst(poem: str):
    return f"""
🎭 Dramatic Poetry Analysis:
- This poem appears to be performed or spoken aloud like a monologue.
- It contains expressions or dialogue as if meant for an audience.
- Tashreeh (Explanation): The tone and delivery style suggest performance, similar to stage drama — a sign of **dramatic poetry**.
"""

# -------- 3. Triage / Parent / Orchestrator Agent --------
def triage_agent(poem: str):
    lower_poem = poem.lower()

    # Indicators for lyric poetry
    lyric_keywords = ["i feel", "my heart", "tears", "sad", "happy", "emotions", "hope", "love"]

    # Indicators for narrative poetry
    narrative_keywords = ["once", "then", "he", "she", "they", "suddenly", "story", "journey"]

    # Indicators for dramatic poetry
    dramatic_keywords = ["oh", "alas", "thou", "must i", "you shall", "do not", "act", "perform"]

    if any(word in lower_poem for word in lyric_keywords):
        return lyric_analyst(poem)
    elif any(word in lower_poem for word in narrative_keywords):
        return narrative_analyst(poem)
    elif any(word in lower_poem for word in dramatic_keywords):
        return dramatic_analyst(poem)
    else:
        return "⚠️ Could not detect poetry type. Try adding emotional, storytelling, or dramatic expressions."

# -------- 4. Main System Execution --------
def main():
    print("🎓 Poetry Analysis Assignment - Agent Based System")
    print("--------------------------------------------------")
    
    # Ask user whether to use built-in poem or custom input
    choice = input("\n📌 Do you want to use the built-in poem from poet agent? (y/n): ").strip().lower()
    
    if choice == 'y':
        poem = poet_agent()
        print("\n📜 Poet Agent's Poem:\n")
        print(poem.strip())
    else:
        print("\n✏️ Please enter your poem (minimum 2 lines). Type 'END' on a new line to finish:\n")
        lines = []
        while True:
            line = input()
            if line.strip().lower() == 'end':
                break
            lines.append(line)
        poem = "\n".join(lines)
        print("\n📜 Your Entered Poem:\n")
        print(poem)

    print("\n🔍 Detecting poem type and generating analysis...\n")
    analysis = triage_agent(poem)
    print(analysis)

# -------- Entry Point --------
if __name__ == "__main__":
    main()
