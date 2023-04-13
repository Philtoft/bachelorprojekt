import { configureStore } from '@reduxjs/toolkit'
import wiki from './redux/wikiSlice'
import { combineReducers } from 'redux';
import { loadState, saveState } from './utils/localStorage';

const preloadedState = loadState()

const reducer = combineReducers({
    wiki: wiki
})

export const store = configureStore({
    reducer: reducer,
    preloadedState: preloadedState
})

store.subscribe(() => {
    saveState(store.getState())
})

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch