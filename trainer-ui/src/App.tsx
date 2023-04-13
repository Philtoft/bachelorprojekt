import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import axios from 'axios'
import './App.css'

function App() {

  const [wikiSlug, setWikiSlug] = useState('Artificial_intelligence')
  const [text, setText] = useState('')
  const [wikiLinks, setWikiLinks] = useState([])

  function handleSubmit() {
    axios.get('http://127.0.0.1:5000/',
      {
        headers: { "Access-Control-Allow-Origin": "*" },
        params: { slug: wikiSlug }
      }
    )
      .then((res) => {
        console.log('res', res)
        setWikiLinks(res.data.links.map((link: any) => "https://en.wikipedia.org" + link))
      })
      .catch((err) => {
        console.log('err', err)
      })
  }

  return (
    <div className="App">
      <div style={{ flexDirection: 'column', display: 'flex', width: 500 }}>
        <h1>Scraper SLUG</h1>
        {/* input SLUG */}
        <input type="text" style={{ padding: 15 }} onChange={(e) => setWikiSlug(e.target.value)} value={wikiSlug} />
        {/* button */}
        <button style={{ marginTop: '10px' }} onClick={handleSubmit}>Submit</button>
        {
          wikiLinks.map((link, index) => {
            return (
              <div key={index} style={{ display: 'flex', flexDirection: 'column', marginTop: 10 }}>
                <span>{link}</span>
              </div>
            )
          })
        }
      </div>
    </div>
  )
}

export default App
