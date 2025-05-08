import React from 'react';
import '../styles/ResultDisplay.css';

const ResultDisplay = ({ result }) => {
    return (
        <div className="result-display">
            {result ? (
                <h2>Gender: {result}</h2>
            ) : (
                <h2>No result available. Please analyze a video.</h2>
            )}
        </div>
    );
};

export default ResultDisplay;