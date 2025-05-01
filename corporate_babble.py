# import random
# import tkinter as tk
# from tkinter import messagebox

# # lists of corporate words, 1 is adverbs, 2 is verbs, 3 is nouns
# corporate_words_1 = ['proactively', 'asynchronously', 'synergistically', 'seamlessly', 'dynamically', 'robustly', 'strategically', 'iteratively', 'scalably', 'holistically', 'flexibly', 'optimally', 'efficiently']
# corporate_words_2 = ['circle back on', 'leverage', 'actualize', 'align on', 'implement', 'touch base on', 'audit', 'make strides towards', 'onboard', 'streamline', 'facilitate', 'pivot towards', 'optimize']
# corporate_words_3 = ['stakeholders', 'opportunities', 'deliverables', 'strategy', 'bandwidth', 'buy-ins', 'portfolios', 'touchpoints', 'pipelines', 'initiatives', 'frameworks', 'ecosystems', 'value propositions', 'workstreams']

# # function to generate a random phrase with one random word from each of the three lists
# def generate_phrase():
#     value_1 = random.choice(corporate_words_1)
#     value_2 = random.choice(corporate_words_2)
#     value_3 = random.choice(corporate_words_3)
#     result = f"{value_1} {value_2} {value_3}"
#     label_result.config(text=result)

# # function to let people copy the generated phrase to clipboard
# def copy_to_clipboard():
#     phrase = label_result.cget("text")
#     if phrase:
#         root.clipboard_clear()
#         root.clipboard_append(phrase)
#         messagebox.showinfo("Copied", "Corporate phrase copied to clipboard!")
#     else:
#         messagebox.showwarning("Nothing to Copy", "Generate a phrase first!")

# # function to have the buttons change color slightly as you hover over them
# def on_enter_button(e):
#     e.widget.config(fg="grey")

# def on_leave_button(e):
#     e.widget.config(fg="black")

# # setting up the main window
# root = tk.Tk()
# root.title("Corporate Jargon Generator")
# root.geometry("500x350")
# root.configure(bg="#f0f0f0")

# # showing the title of the page
# title_label = tk.Label(root, text="Corporate Jargon Generator", font=("Times New Roman", 20, "bold"), bg="#f0f0f0", fg="black")
# title_label.pack(pady=15)

# # showing the generated phrase
# label_result = tk.Label(root, text="", wraplength=400, font=("Times New Roman", 16), bg="#f0f0f0", fg="black")
# label_result.pack(pady=20)

# # making the button people press to generate the random phrase
# button_generate = tk.Button(root, text="Generate Phrase", font=("Times New Roman", 16, "bold"), bg="#4CAF50", fg="black", activebackground="#45a049", padx=20, pady=10, command=generate_phrase)
# button_generate.pack(pady=10)

# # button to copy to clipboard
# button_copy = tk.Button(root, text="Copy to Clipboard", font=("Times New Roman", 12), bg="#dddddd", fg="black", activebackground="#cccccc", padx=10, pady=5, command=copy_to_clipboard)
# button_copy.pack(pady=5)

# # bind hover events to buttons
# for button in [button_generate, button_copy]:
#     button.bind("<Enter>", on_enter_button)
#     button.bind("<Leave>", on_leave_button)

# # running the app!
# root.mainloop()

####### below is the streamlit version for website deployment

import random
import streamlit as st
import os

# Corporate jargon word lists
corporate_words_1 = ['proactively', 'asynchronously', 'synergistically', 'seamlessly', 'dynamically', 'robustly', 'strategically', 'iteratively', 'scalably', 'holistically', 'flexibly', 'optimally', 'efficiently']
corporate_words_2 = ['circle back on', 'leverage', 'actualize', 'align on', 'implement', 'touch base on', 'audit', 'make strides towards', 'onboard', 'streamline', 'facilitate', 'pivot towards', 'optimize']
corporate_words_3 = ['stakeholders', 'opportunities', 'deliverables', 'strategy', 'bandwidth', 'buy-ins', 'portfolios', 'touchpoints', 'pipelines', 'initiatives', 'frameworks', 'ecosystems', 'value propositions', 'workstreams']

# Add some clipart image URLs or local image paths
clipart_images = [
    "images/bat.jpg",
    "images/cat.jpg",
    "images/crab.jpg",
    "images/egg.png",
    "images/heart.jpg",
    "images/lil_guy.jpg",
    "images/monkey.jpg",
    "images/no.jpg",
    "images/pikachu.jpg",
    "images/skull.jpg",
    "images/stethoscope.jpg",
    "images/strawberry.jpg",
    "images/tree.jpg"
]

# Check if images exist and are accessible
clipart_images = [img for img in clipart_images if os.path.exists(img)]

st.set_page_config(page_title="Corporate Jargon Generator", layout="centered")

# Custom styles for buttons
st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white !important;
            font-size: 16px;
            border: none;
            padding: 12px 24px;
            cursor: pointer;
            border-radius: 8px;
            transition: background-color 0.2s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .copy-button {
            background-color: #888888;  /* gray */
            color: white;
            font-size: 16px;
            padding: 8px 16px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.2s ease-in-out;
            margin-top: 12px;
        }
        .copy-button:hover {
            background-color: #666666;  /* darker gray */
        }
        #copiedMsg {
            color: green;
            margin-top: 8px;
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

st.title("💼 Corporate Jargon Generator")
st.write("Press the button below to generate a random, buzzword-packed phrase:")

if st.button("Generate Phrase"):
    value_1 = random.choice(corporate_words_1)
    value_2 = random.choice(corporate_words_2)
    value_3 = random.choice(corporate_words_3)
    phrase = f"{value_1} {value_2} {value_3}"

    # Random image
    selected_image = random.choice(clipart_images)

    # Display the phrase and image
    st.markdown(f"<h3 style='color:white;'>{phrase}</h3>", unsafe_allow_html=True)
    st.image(selected_image, use_column_width=True)