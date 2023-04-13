import React, { useEffect, useState } from 'react'
import { useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'
import styles from './Article.module.css'
import { faker } from '@faker-js/faker';

interface QuestionAnswer {
    question: string
    answer: string
}

const QAComponent = ({ index, qa }: { index: number, qa: QuestionAnswer }): JSX.Element => {

    const [question, setQuestion] = useState(qa.question)
    const [answer, setAnswer] = useState(qa.answer)

    return (
        <div key={index} className={styles.question_answer}>
            <input className={styles.question} value={question} onChange={question => setQuestion(question.target.value)} />
            <input className={styles.answer} value={answer} onChange={answer => setAnswer(answer.target.value)} />
        </div>
    );
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


    useEffect(() => {
        for (let i = 0; i < 10; i++) {
            let question = faker.lorem.sentence(Math.floor(Math.random() * (3 - 1 + 1)) + 1)
            let answer = faker.lorem.sentence(Math.floor(Math.random() * (3 - 1 + 1)) + 1)
            setQuestionsAnswers(prev => [...prev, { question: `${question}`, answer: `${answer}` }])
        }
    }, [])

    return (
        <div style={{ width: '100%' }}>
            <div className={styles.column_wrapper}>
                <div className={styles.context}>
                    <p><b>Link</b>: {link}</p>
                    <div>ArticleId: {articleId}</div>
                </div>
                <div className={styles.question_answer_wrapper}>
                    {questionsAnswers.map((qa, index) => (
                        <QAComponent index={index} qa={qa} />
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Article
