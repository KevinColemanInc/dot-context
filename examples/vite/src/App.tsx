import React from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import TodoList from "./components/TodoList";

const App: React.FC = () => {
  return (
    <div className="flex flex-col w-full min-h-screen text-gray-800">
      <Header />

      <main className="flex flex-1 justify-center items-center p-4 w-full max-h-screen">
        <div className="w-full max-w-screen max-h-screen">
          <TodoList />
        </div>
      </main>

      <Footer />
    </div>
  );
};

export default App;
