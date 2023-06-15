import React from 'react';

const Admin = () => {
  const handleUpload = async (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

    try {
      await fetch('/upload-csv', {
        method: 'POST',
        body: formData,
      });
      alert('CSV uploaded successfully!');
    } catch (error) {
      console.error(error);
      alert('Error uploading CSV.');
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-4xl font-bold mb-4">Admin Page</h1>
      <input
        type="file"
        accept=".csv"
        onChange={handleUpload}
        className="border p-2 rounded-md"
      />
    </div>
  );
};

export default Admin;
