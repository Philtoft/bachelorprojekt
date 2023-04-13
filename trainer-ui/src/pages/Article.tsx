import React, { useEffect, useState } from 'react'
import { useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'
import styles from './Article.module.css'
import { faker } from '@faker-js/faker';
import { useDispatch } from 'react-redux';
import { setQuestionsAnswers } from '../redux/wikiSlice';

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

    const dispatch = useDispatch()

    // 1. Get articleId from params
    let { articleId } = useParams()

    if (articleId == undefined) {
        return <div>ArticleId is not defined</div>
    }

    let id = parseInt(articleId)

    if (isNaN(id)) {
        return <div>ArticleId is not a number</div>
    }

    const { link, questionsAndAnswers } = useSelector((state: any) => state.wiki.articles[id])

    function generateQuestionsAnswers() {
        let questionsAndAnswers: QuestionAnswer[] = []
        for (let i = 0; i < 5; i++) {
            questionsAndAnswers.push({
                question: faker.lorem.sentence(),
                answer: faker.lorem.paragraph()
            })
        }
        return questionsAndAnswers
    }

    return (
        <div style={{ width: '100%' }}>
            <div className={styles.column_wrapper}>
                <div className={styles.context}>
                    <p><b>Link</b>: {link}</p>
                    <h2 style={{ marginTop: 0, marginBottom: 0 }}>Article</h2>
                    <p>{link}</p>

                    {
                        questionsAndAnswers.length == 0 && (
                            <button onClick={() => dispatch(setQuestionsAnswers({
                                articleId: id,
                                questionsAnswers: generateQuestionsAnswers()
                            }))}>Generate Questions & Answers</button>
                        )
                    }
                </div>
                <div className={styles.question_answer_wrapper}>
                    <h2 style={{ marginTop: 0 }}>Questions and answers</h2>
                    {questionsAndAnswers.map((qa: QuestionAnswer, index: number) => (
                        <QAComponent key={index} index={index} qa={qa} />
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Article
