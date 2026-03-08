# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  
  It will ask you to go lower despite the number being correct being higher, switching difficulties still shows it as 1-100, and the secret (the answer) is the same. What suprised me was the max attempt number still being able to change. The loading screen and other functions like display color or print still work ok. Hints were also useless. New Game button also doesn't work.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I successfully refactored the project using Codex/Copilot by migrating the core game logic, i.e., check_guess, parse_guess, get_range_for_difficulty, and update_score, from the file app.py into a new file named logic_utils.py. Apart from refactoring the code, I also fixed several critical game logic issues, including the inverted logic in the hint, inconsistent data type handling for the secret number, failure in resetting the game when the user clicks on the New Game option, and errors in displaying the range texts. This strategy has been completely effective in terms of refactoring the code because I have successfully cleaned up the import statements in the file app.py, and I have also updated the test cases according to the new function return contracts. I have checked the effectiveness of the refactoring and fixes by implementing a verification process: verification of the removal of duplicate logic in the codebase, passing all three Pytest cases in the virtual environment, and launching the Streamlit application successfully. It have one issue when fixing: the hints were still wrong, and I had to check the logic again and found that I had to change the hint logic to be correct. I also had to change the logic for the secret number to be a string instead of an integer, which was a bit tricky because I had to make sure that all the comparisons were done correctly. I also had to change the logic for the difficulty levels to be correct, which was also a bit tricky because I had to make sure that all the comparisons were done correctly. Overall, I think the AI suggestions were mostly correct, but I had to verify them carefully and make some adjustments to get everything working correctly.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I determined whether the bug was fixed by running the application using the Streamlit application and checking the functionality manually. I also ran the Pytest test cases to check whether all the test cases were passing. For example, I ran the test case for the check_guess function, which checks whether the guess is correct, too low, or too high. I could see the function working properly and returning the correct results through the test case. AI assisted me in writing the test cases by suggesting the test cases based on the changes I made to the code. It also assisted me in understanding the test cases by explaining what each test case was doing and its significance.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number was constantly changing because `random.randint()` was being executed each time the Streamlit code was re-run, which is every time the user interacts with it. This is because Streamlit works by re-running the entire code from the top down each time the user interacts with it, such as each time a button is clicked or the form is submitted. To explain it more simply, think of it like this: what if every time you blinked, the game reset itself? Well, the secret number is now placed into a session state guard, meaning it is only executed once.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One thing that I hope to continue is refactoring code, as this made it much simpler to test the code. Using Pytest after each major code change was beneficial, as it prevented me from discovering bugs through play testing. If I were to work with AI again on a coding task, I would test each suggestion before continuing, rather than accepting all the suggested code at once and then trying to figure out which one caused the new bug. This project has altered my perspective on working with AI code, as it has taught me that it can appear completely correct but still harbor underlying bugs, such as inverted hints or the lack of session state guards, that do not become apparent until the code is run.
