import React, { useState, FormEvent, ChangeEvent } from 'react';
import './App.css';

interface EmotionResult {
  emotion: string;
  confidence: number;
}

const App: React.FC = () => {
  const [reflection, setReflection] = useState<string>('');
  const [result, setResult] = useState<EmotionResult | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const response = await fetch('http://localhost:5000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: reflection }),
      });
      if (!response.ok) {
        throw new Error('API error');
      }
      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError('Failed to analyze emotion.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>Emotion Reflection Analyzer</h1>
      <form className="reflection-form" onSubmit={handleSubmit}>
        <textarea
          value={reflection}
          onChange={(e: ChangeEvent<HTMLTextAreaElement>) => setReflection(e.target.value)}
          placeholder="Enter your reflection..."
          rows={4}
          required
        />
        <button type="submit" disabled={loading || !reflection.trim()}>
          {loading ? 'Analyzing...' : 'Submit'}
        </button>
      </form>
      {error && <div className="error-message">{error}</div>}
      {result && (
        <div className="result-card">
          <h2>Emotion Analysis</h2>
          <p><strong>Emotion:</strong> {result.emotion}</p>
          <p><strong>Confidence:</strong> {(result.confidence * 100).toFixed(1)}%</p>
        </div>
      )}
    </div>
  );
};

export default App;
