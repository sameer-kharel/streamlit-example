import streamlit as st

def main():
    st.title("Machine Learning and Artificial Intelligence")

    st.write("Welcome to the interactive blog post about Machine Learning and Artificial Intelligence!")

    st.header("Machine Learning (ML)")
    st.write("Machine Learning is a subset of Artificial Intelligence that focuses on developing algorithms and models "
             "that enable computers to learn from data and make predictions or decisions without being explicitly programmed.")

    st.subheader("Common ML Techniques:")
    st.markdown("- Supervised Learning: Models learn from labeled training data.")
    st.markdown("- Unsupervised Learning: Models find patterns in unlabeled data.")
    st.markdown("- Reinforcement Learning: Agents learn by interacting with an environment and receiving feedback.")

    with st.expander("Supervised Learning in Detail"):
        st.write("Supervised Learning involves training a model on a labeled dataset, where each example is paired with a "
                 "correct label. The model makes predictions on new, unseen data.")

        st.subheader("Example Algorithms:")
        st.markdown("- Linear Regression")
        st.markdown("- Decision Trees")
        st.markdown("- Support Vector Machines")

    with st.expander("Unsupervised Learning in Detail"):
        st.write("Unsupervised Learning deals with finding patterns and relationships in data without labeled outcomes. "
                 "Clustering and dimensionality reduction are common tasks.")

        st.subheader("Example Algorithms:")
        st.markdown("- K-Means Clustering")
        st.markdown("- Principal Component Analysis (PCA)")
        st.markdown("- Autoencoders")

    with st.expander("Reinforcement Learning in Detail"):
        st.write("Reinforcement Learning involves an agent learning to make decisions by interacting with an environment. "
                 "The agent receives feedback in the form of rewards or penalties.")

        st.subheader("Example Algorithms:")
        st.markdown("- Q-Learning")
        st.markdown("- Deep Q Networks (DQN)")
        st.markdown("- Policy Gradient Methods")

    st.header("Artificial Intelligence (AI)")
    st.write("Artificial Intelligence is a broader concept that encompasses machines or systems that can perform tasks "
             "that typically require human intelligence. Machine Learning is a subset of AI.")

    st.subheader("AI Applications:")
    st.markdown("- Natural Language Processing (NLP)")
    st.markdown("- Computer Vision")
    st.markdown("- Speech Recognition")
    st.markdown("- Robotics")

    st.header("Interactive Demo")

    st.write("Let's explore a simple interactive demo to understand your preferences and experiences in ML and AI.")

    ml_experience = st.slider("How familiar are you with Machine Learning?", 0, 10, 5)
    ai_experience = st.slider("How familiar are you with Artificial Intelligence?", 0, 10, 3)

    st.write(f"Your Machine Learning experience level: {ml_experience}")
    st.write(f"Your Artificial Intelligence experience level: {ai_experience}")

    st.success("Thank you for exploring the interactive demo! Feel free to reach out if you have any questions.")

if __name__ == "__main__":
    main()
