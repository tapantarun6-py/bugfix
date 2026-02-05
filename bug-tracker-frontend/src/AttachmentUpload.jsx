import api from "../api/axios";
import { useState } from "react";

export default function AttachmentUpload({ ticketId, onUploaded }) {
  const [file, setFile] = useState(null);

  const upload = async () => {
    if (!file) return;
    const form = new FormData();
    form.append("file", file);

    await api.post(`/attachments/ticket/${ticketId}`, form, {
      headers: { "Content-Type": "multipart/form-data" }
    });

    setFile(null);
    onUploaded && onUploaded();
  };

  return (
    <div className="mt-2">
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={upload} className="ml-2 px-3 py-1 bg-black text-white">
        Upload
      </button>
    </div>
  );
}
