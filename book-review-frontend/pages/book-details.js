// pages/book-details.js
import React from 'react';
import { useRouter } from 'next/router';

const BookDetailsPage = () => {
  const router = useRouter();
  const { bookId } = router.query; // Access the bookId from the URL

  // Replace with actual book details based on the bookId
  const book = {
    id: bookId,
    title: 'Book Title',
    author: 'Author Name',
    coverImage: '/images/book1.jpg',
    // Add more book details here
  };

  return (
    <div>
      <h1>Book Details</h1>
      <div>
        <img src={book.coverImage} alt={`${book.title} Cover`} />
        <h2>{book.title}</h2>
        <p>Author: {book.author}</p>
        {/* Display more book details here */}
      </div>
    </div>
  );
};

export default BookDetailsPage;
