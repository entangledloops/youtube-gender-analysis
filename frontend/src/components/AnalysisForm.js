import React, { useState } from 'react';
import '../styles/AnalysisForm.css';

const AnalysisForm = ({ onAnalyze }) => {
    const [url, setUrl] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            // Changed from '/api/analyze' to '/analyze' to match the backend endpoint
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url }),
            });

            if (!response.ok) {
                throw new Error('Failed to analyze the video');
            }

            const data = await response.json();
            onAnalyze(data.gender);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="analysis-form">
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Enter YouTube Video URL"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    required
                />
                <button type="submit" disabled={loading}>
                    {loading ? 'Analyzing...' : 'Analyze'}
                </button>
            </form>
            {error && <p className="error">{error}</p>}
        </div>
    );
};

export default AnalysisForm;