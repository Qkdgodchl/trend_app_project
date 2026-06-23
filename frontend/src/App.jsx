// frontend/src/App.jsx
import { useState } from "react";

function App() {
  const [title, setTitle] = useState("");
  const [category, setCategory] = useState("IT");
  const [rank, setRank] = useState(1);
  const [message, setMessage] = useState("");

  // 🔥 [핵심] 버튼을 누르면 우리 FastAPI 백엔드 서버로 데이터를 쏴주는 함수!
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const backendUrl = `http://127.0.0.1:8000/trends/db?title=${encodeURIComponent(title)}&category=${category}&rank=${rank}`;
    
    try {
      const response = await fetch(backendUrl, { method: "POST" });
      const data = await response.json();

      if (response.ok) {
        setMessage(`🟢 DB 저장 성공! (등록된 ID: ${data.data.id})`);
        setTitle(""); // 입력창 비우기
      } else {
        setMessage("🔴 서버 에러 발생!");
      }
    } catch (error) {
      setMessage("🔴 FastAPI 서버가 꺼져있는지 확인하세요!");
    }
  };

  // 눈에 보이는 진짜 HTML 화면 구조
  return (
    <div style={{ padding: "40px", fontFamily: "sans-serif", maxWidth: "500px", margin: "0 auto" }}>
      <h2>📈 실시간 시장 트렌드 (React 풀스택)</h2>
      <p style={{ color: "#666" }}>진짜 대중적인 리액트 화면과 FastAPI + PostgreSQL 연동 테스트</p>
      <hr />
      
      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "15px", marginTop: "20px" }}>
        <div>
          <label style={{ display: "block", marginBottom: "5px" }}>트렌드 키워드:</label>
          <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} style={{ width: "100%", padding: "8px" }} placeholder="예: 리액트 x 백엔드 대유행" required />
        </div>

        <div>
          <label style={{ display: "block", marginBottom: "5px" }}>카테고리:</label>
          <select value={category} onChange={(e) => setCategory(e.target.value)} style={{ width: "100%", padding: "8px" }}>
            <option value="IT">IT</option>
            <option value="주식">주식</option>
            <option value="크립토">크립토</option>
          </select>
        </div>

        <div>
          <label style={{ display: "block", marginBottom: "5px" }}>순위:</label>
          <input type="number" value={rank} onChange={(e) => setRank(e.target.value)} style={{ width: "100%", padding: "8px" }} min="1" />
        </div>

        <button type="submit" style={{ padding: "10px", background: "#007bff", color: "#fff", border: "none", cursor: "pointer" }}>
          서버에 데이터 전송 및 DB 저장
        </button>
      </form>

      {message && <div style={{ marginTop: "20px", padding: "10px", background: "#eee", borderRadius: "5px", fontWeight: "bold" }}>{message}</div>}
    </div>
  );
}

export default App;