// src/components/Footer.tsx

import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-[#34C759] text-white p-4">
      <div className="container mx-auto p-4 flex flex-wrap justify-between">
        <div className="w-full lg:w-1/2 xl:w-1/2 md:w-1/2 mb-6 lg:mb-0">
          <h6 className="uppercase text-gray-200 font-bold mb-4">
            Terms of Service
          </h6>
          <ul>
            <li className="mt-2">
              <a href="/tos" className="text-gray-200 hover:text-white">
                Terms of Service
              </a>
            </li>
            <li className="mt-2">
              <a href="/privacy" className="text-gray-200 hover:text-white">
                Privacy Policy
              </a>
            </li>
          </ul>
        </div>
        <div className="w-full lg:w-1/2 xl:w-1/2 md:w-1/2 mb-6 lg:mb-0 text-right">
          <h6 className="uppercase text-gray-200 font-bold mb-4">CheckMate</h6>
          <ul>
            <li className="mt-2">&copy; CheckMate</li>
            <li className="mt-2">Built in Redmond, WA</li>
            <li className="mt-2">
              <a href="/contact" className="text-gray-200 hover:text-white">
                Contact Us
              </a>
            </li>
          </ul>
        </div>
      </div>
    </footer>
  );
};

export default Footer;