import { PayloadAction, createSlice } from "@reduxjs/toolkit"

interface Link {
    link: string
    questionsAnswersGenerated: boolean
}

interface InitialState {
    links: Link[]
}

const initialState: InitialState = {
    links: [],
}

const slice = createSlice({
    name: 'wiki',
    initialState: initialState,
    reducers: {
        setLinks: (state, { payload }: PayloadAction<string[]>) => {
            payload.map((link) => {
                state.links.push({ link: link, questionsAnswersGenerated: false })
            })
        },
        setQuestionsAnswersGenerated: (state, { payload }: PayloadAction<number>) => {
            state.links[payload].questionsAnswersGenerated = true
        }
    }
})

export const { setLinks } = slice.actions
export default slice.reducer
