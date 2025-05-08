import React, { useState } from 'react';
import '../styles/AnalysisForm.css';

const AnalysisForm = ({ onAnalyze }) => {
    const [url, setUrl] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    // Get the backend URL based on the environment
    const getBackendUrl = () => {
        // For production in render.com
        if (process.env.REACT_APP_BACKEND_URL) {
            return process.env.REACT_APP_BACKEND_URL;
        }
        // For local development with proxy configured in package.json
        return '';
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            const backendUrl = getBackendUrl();
            console.log(`Making request to: ${backendUrl}/analyze`);
            
            const response = await fetch(`${backendUrl}/analyze`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url }),
            });

            const data = await response.json();
            
            if (!response.ok) {
                const errorMessage = data.error || `Failed to analyze the video: ${response.status} ${response.statusText}`;
                throw new Error(errorMessage);
            }

            onAnalyze(data.gender);
        } catch (err) {
            console.error("Error during analysis:", err);
            setError(err.message || "An unexpected error occurred");
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