// generate a chat box component. use separate components for chat messages, chat window area, text input, chat button. This component should accept in the props languages (strings) and contexts (string array)

import React, { useState } from "react";

interface ChatBoxProps {
  languages: string[];
  contexts: string[];
}

const ChatBox: React.FC<ChatBoxProps> = ({ languages, contexts }) => {
  return (
    <div className="flex flex-col w-full max-w-md mx-auto p-4 bg-white shadow-lg rounded-lg">
      <div className="flex mt-4">
        {languages} {contexts}
      </div>
    </div>
  );
};

export default ChatBox;
