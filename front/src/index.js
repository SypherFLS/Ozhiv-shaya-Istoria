import React, { useState } from 'react';
import ReactPlayer from 'react-player';

function App() {
  const [text, setText] = useState('');
  const [videoUrl, setVideoUrl] = useState('');
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8080/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text })
      });

      const data = await response.json();
      const videoId = data.id;

      const resultResponse = await fetch(`http://localhost:8080/result/${videoId}`);
      const resultData = await resultResponse.json();
      setVideoUrl(resultData.videoUrl);
    } catch (error) {
      console.error('Ошибка при генерации видео:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Ожившая история</h1>
      <textarea
        rows="10"
        cols="50"
        placeholder="Введите текст письма..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <br />
      <button onClick={handleGenerate} disabled={loading}>
        {loading ? 'Генерация...' : 'Сгенерировать'}
      </button>
      <div style={{ marginTop: '20px' }}>
        {videoUrl && (
          <ReactPlayer url={videoUrl} controls width="100%" />
        )}
      </div>
    </div>
  );
}

export default App;
