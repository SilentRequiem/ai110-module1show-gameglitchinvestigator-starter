import random
import streamlit as st
from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 8,
    "Normal": 6,
    "Hard": 4,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "active_difficulty" not in st.session_state:
    st.session_state.active_difficulty = difficulty

# Streak feature: tracks consecutive wins and resets on New Game / game over.
# Added it because it was a fun extra feature to implement and also to test that the streak resets correctly on game over and new game.
if "streak" not in st.session_state:
    st.session_state.streak = 0

if st.session_state.active_difficulty != difficulty:
    st.session_state.active_difficulty = difficulty
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.rerun()

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")
st.sidebar.caption(f"Win streak: {st.session_state.streak}")

st.subheader("Make a guess")

col1, col2, col3 = st.columns(3)
with col1:
    with st.form(key=f"guess_form_{difficulty}", clear_on_submit=False):
        raw_guess = st.text_input(
            "Enter your guess:",
            key=f"guess_input_{difficulty}"
        )
        submit = st.form_submit_button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)
        outcome, message = check_guess(guess_int, st.session_state.secret)

        if show_hint:
            st.warning(message)

        if outcome == "Win":
            potential_attempt_number = st.session_state.attempts + 1
            st.session_state.score = update_score(
                current_score=st.session_state.score,
                outcome=outcome,
                attempt_number=potential_attempt_number,
            )
            st.session_state.streak += 1
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            st.session_state.attempts += 1
            st.session_state.score = update_score(
                current_score=st.session_state.score,
                outcome=outcome,
                attempt_number=st.session_state.attempts,
            )
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.session_state.streak = 0
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

potential_win_score = update_score(
    current_score=st.session_state.score,
    outcome="Win",
    attempt_number=st.session_state.attempts + 1,
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts + 1)
    st.write("Score:", st.session_state.score)
    st.write("Potential win score (next correct guess):", potential_win_score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)
    st.write("Streak:", st.session_state.streak)

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {max(0, attempt_limit - st.session_state.attempts)}"
)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
