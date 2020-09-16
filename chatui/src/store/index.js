import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);


const modulesCustomFiles = require.context('./modules', true, /(index\.js$)$/);

const modules = modulesCustomFiles.keys().reduce((modules, modulePath) => {
    const moduleNameFull = modulePath.replace(/^\.\/(.*)\.\w+$/, '$1');
    const moduleName = moduleNameFull.match(/(.+)\//, '$1');
    const value = modulesCustomFiles(modulePath);

    modules[moduleName[1]] = value.default;
    return modules;
}, {});
console.log(modules)

const Store = new Vuex.Store({
    modules: modules
});

export default function () {
    return Store;
}

export { Store }
