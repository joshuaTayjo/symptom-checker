const appEndpoint='/api_v1'

const vm = new Vue({
    el: '#vm',
    delimiters: ['[[',']]'],
    data:{
        greeting: 'Hello from vue!',
        flaskGreeting:''
    },

    created: async function(){
        const gResponse=await(fetch(appEndpoint+'greeting'))
        const gObject=await gResponse.json()
        this.flaskGreeting=gObject.greeting
    }
})