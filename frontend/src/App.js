import React, { useState } from 'react';
import AnalysisForm from './components/AnalysisForm';
import ResultDisplay from './components/ResultDisplay';
import './styles/App.css';

function App() {
    const [result, setResult] = useState(null);

    const handleAnalysisResult = (data) => {
        setResult(data);
    };

    return (
        <div className="container">
            <div className="App">
                <h1>YouTube Gender Analysis</h1>
                <AnalysisForm onAnalyze={handleAnalysisResult} />
                {result && <ResultDisplay result={result} />}
            </div>
        </div>
    );
}

export default App;