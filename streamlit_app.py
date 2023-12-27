import streamlit as st

def main():
    st.title("Demystifying Machine Learning and Artificial Intelligence")

    st.write("Welcome to an in-depth exploration of Machine Learning (ML) and Artificial Intelligence (AI)! "
             "Let's unravel the mysteries behind these transformative technologies.")

    # Styling
    st.markdown(
        """
        <style>
            body {
                background-color: #f8f9fa;
                color: #333;
                font-family: 'Arial', sans-serif;
            }
            .content {
                max-width: 800px;
                margin: auto;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                background-color: #fff;
            }
            h1, h2, h3 {
                color: #007bff;
            }
            .section {
                margin-top: 20px;
            }
            .sub-section {
                margin-top: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.header("Understanding Machine Learning (ML)")

    st.markdown(
        "Machine Learning is a subset of Artificial Intelligence that empowers computers to learn patterns and make decisions without "
        "explicit programming. Let's delve into some common ML techniques."
    )

    st.subheader("1. Supervised Learning")
    st.markdown(
        "In supervised learning, models are trained on labeled data, where each example has an associated label. "
        "This enables the model to make predictions on new, unseen data."
    )
    st.markdown("Example Algorithms:")
    st.markdown("- Linear Regression")
    st.markdown("- Decision Trees")
    st.markdown("- Support Vector Machines")

    st.subheader("2. Unsupervised Learning")
    st.markdown(
        "Unsupervised learning involves finding patterns in unlabeled data. Clustering and dimensionality reduction "
        "are common tasks in this category."
    )
    st.markdown("Example Algorithms:")
    st.markdown("- K-Means Clustering")
    st.markdown("- Principal Component Analysis (PCA)")
    st.markdown("- Autoencoders")

    st.subheader("3. Reinforcement Learning")
    st.markdown(
        "Reinforcement Learning focuses on agents learning to make decisions by interacting with an environment and receiving feedback in the form of rewards or penalties."
    )
    st.markdown("Example Algorithms:")
    st.markdown("- Q-Learning")
    st.markdown("- Deep Q Networks (DQN)")
    st.markdown("- Policy Gradient Methods")

    st.header("Artificial Intelligence (AI)")

    st.markdown(
        "Artificial Intelligence is a broader concept encompassing machines or systems performing tasks that typically require human intelligence. "
        "Machine Learning is a key component of AI."
    )

    st.subheader("AI Applications:")
    st.markdown("- Natural Language Processing (NLP)")
    st.markdown("- Computer Vision")
    st.markdown("- Speech Recognition")
    st.markdown("- Robotics")

    st.header("In Conclusion")

    st.markdown(
        "Machine Learning and Artificial Intelligence are driving innovations across industries. As you continue your journey into the world of AI/ML, "
        "explore the diverse applications and contribute to the advancement of these transformative technologies."
    )

if __name__ == "__main__":
    main()
