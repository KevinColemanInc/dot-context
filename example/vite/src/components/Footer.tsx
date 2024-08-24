// generate a footer component. title is 698 Expat. there is no logo.

// import
// component/logo

// menu items:
// - Terms of Service linkts to /tos
// - Copyright 698 Expat no link
// - Privacy policy links to /privacy
// - Contact us links to /contact
// - about us (built in seattle)
// - email us: dev@698expat.com

// terms of service should be on the left
// 2 columns

// ----
import React from "react";

const Footer: React.FC = () => {
  return (
    <footer className="bg-primary text-white py-6">
      <div className="container mx-auto px-6">
        {/* Footer Title */}
        <h2 className="text-xl font-bold text-center mb-4">698 Expat</h2>

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
                Copyright 698 Expat
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
              dev@698expat.com
            </a>
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
