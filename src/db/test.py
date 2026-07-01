from src.db.crud import (
    create_or_get_user,
    create_new_conversation,
    add_message,
    get_conversation,
    get_conversations_by_user,
    add_document,
    get_documents
)


def main():

    print("\n========== USER TEST ==========\n")

    user_id = create_or_get_user("ajay")

    print(f"User ID: {user_id}")

    print("\n========== CONVERSATION TEST ==========\n")

    conv_id = create_new_conversation(
        user_id=user_id,
        title="Physics Chat"
    )

    print(f"Conversation ID: {conv_id}")

    print("\n========== MESSAGE TEST ==========\n")

    add_message(
        conv_id=conv_id,
        role="user",
        content="What is Ohm's law?"
    )

    add_message(
        conv_id=conv_id,
        role="assistant",
        content="Ohm's law states V = I × R"
    )

    add_message(
        conv_id=conv_id,
        role="user",
        content="Give me an example."
    )

    conversation = get_conversation(conv_id)

    print("Conversation Details:\n")
    print(f"Title: {conversation['title']}")
    print(f"Last Interacted: {conversation['last_interacted']}")

    print("\nMessages:\n")

    for msg in conversation["messages"]:
        print(f"{msg['role']} -> {msg['content']}")

    print("\n========== DOCUMENT TEST ==========\n")

    add_document(
        conv_id=conv_id,
        filename="physics_notes.pdf"
    )

    add_document(
        conv_id=conv_id,
        filename="ohms_law.pdf"
    )

    docs = get_documents(conv_id)

    print("Documents:\n")

    for doc in docs:
        print(doc)

    print("\n========== USER CONVERSATIONS TEST ==========\n")

    conversations = get_conversations_by_user(user_id)

    for conv_id, title in conversations.items():
        print(f"{conv_id} -> {title}")

    print("\n========== ALL TESTS PASSED ==========\n")


if __name__ == "__main__":
    main()