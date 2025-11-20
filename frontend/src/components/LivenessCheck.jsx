import React, { useRef, useEffect } from 'react'

export default function LivenessCheck({ onCapture }) {
  const videoRef = useRef()
  const canvasRef = useRef()

  useEffect(() => {
    let mounted = true
    async function start() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' } })
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

  function doLiveness() {
    const v = videoRef.current
    const c = canvasRef.current
    c.width = v.videoWidth || 640
    c.height = v.videoHeight || 480
    const ctx = c.getContext('2d')
    ctx.drawImage(v, 0, 0, c.width, c.height)
    c.toBlob(blob => {
      onCapture(blob)
      alert('Selfie captured for liveness demo')
    }, 'image/jpeg', 0.9)
  }

  return (
    <div className="liveness">
      <h3>Liveness test</h3>
      <video ref={videoRef} playsInline muted />
      <canvas ref={canvasRef} style={{display:'none'}} />
      <div>
        <button onClick={doLiveness}>Complete liveness</button>
      </div>
    </div>
  )
}
