<template>
    <div class="ui card">
        <div class="content">
            <h5 class="header">{{ this.translateTitle() }}</h5>
            <canvas :id="this.title" />
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js';

export default {
    name: 'GraphCard',
    props: ['graphProp', 'title'],
    data: function() {
        return {
            headerLabels: Object.keys(this.$store.state.graph.data),
            headerText: ''
        }
    },
    mounted() {
        // Generate Chart
        const ctx = document.getElementById(this.title);

        new Chart(ctx, {
            type: 'horizontalBar',
            data: {
                labels: this.getKeys(),
                datasets: [{
                    data: this.getValues(),
                    backgroundColor: this.getRandomColor()
                }]
            },
            options: {
                    legend: {
                        display: false
                    },
                    scales: {
                        xAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
        });

    },
    methods: {
        // Generate Random value of color for graph bar
        getRandomColor: function()  {
            let colorList = [];
            this.graphProp.map(() => {
                var letters = '0123456789ABCDEF'.split('');
                var color = '#';
                for (var i = 0; i < 6; i++ ) {
                    color += letters[Math.floor(Math.random() * 16)];
                }
                colorList.push(color);
            })
            
            return colorList;
        },

        // Get Keys for graph x-axis label
        getKeys: function() {
            return this.graphProp.map(item => item.key);
        },

        // Get Values for graph y-axis label
        getValues: function() {
            return this.graphProp.map(item => item.doc_count);
        },
        
        // Translate Title based on Props
        translateTitle: function() {
            if (this.title === 'is_remote') {
                return this.headerText = 'Remote';
            } else if (this.title === 'location') {
                return this.headerText = 'Location';
            } else if (this.title === 'employment_type') {
                return this.headerText = 'Employment Type'
            } else {
                this.headerText = 'Skills';
            }
            return this.headerText;
        }
    }
}
</script>

<style scoped>
    .ui.card {
        flex: 400px 1;
        margin: 10px;
    }
</style>