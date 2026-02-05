import { useEffect, useState } from "react";
import api from "../api/axios";

export default function AttachmentList({ ticketId }) {
  const [files, setFiles] = useState([]);

  const load = () => {
    api.get(`/attachments/ticket/${ticketId}`).then(res => setFiles(res.data));
  };

  useEffect(load, [ticketId]);

  return (
    <div className="mt-2">
      {files.map(f => (
        <a
          key={f.id}
          href={`http://127.0.0.1:8000/attachments/${f.id}/download`}
          className="block text-blue-600 underline"
        >
          {f.filename}
        </a>
      ))}
    </div>
  );
}

