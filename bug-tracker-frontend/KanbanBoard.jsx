import { useEffect, useState } from "react";
import api from "../api/axios";

const columns = ["TODO", "IN_PROGRESS", "DONE"];

export default function KanbanBoard() {
  const [tickets, setTickets] = useState([]);

  useEffect(() => {
    api.get("/tickets").then(res => setTickets(res.data));

    const ws = new WebSocket("ws://127.0.0.1:8000/ws");

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === "TICKET_STATUS_UPDATED") {
        setTickets(prev =>
          prev.map(t =>
            t.id === data.ticket_id
              ? { ...t, status: data.status }
              : t
          )
        );
      }
    };

    return () => ws.close();
  }, []);

  const updateStatus = async (id, status) => {
    await api.patch(`/tickets/${id}/status?status=${status}`);
  };

  return (
    <div className="grid grid-cols-3 gap-4">
      {columns.map(col => (
        <div key={col} className="border p-3">
          <h3 className="font-bold mb-2">{col}</h3>
          {tickets.filter(t => t.status === col).map(ticket => (
            <div
              key={ticket.id}
              className="bg-gray-100 p-2 mb-2"
              onClick={() =>
                updateStatus(
                  ticket.id,
                  col === "TODO"
                    ? "IN_PROGRESS"
                    : col === "IN_PROGRESS"
                    ? "DONE"
                    : "TODO"
                )
              }
            >
              <h4 className="font-semibold">{ticket.title}</h4>
              <p className="text-sm">{ticket.description}</p>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}
