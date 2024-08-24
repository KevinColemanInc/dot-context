// components/Footer.tsx
import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-gray-100 py-8 text-gray-600">
      <div className="container mx-auto px-4">
        <div className="flex flex-wrap justify-between">
          <div className="w-full md:w-1/2 xl:w-1/2 mb-4 md:mb-0">
            <h5 className="uppercase text-sm font-bold mb-2 text-[#3728af]">CheckMate</h5>
            <ul>
              <li className="mb-2">
                <a
                  href="/tos"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-gray-600 hover:text-[#3728af]"
                >
                  Terms of Service
                </a>
              </li>
            </ul>
          </div>
          <div className="w-full md:w-1/2 xl:w-1/2 mb-4 md:mb-0">
            <h5 className="uppercase text-sm font-bold mb-2">&copy; CheckMate</h5>
            <ul>
              <li className="mb-2">
                <a
                  href="/privacy"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-gray-600 hover:text-[#3728af]"
                >
                  Privacy Policy
                </a>
              </li>
              <li className="mb-2">
                <a
                  href="/contact"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-gray-600 hover:text-[#3728af]"
                >
                  Contact Us
                </a>
              </li>
              <li className="mb-2">
                Built in Seattle with love
              </li>
              <li className="mb-2">
                <a
                  href="mailto:dev@698expat.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-gray-600 hover:text-[#3728af]"
                >
                  dev@698expat.com
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;


