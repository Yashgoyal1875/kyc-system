import React, { useState } from 'react'
import CaptureCamera from './components/CaptureCamera'
import LivenessCheck from './components/LivenessCheck'
import ResultPage from './components/ResultPage'

const BACKEND = (import.meta.env.VITE_BACKEND_URL) ? import.meta.env.VITE_BACKEND_URL : 'http://localhost:8000'

export default function App() {
  const [idBlob, setIdBlob] = useState(null)
  const [selfieBlob, setSelfieBlob] = useState(null)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

  async function submitToBackend() {
    if (!idBlob || !selfieBlob) return alert('Please capture both id and selfie')
    setLoading(true)
    const fd = new FormData()
    fd.append('id_file', idBlob, 'id.jpg')
    fd.append('selfie_file', selfieBlob, 'selfie.jpg')

    try {
      const res = await fetch(`${BACKEND}/api/verify`, {
        method: 'POST',
        body: fd
      })
      const data = await res.json()
      setResult(data)
    } catch (e) {
      alert('Failed to reach backend ' + e.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <h1>Seamless Trust Engine demo</h1>
      {!result && (
        <>
          <CaptureCamera label="Capture ID document" onCapture={setIdBlob} accept="environment" />
          <LivenessCheck onCapture={setSelfieBlob} />
          <div style={{marginTop:20}}>
            <button onClick={submitToBackend} disabled={loading}>Submit</button>
          </div>
        </>
      )}
      {loading && <p>Processing...</p>}
      {result && <ResultPage result={result} onReset={() => { setResult(null); setIdBlob(null); setSelfieBlob(null);} } />}
    </div>
  )
}
