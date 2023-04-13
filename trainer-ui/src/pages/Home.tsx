import { useState } from 'react'
import axios from 'axios'
import { useDispatch } from 'react-redux'
import { setLinks } from '../redux/wikiSlice'
import { Link } from 'react-router-dom'

function Home() {

    const [wikiSlug, setWikiSlug] = useState('Artificial_intelligence')
    const [text, setText] = useState('')
    const [wikiLinks, setWikiLinks] = useState([])
    const dispatch = useDispatch()

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
                dispatch(setLinks(res.data.links.map((link: any) => "https://en.wikipedia.org" + link)))
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
                    wikiLinks.length > 0 && <h3 style={{ marginBottom: 0 }}>Links</h3>
                }
                {
                    wikiLinks.map((link, index) => {
                        return (
                            <div key={index} style={{ display: 'flex', flexDirection: 'column', marginTop: 10 }}>
                                <span>{link}</span>
                            </div>
                        )
                    })
                }
                {
                    wikiLinks.length > 0 && (
                        <div>
                            <Link to={"/article/0"} style={{ marginTop: 15 }}>
                                <button style={{ marginTop: 10 }}>Start question answering generation process</button></Link>
                        </div>
                    )
                }

                <button style={{ marginTop: 20 }}>Clear store</button>
            </div>
        </div>
    )
}

export default Home