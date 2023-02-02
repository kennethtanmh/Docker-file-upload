import React, { useState } from "react";
import axios from "axios";

function FileUpload() {
  const [fileInput1, setFileInput1] = useState(null);
  const [fileInput2, setFileInput2] = useState(null);
  const [filenames, setFilenames] = useState([]);
  const [isIdentical, setIsIdentical] = useState(null);

  const handleFileChange1 = (event) => {
    setFileInput1(event.target.files);
  };
  
  const handleFileChange2 = (event) => {
    setFileInput2(event.target.files);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    for (let i = 0; i < fileInput1.length; i++) {
      formData.append("files1", fileInput1[i]);
    }
    
    for (let i = 0; i < fileInput2.length; i++) {
      formData.append("files2", fileInput2[i]);
    }

    try {
      const response = await axios.post('http://localhost:5000/api/upload', formData);
      setFilenames([...filenames, ...response.data.filenames]);
      const checksum1 = response.data.checksum1;
      const checksum2 = response.data.checksum2;
      setIsIdentical(checksum1 === checksum2);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <input type="file" multiple onChange={handleFileChange1} />
      <input type="file" multiple onChange={handleFileChange2} />
      <button onClick={handleUpload}>Upload</button>
      <ul>
        {filenames.map((filename, index) => (
          <li key={index}>{filename}</li>
        ))}
      </ul>
      {isIdentical === true && <div>The files are identical.</div>}
      {isIdentical === false && <div>The files are different.</div>}
    </div>
  );
}

export default FileUpload;

