import React from "react";

const Header: React.FC = () => {
  return (
    <header className=" text-green-900">
      <div className="container mx-auto flex justify-between items-center py-4 px-6">
        {/* Title */}
        <h1 className="text-2xl font-bold">CheckMate</h1>

        {/* Navigation Menu */}
        <nav className="flex-1">
          <ul className="flex justify-end space-x-8">
            <li>
              <a href={`/`} className="hover:text-secondary">
                Home
              </a>
            </li>
            <li>
              <a href={`/`} className="hover:text-secondary">
                About
              </a>
            </li>
            <li>
              <a href={`/`} className="hover:text-secondary">
                Demo
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;
