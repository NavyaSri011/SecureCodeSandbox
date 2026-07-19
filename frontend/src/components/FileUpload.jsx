import "./FileUpload.css";

function FileUpload({ setCode }) {

  const handleFile = (e) => {
    const file = e.target.files[0];

    if (!file) return;

    const reader = new FileReader();

    reader.onload = () => {
      setCode(reader.result);
    };

    reader.readAsText(file);
  };


  return (
    <div className="file-upload">

      <label>
        📂 Upload Code File
      </label>

      <input
        type="file"
        accept=".py,.c,.cpp,.java"
        onChange={handleFile}
      />

      <small>
        Supported files: Python (.py), C (.c), C++ (.cpp), Java (.java)
      </small>

    </div>
  );
}

export default FileUpload;