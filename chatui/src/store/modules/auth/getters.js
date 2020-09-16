export const authUser = (state) => {
    return state.authUser||{}
}

export const isLoggedIn = (state) => {
    return state.authUser!==null
}
