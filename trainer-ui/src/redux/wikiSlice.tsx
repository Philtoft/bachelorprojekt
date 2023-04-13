import { PayloadAction, createSlice } from "@reduxjs/toolkit"

interface Link {
    link: string
    questionsGenerated: boolean
}

interface initialState {
    links: Link[]
}

const initialState: initialState = {
    links: [],
}

const slice = createSlice({
    name: 'wiki',
    initialState,
    reducers: {
        setLinks: (state, { payload }: PayloadAction<Link[]>) => {
            state.links = payload
        }
    }
})

export const { setLinks } = slice.actions
export default slice.reducer
