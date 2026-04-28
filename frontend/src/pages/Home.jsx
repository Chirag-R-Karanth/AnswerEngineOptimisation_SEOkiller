import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="min-h-screen bg-white flex flex-col items-center justify-center">
      <header className="text-center">
        <h1 className="text-5xl font-bold text-gray-800 mb-4">Welcome to Our Platform</h1>
        <p className="text-xl text-gray-600 mb-8">Discover a new way to manage your tasks efficiently.</p>
        <Link
          to="/signup"
          className="px-8 py-3 bg-blue-600 text-white font-semibold rounded-full hover:bg-blue-700 transition duration-300"
        >
          Get Started
        </Link>
      </header>
      <main className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl px-4">
        <div className="p-6 border border-gray-100 rounded-2xl shadow-sm hover:shadow-md transition">
          <h3 className="text-xl font-semibold text-gray-700 mb-2">Fast</h3>
          <p className="text-gray-500">Optimized for speed and efficiency.</p>
        </div>
        <div className="p-6 border border-gray-100 rounded-2xl shadow-sm hover:shadow-md transition">
          <h3 className="text-xl font-semibold text-gray-700 mb-2">Secure</h3>
          <p className="text-gray-500">Your data is safe with us.</p>
        </div>
        <div className="p-6 border border-gray-100 rounded-2xl shadow-sm hover:shadow-md transition">
          <h3 className="text-xl font-semibold text-gray-700 mb-2">Pleasant</h3>
          <p className="text-gray-500">Enjoy a clean and light user interface.</p>
        </div>
      </main>
    </div>
  );
};

export default Home;
