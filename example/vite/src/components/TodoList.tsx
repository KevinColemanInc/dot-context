import React, { useState } from "react";

const TodoList: React.FC = () => {
  const [todos, setTodos] = useState<string[]>([
    "Give hackathon presentation",
    "High five team members",
    "Swagger back to seats",
  ]);
  const [newTodo, setNewTodo] = useState<string>("");

  const addTodo = () => {
    if (newTodo.trim()) {
      setTodos([...todos, newTodo]);
      setNewTodo("");
    }
  };

  const deleteTodo = (index: number) => {
    setTodos(todos.filter((_, i) => i !== index));
  };

  return (
    <div className="flex flex-col w-full max-w-md mx-auto p-4  rounded-lg bg-green-50 text-2xl">
      <h3 className="text-lg font-bold mb-4">To-Do List</h3>
      <div className="flex mb-4">
        <input
          type="text"
          className="flex-1 p-2 border rounded-l-lg"
          placeholder="Add a new task"
          value={newTodo}
          onChange={(e) => setNewTodo(e.target.value)}
        />
        <button
          onClick={addTodo}
          className="p-2 bg-green-600 text-white rounded-r-lg"
        >
          Add
        </button>
      </div>
      <ul className="list-disc list-inside">
        {todos.map((todo, index) => (
          <li key={index} className="flex justify-between items-center mb-2">
            {todo}
            <button
              onClick={() => deleteTodo(index)}
              className="text-red-600 hover:text-red-800"
            >
              ⏹️ Check
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoList;
