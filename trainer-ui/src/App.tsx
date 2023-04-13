import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import axios from 'axios'
import './App.css'

function App() {

  const [slug, setSlug] = useState('Artificial_intelligence')
  const [text, setText] = useState('')

  function handleSubmit() {
    axios.get('http://127.0.0.1:5000/',
      {
        headers: { "Access-Control-Allow-Origin": "*" },
        params: { url: slug }
      }
    )
      .then((res) => {
        console.log('res', res)
        setText(res.data)
      })
      .catch((err) => {
        console.log('err', err)
      })
  }

  return (
    <div className="App">
      <div style={{ flexDirection: 'column', display: 'flex', width: 500 }}>
        <h1>Scraper SLUG</h1>
        {/* input URL */}
        <input type="text" style={{ padding: 15 }} onChange={(e) => setSlug(e.target.value)} value={slug} />
        {/* button */}
        <button style={{ marginTop: '10px' }} onClick={handleSubmit}>Submit</button>
        <p>{JSON.stringify(text)}</p>
      </div>
    </div>
  )
}

export default App
