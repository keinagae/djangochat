export function me ({commit}) {
    return axios.get('auth/users/me').then((response) => {
        commit('setAuthUser', response.data)
        return response.data;
    }).finally(() => {

    })
}
