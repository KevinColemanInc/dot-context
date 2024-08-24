import React from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import ChatArea from "./components/ChatArea";

const App: React.FC = () => {
  return (
    <div className="flex flex-col min-h-screen bg-gray-100">
      {/* Header Component */}
      <Header />

      {/* Main content area */}
      <main className="flex flex-1 justify-center items-center p-4">
        <div className="w-full max-w-4xl bg-white shadow-lg rounded-lg">
          <ChatArea />
        </div>
      </main>

      {/* Footer Component */}
      <Footer />
    </div>
  );
};

export default App;
