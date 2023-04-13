import { PayloadAction, createSlice } from "@reduxjs/toolkit"

interface QuestionAnswer {
    question: string
    answer: string
}
interface Link {
    link: string
    questionsAndAnswers: QuestionAnswer[]
}

interface InitialState {
    articles: Link[]
}

const initialState: InitialState = {
    articles: [],
}

const slice = createSlice({
    name: 'wiki',
    initialState: initialState,
    reducers: {
        setLinks: (state, { payload }: PayloadAction<string[]>) => {
            payload.map((link) => {
                state.articles.push({ link: link, questionsAndAnswers: [] })
            })
        },
        setQuestionsAnswers: (state, { payload }: PayloadAction<{ articleId: number, questionsAnswers: QuestionAnswer[] }>) => {
            state.articles[payload.articleId].questionsAndAnswers = payload.questionsAnswers
        },

        clearStore: (state) => {
            state.articles = []
        }
    }
})

export const { setLinks, setQuestionsAnswers, clearStore } = slice.actions
export default slice.reducer
