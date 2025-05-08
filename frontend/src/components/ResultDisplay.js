import React from 'react';
import '../styles/ResultDisplay.css';

const ResultDisplay = ({ result }) => {
    // Check if result has probability data
    const hasProbabilities = result && 
                             typeof result === 'object' && 
                             result.probabilities && 
                             (result.probabilities.male !== undefined || 
                              result.probabilities.female !== undefined);
    
    return (
        <div className="result-display">
            {result ? (
                <div>
                    <h2>Gender: {hasProbabilities ? result.gender : result}</h2>
                    
                    {hasProbabilities && (
                        <div className="probabilities">
                            <p><strong>Confidence:</strong></p>
                            <ul>
                                <li>Male: {(result.probabilities.male * 100).toFixed(2)}%</li>
                                <li>Female: {(result.probabilities.female * 100).toFixed(2)}%</li>
                            </ul>
                        </div>
                    )}
                </div>
            ) : (
                <h2>No result available. Please analyze a video.</h2>
            )}
        </div>
    );
};

export default ResultDisplay;