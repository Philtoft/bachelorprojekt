import React, { useEffect, useState } from 'react'
import { useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'

interface QuestionAnswer {
    question: string
    answer: string
}

function Article() {

    let { articleId } = useParams()

    /**
     * 1. Get articleId from params
     * 2. Get article from API
     * 3. Get questions & answers from API
     * 
     */

    if (!articleId) {
        return <div>ArticleId is not defined</div>
    }

    const [article, setArticle] = useState(null)
    const [questionsAnswers, setQuestionsAnswers] = useState<QuestionAnswer[]>([])
    const link = useSelector((state: any) => state.wiki.links[articleId])


    useEffect(() => { }, [])

    return (
        <div style={{ width: '100%' }}>
            <div style={{ backgroundColor: '#eeeeee', display: 'flex' }}>
                <div className="context">
                    <div>ArticleWithQuestionAnswers</div>
                    <div>Link: {link}</div>
                    <div>ArticleId: {articleId}</div>
                </div>
                <div></div>
            </div>
        </div>
    )
}

export default Article