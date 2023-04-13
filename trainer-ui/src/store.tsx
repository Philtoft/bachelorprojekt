import { configureStore } from '@reduxjs/toolkit'
import wiki from './redux/wikiSlice'
import { persistStore, persistReducer } from 'redux-persist'
import storage from 'redux-persist/lib/storage' // defaults to localStorage for web

export const store = configureStore({
    reducer: {
        wiki: wiki,
    },
})

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch

// TODO: Add persistor
// import { combineReducers, configureStore } from '@reduxjs/toolkit'
// import wiki from './redux/wikiSlice'
// import { persistStore, persistReducer } from 'redux-persist'
// import storage from 'redux-persist/lib/storage' // defaults to localStorage for web
// import { useDispatch } from 'react-redux'

// const rootReducer = combineReducers({
//     wiki: wiki,
// })

// const persistConfig = {
//     key: 'root',
//     storage,
// }

// const persistedReducer = persistReducer(persistConfig, rootReducer)

// export const store = configureStore({
//     reducer: persistedReducer,
// })

// export const persistor = persistStore(store)

// export type RootState = ReturnType<typeof rootReducer>;

// export type AppDispatch = typeof store.dispatch;
// export const useAppDispatch: () => AppDispatch = useDispatch;