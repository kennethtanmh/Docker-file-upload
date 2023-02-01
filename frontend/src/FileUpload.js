import React, { useState } from "react";
import axios from "axios";

function FileUpload() {
  const [fileInput, setFileInput] = useState(null);
  const [filenames, setFilenames] = useState([]);

  const handleFileChange = (event) => {
    setFileInput(event.target.files);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    for (let i = 0; i < fileInput.length; i++) {
      formData.append("files", fileInput[i]);
    }

    try {
      const response = await axios.post('http://localhost:5000/api/upload', formData);
      setFilenames([...filenames, ...response.data.filenames]);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <input type="file" multiple onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <ul>
        {filenames.map((filename, index) => (
          <li key={index}>{filename}</li>
        ))}
      </ul>
    </div>
  );
}

export default FileUpload;
