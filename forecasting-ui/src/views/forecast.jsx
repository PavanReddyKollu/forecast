import React, { useState } from "react";

export default function ForecastUI() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState([]);

  const handleUpload = (e) => {
    setFile(e.target.files[0]);
    console.log(e)
  };

  const handleSubmit = () => {
    // Dummy data for table preview after submission
    const sampleData = [
      { column1: "Jan", column2: "1000", column3: "1200", column4: "200" },
      { column1: "Feb", column2: "1100", column3: "1300", column4: "200" },
    ];
    setData(sampleData);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      {/* Header centered at top */}
      <div className="w-full flex justify-center mb-10" style={{position:'absolute',top:'2px'}}>
        <h1 className="text-4xl font-bold text-center">Forecast UI</h1>
      </div>

      {/* Upload and Submit Section */}
      <div className="flex flex-col items-center gap-4">
        <input
          type="file"
          onChange={handleUpload}
          className="file-input file-input-bordered file-input-primary"
        />

        {file && (
          <button
            onClick={handleSubmit}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
          >
            Submit
          </button>
        )}
      </div>

      {/* Table Section */}
      {data.length > 0 && (
        <div className="mt-10 w-full flex justify-center">
          <div className="w-full max-w-4xl">
            <table className="w-full bg-white shadow-md rounded">
              <thead className="bg-blue-500 text-white">
                <tr>
                  <th className="p-3">Column 1</th>
                  <th className="p-3">Column 2</th>
                  <th className="p-3">Column 3</th>
                  <th className="p-3">Column 4</th>
                </tr>
              </thead>
              <tbody>
                {data.map((row, i) => (
                  <tr key={i} className="text-center border-t">
                    <td className="p-3">{row.column1}</td>
                    <td className="p-3">{row.column2}</td>
                    <td className="p-3">{row.column3}</td>
                    <td className="p-3">{row.column4}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
}
