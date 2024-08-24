// generate a header component. title is 698 Expat. there is no logo.

// menu items:
// - Home
// - about
// - demo

// ----
import React from "react";
import { Link } from "react-router-dom";

const Header: React.FC = () => {
  return (
    <header className="bg-primary text-white shadow-md">
      <div className="container mx-auto flex justify-between items-center py-4 px-6">
        {/* Title */}
        <h1 className="text-2xl font-bold">698 Expat</h1>

        {/* Navigation Menu */}
        <nav>
          <ul className="flex space-x-8">
            <li>
              <Link to="/" className="hover:text-secondary">
                Home
              </Link>
            </li>
            <li>
              <Link to="/about" className="hover:text-secondary">
                About
              </Link>
            </li>
            <li>
              <Link to="/demo" className="hover:text-secondary">
                Demo
              </Link>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;
