// pages/index.js
import React from 'react';
import BookCard from '../components/BookCard';

const HomePage = () => {
  // Replace with actual book data or API call
  const books = [
    {
      id: 1,
      title: 'Book Title 1',
      author: 'Author Name 1',
      coverImage: '/images/book1.jpg',
      // Add more book details here
    },
    {
      id: 2,
      title: 'Book Title 2',
      author: 'Author Name 2',
      coverImage: '/images/book2.jpg',
      // Add more book details here
    },
    // Add more books
  ];

  return (
    <div>
      <h1>Welcome to the Book Review Website</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {books.map((book) => (
          <BookCard key={book.id} book={book} />
        ))}
      </div>
    </div>
  );
};

export default HomePage;
