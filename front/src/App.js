import React, { useState } from 'react';
import ReactPlayer from 'react-player';

function App() {
  const [text, setText] = useState('');
  const [videoUrl, setVideoUrl] = useState('');
  const [loading, setLoading] = useState(false);

  // пока заглушка
  const handleGenerate = async () => {
    setLoading(true);
    try {
      
      await new Promise((resolve) => setTimeout(resolve, 2000));
  
      
      setVideoUrl('https://www.w3schools.com/html/mov_bbb.mp4');
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
