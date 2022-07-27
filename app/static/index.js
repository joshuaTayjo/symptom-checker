const {createApp} = Vue

const vm = createApp({
    data() {
        return {
            greeting: 'Hello from vue'
        }
    },
})
vm.config.compilerOptions = {delimiters: ['[[', ']]']}
console.log(vm)


vm.mount('#vm')