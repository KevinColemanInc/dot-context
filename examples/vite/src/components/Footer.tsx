import React from 'react';

const Footer = () => {
    return (
        <footer className="bg-green-50 p-6">
            <div className="flex justify-between">
                <div className="space-y-2">
                    <a href="/tos" className="text-blue-600">Terms of Service</a>
                    <a href="/privacy" className="text-blue-600">Privacy Policy</a>
                    <p className="text-black">Copyright 2024</p>
                </div>
                <div className="space-y-2 text-right">
                    <a href="mailto:kevin@sparkstart.io" className="text-blue-600">Contact Us</a>
                    <p className="text-black">About Us</p>
                    <a href="https://github.com/kevincolemaninc/dot-context" className="text-blue-600">GitHub</a>
                    <p className="text-black">Built in Redmond, WA</p>
                </div>
            </div>
        </footer>
    );
};

export default Footer;