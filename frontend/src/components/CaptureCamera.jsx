import React, { useRef, useEffect } from 'react'

export default function CaptureCamera({ label, onCapture, accept }) {
  const videoRef = useRef()
  const canvasRef = useRef()

  useEffect(() => {
    let mounted = true
    async function start() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: accept || 'user' } })
        if (!mounted) {
          stream.getTracks().forEach(t => t.stop())
          return
        }
        videoRef.current.srcObject = stream
        await videoRef.current.play()
      } catch (e) {
        console.error(e)
        alert('Camera access denied: ' + e.message)
      }
    }
    start()
    return () => {
      mounted = false
      const s = videoRef.current?.srcObject
      if (s) s.getTracks().forEach(t => t.stop())
    }
  }, [])

  function handleCapture() {
    const v = videoRef.current
    const c = canvasRef.current
    if (!v || !c) return
    c.width = v.videoWidth || 640
    c.height = v.videoHeight || 480
    const ctx = c.getContext('2d')
    ctx.drawImage(v, 0, 0, c.width, c.height)
    c.toBlob(blob => {
      onCapture(blob)
      alert(label + ' captured')
    }, 'image/jpeg', 0.9)
  }

  return (
    <div className="capture">
      <h3>{label}</h3>
      <video ref={videoRef} playsInline muted />
      <canvas ref={canvasRef} style={{display:'none'}} />
      <div>
        <button onClick={handleCapture}>Capture</button>
      </div>
    </div>
  )
}
