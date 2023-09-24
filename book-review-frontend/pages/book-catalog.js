// pages/book-catalog.js
import React from 'react';
import BookCard from '../components/BookCard';

const BookCatalogPage = () => {
  // Replace with actual book data or API call
  const books = [
    // Add books for the catalog page
  ];

  return (
    <div>
      <h1>Book Catalog</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {books.map((book) => (
          <BookCard key={book.id} book={book} />
        ))}
      </div>
    </div>
  );
};

export default BookCatalogPage;
