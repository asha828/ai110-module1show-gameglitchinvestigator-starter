# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The difficulty level didn't make sense. The harder difficulty was easier that the other levels.
Also when you press enter it just does not submit you have to click "submit guess" even thouhg in the text box it says you can hit enter.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1) The difficulty level was wrong
  2) The new game button does not work. I have to reload my page to play a new game.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used ClaudeAI and CoPilot.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

I asked Copilot to help me fix the "too high" and "too low" hints because they were flipped. So Copilot suggested that I change the hints to "Go HIGHER" and "Go LOWER" instead of the opposite. I verified the result by running the game and testing out the hints myself.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
AI suggested I add try/except blocks for when I check if the guess is greater than or less than the secret number. This was incorrect because the guess is always an integer and the secret number is also an integer, so there is no need for a try/except block. I verified this by running the game and testing out different guesses to see if any errors occurred, and they did not.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was really fixed by running the game and testing out the specific functionality that was broken. For example, when I fixed the difficulty level, I ran the game and tested out each difficulty level to see if they were working as expected. If the harder difficulty was actually harder than the easier difficulty, then I knew the bug was fixed.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I manually played the game and tested if the hints were correct and it was which told me that code was working.

- Did AI help you design or understand any tests? How?
AI helped me design some tests that check if the score updated properly after each guess. I asked AI to suggest some test cases for the update_score function, and it gave me some examples of different outcomes and how the score should change based on those outcomes. This helped me understand how the scoring system works and how to test it effectively.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would say that Streamlit reruns the entire script every time there is an interaction with the app, such as clicking a button or entering text. This means that any variables or state that you have in your script will be reset to their initial values unless you use session state to store them. Session state allows you to keep track of variables across reruns, so you can maintain things like the user's score or the history of their guesses even as they interact with the app.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Being thorough in my own testing and makign I sure I understand what's wrong before asking AI for help.
- What is one thing you would do differently next time you work with AI on a coding task?
Spend more time trying to undertand the problem so I can ask targeted questions to AI instead of just asking for the bug to be fixed right away.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project made me realize that AI generated code can be helpful, but it's not always correct and it's important to understand the code and the problem before relying on AI to fix it. It also showed me that AI can be a useful tool for generating ideas and suggestions, but ultimately it's up to the developer to decide what to implement and how to test it.
