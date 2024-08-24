import React from "react";

const Footer: React.FC = () => {
  return (
    <footer className=" text-green-100 py-6 bg-green-900">
      <div className="container mx-auto px-6">
        {/* Footer Title */}
        <h2 className="text-xl font-bold text-center mb-4">CheckMate</h2>

        {/* Navigation Menu */}
        <nav className="text-center mb-4">
          <ul className="flex flex-wrap justify-center space-x-6">
            <li>
              <a href="#" className="hover:text-secondary">
                Terms of Service
              </a>
            </li>
            <li>
              <a href="#" className="hover:text-secondary">
                Copyright CheckMate
              </a>
            </li>
            <li>
              <a href="#" className="hover:text-secondary">
                Privacy Policy
              </a>
            </li>
            <li>
              <a href="#" className="hover:text-secondary">
                Contact Us
              </a>
            </li>
            <li>
              <a href="#" className="hover:text-secondary">
                About Us (Built in Seattle)
              </a>
            </li>
          </ul>
        </nav>

        {/* Contact Information */}
        <div className="text-center">
          <p className="hover:text-secondary">
            Email us:{" "}
            <a href="mailto:dev@698expat.com" className="hover:text-secondary">
              support@checkmate.internal
            </a>
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
