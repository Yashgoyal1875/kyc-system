import React from 'react'

export default function ResultPage({ result, onReset }) {
  return (
    <div>
      <h2>Result</h2>
      <p><strong>Decision</strong>: {result?.decision?.status}</p>
      <p><strong>Score</strong>: {result?.decision?.score}</p>
      <p><strong>Reasons</strong>: {result?.decision?.reasons?.join(', ')}</p>
      <h4>Raw extract preview</h4>
      <pre>{JSON.stringify(result?.extracted, null, 2)}</pre>
      <h4>Face check</h4>
      <pre>{JSON.stringify(result?.face, null, 2)}</pre>
      <button onClick={onReset}>Reset</button>
    </div>
  )
}
