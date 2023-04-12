import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {

  const [url, setUrl] = useState('https://en.wikipedia.org/wiki/Artificial_intelligence')

  function handleSubmit() {
    console.log('url', url)
  }

  return (
    <div className="App">
      <div style={{ flexDirection: 'column', display: 'flex', width: 500 }}>
        <h1>Scraper URL</h1>
        {/* input URL */}
        <input type="text" style={{ padding: 15 }} onChange={(e) => setUrl(e.target.value)} value={url} />
        {/* button */}
        <button style={{ marginTop: '10px' }} onClick={handleSubmit}>Submit</button>
      </div>
    </div>
  )
}

export default App
