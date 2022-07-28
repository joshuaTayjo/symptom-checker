const {createApp} = Vue

const vm = createApp({
    data() {
        return {
            greeting: 'Hello from vue',
            // symptomsByLocation,
            clickedLocations: [],
            renderSublocations: [],
            renderSymptoms: []
        }
    },

    methods: {
        renderSublocation({target}) {
            const text = target.innerText.trim()
            if (!this.clickedLocations.includes(text))
                this.clickedLocations.push(text)
            else this.clickedLocations = this.clickedLocations.filter(e => e !== text)
            const children = target.childNodes
            children.forEach(el => {
                this.renderSublocations.push(el.innerText.trim())
            })
            console.log(this.clickedLocations)
        },

    },
    computed: {
        checkSublocation() {
            this.$el.querySelectorAll('.body-sublocation')

        }
    }

})
vm.config.compilerOptions = {delimiters: ['[[', ']]']}
console.log(vm)


vm.mount('#vm')