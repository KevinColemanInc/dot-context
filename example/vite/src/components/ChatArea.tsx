// generate a chat box component. use separate components for chat messages, chat window area, text input, chat button. This component should accept in the props languages (strings) and contexts (string array)

import React, { useState } from "react";
import ChatWindow from "./ChatWindow";
import TextInput from "./TextInput";
import ChatButton from "./ChatButton";
import ChatMessage from "./ChatMessage";

interface ChatBoxProps {
  languages: string[];
  contexts: string[];
}

const ChatBox: React.FC<ChatBoxProps> = ({ languages, contexts }) => {
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState<string>("");

  const handleSendMessage = async () => {
    if (input.trim()) {
      const newMessage = input.trim();
      setMessages([...messages, `You: ${newMessage}`]);
      setInput("");

      try {
        const response = await client.SendMessage(
          newMessage,
          languages,
          contexts
        );
        setMessages([...messages, `You: ${newMessage}`, `Bot: ${response}`]);
      } catch (error) {
        setMessages([
          ...messages,
          `You: ${newMessage}`,
          `Bot: Error sending message.`,
        ]);
        console.error("Error sending message:", error);
      }
    }
  };

  return (
    <div className="flex flex-col w-full max-w-md mx-auto p-4 bg-white shadow-lg rounded-lg">
      <ChatWindow messages={messages} />
      <div className="flex mt-4">
        <TextInput value={input} onChange={setInput} />
        <ChatButton onClick={handleSendMessage} />
      </div>
    </div>
  );
};

export default ChatBox;
