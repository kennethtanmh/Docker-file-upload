import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = () => {
  const [files, setFiles] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setFiles(e.target.files);
  };

  const handleUpload = async () => {
    setUploading(true);
    setError(null);
    const formData = new FormData();
    for (const file of files) {
      formData.append('files', file);
    }

    try {
      await axios.post('http://localhost:5000/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
    } catch (err) {
      setError(err.message);
      console.error(err);
    } finally {
      setUploading(false);
      setFiles([]);
    }
  };

  return (
    <div>
      <input type="file" multiple onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={uploading || !files.length}>
        {uploading ? 'Uploading...' : 'Upload'}
      </button>
      {error && <div>{error}</div>}
    </div>
  );
};

export default FileUpload;