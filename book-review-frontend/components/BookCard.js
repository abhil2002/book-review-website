// components/BookCard.js
import React from 'react';

const BookCard = ({ book }) => {
  return (
    <div className="border p-4 rounded shadow-md">
      <img src={book.coverImage} alt={`${book.title} Cover`} className="w-32 h-32" />
      <h2 className="text-lg font-semibold">{book.title}</h2>
      <p className="text-gray-600">Author: {book.author}</p>
      {/* Add more book details here */}
    </div>
  );
};

export default BookCard;
